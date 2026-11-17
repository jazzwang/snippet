# tsrs 技術報告

## 概述

`tsrs` 是用 Rust 撰寫的 TypeScript 7 編譯器和語言服務器（Language Server）的替換實現。其目標是在保持 100% 相容性的同時，提供更低的記憶體使用和更快的類型檢查效能。

tsrs 是 TypeScript 團隊官方 Go 實現（位於 `microsoft/TypeScript` 倉庫）的函數級別端口，遵循相同的行為規範。任何與 Go 實現的差異都被視為 bug。

倉庫：https://github.com/oxc-project/tsrs

## 安裝步驟

### 方式一：使用 NPM（推薦）

tsrs 以 NPM 套件形式發布，支援自動偵測作業系統和架構並安裝對應的 native binary。

```bash
# 使用 pnpm 安裝（推薦）
pnpm add -D tsrs

# 或使用 npm
npm install -D tsrs
```

安裝後，tsrs 會自動安裝對應平台的 native 套件（如 `@tsrs/win32-x64`、`@tsrs/darwin-x64` 等）。

### 方式二：使用 pnpm dlx（不安裝）

```bash
pnpm dlx tsrs@7.1.0-beta.tsrs2 -p .
```

### 方式三：自編譯（開發或自訂需求）

```bash
# 安裝 Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# 複製倉庫
git clone https://github.com/oxc-project/tsrs.git
cd tsrs

# 安裝 npm 工具鏈（管理 Node.js 24 和 pnpm 12.15.0）
vp install --frozen-lockfile

# 編譯 CLI
cargo build --profile dev -p tsrs_cli

# 編譯 WebAssembly（需要 wasm32-wasip1 目標）
cargo build --profile dev -p tsrs_wasm --target wasm32-wasip1

# 編譯語言服務器測試伺服器
cargo build --profile dev -p tsrs_fourslash_server
```

## 測試步驟

### 基本測試

```bash
# 使用 pnpm 套件
pnpm exec tsrs -p path/to/project          # 編譯並輸出
pnpm exec tsrs -p path/to/project --noEmit # 僅類型檢查
pnpm exec tsrs -p path/to/project --fast   # 啟用效能模式
pnpm exec tsrs --version                    # 檢視版本

# 使用自編譯二進制檔案
./target/debug/tsrs -p path/to/project
```

### 完整測試套件

要運行完整的測試套件，需要準備 TypeScript 參考實現（見「驗證步驟」章節）：

```bash
# 運行符合性測試（conformance tests）
cargo run --profile dev -p tsrs_determinism -- conformance

# 運行 Go 歷史測試
./target/debug/tsrs-test run --suite all --baselines all

# 運行單一測試或測試群組
./target/debug/tsrs-test run --filter <substring>

# 顯示測試結果（預期的 vs 實際的）
./target/debug/tsrs-test show <suite/name>

# 運行語言服務器測試（Fourslash 套件）
.github/scripts/go-fourslash-gate.sh

# 運行回歸測試
tools/regressions.sh target/debug/tsrs

# 運行 Rust 整合測試
cargo test --locked
```

### 效能測試

```bash
# 運行效能基準測試
cargo run --profile dev -p tsrs_determinism -- check --tsrs target/debug/tsrs
```

## 驗證步驟

### 準備 TypeScript 參考實現

tsrs 必須使用與 `Cargo.toml` 中指定的相同 TypeScript commit 進行驗證：

```bash
# 取得 TypeScript commit
commit=$(node npm/build.mjs --print-typescript-commit)

# 克隆並設定 sparse checkout
git clone --filter=blob:none --sparse https://github.com/microsoft/TypeScript ts-ref
git -C ts-ref sparse-checkout set tsc packages/typescript/src \
  packages/typescript/lib packages/typescript/vendor tools/scripts/tsc
git -C ts-ref checkout --detach "$commit"

# 驗證 source pin
test "$(git -C ts-ref rev-parse HEAD)" = "$commit"
git -C ts-ref diff --exit-code HEAD -- tsc packages/typescript

# 安裝 npm 工具鏈
vp install --frozen-lockfile

# 編譯參考編譯器
reference_bin=$(node tools/lib/typescript-reference.mjs --binary)
"$reference_bin" --version
```

### 運行符合性驗證

```bash
# 完整的符合性測試（包含錯誤、類型、symbol、emit 等）
cargo run --profile dev -p tsrs_determinism -- conformance

# 使用 Go 歷史測試
./target/debug/tsrs-test run --suite all --baselines all

# 使用類型和 symbol 基準測試
./target/debug/tsrs-test run --suite all --baselines types,symbols
```

### 語言服務器驗證

```bash
# Fourslash 語言服務器測試
.github/scripts/go-fourslash-gate.sh
```

### 效能測試驗證

```bash
# 確定性測試（與已提交的快照比較）
cargo run --profile dev -p tsrs_determinism -- check --tsrs target/debug/tsrs
```

### 線程安全檢查

```bash
# 運行 ThreadSanitizer 檢查
cargo run --profile dev -p tsrs_determinism -- thread-sanitizer
```

## 效能模式（Fast Mode）

tsrs 提供效能模式（Fast Mode），啟用以下優化：

- 動態調整 checker 數量（根據 CPU 和專案大小，最多 32 個）
- 目錄局部性調度和工作搶奪（work stealing）
- 標準化 checker 歷史處理
- 額外的檢查緩存（union-front、indexed-access、inference-walk）
- 延遲類型成員解析和類型聲明解析
- 記憶體優化（如 eligible 時釋放 leaf 檔案）

啟用方式：

```bash
# 使用 --fast 旗標
pnpm exec tsrs --noEmit --fast

# 使用環境變數
TSRS_FAST=1 pnpm exec tsrs --noEmit

# 在專案設定中設定
TSRS_FAST=1 pnpm exec tsrs -p .
```

### 個別控制選項

- `--checkers N`：設定 checker 線程數量（預設 4）
- `--singleThreaded`：使用單一線程
- `--fast --checkerCostCache <file>`：記住檔案檢查時間以平衡線程
- `--fast --maxMemory <size>`：維持在目標記憶體附近
- `--checkerAssignment go|locality`：檔案分配策略
- `--lazyMembers`：啟用延遲類型成員優化
- `TSRS_LAZY_DTS=1`：啟用延遲類型聲明解析

## 相容性

tsrs 目標是與 TypeScript 7.1 達到 100% 相容性。詳細的相容性表和已知差距請參考 [COMPATIBILITY.md](https://github.com/oxc-project/tsrs/blob/main/docs/COMPATIBILITY.md)。

### 符合性統計（截至 0.25.0）

- **錯誤基準測試**：13,700 個基準測試全部通過
- **類型基準測試**：12,998 個 `.types` 基準測試全部通過
- **Symbol 基準測試**：12,998 個 `.symbols` 基準測試全部通過
- **Emit 基準測試**：13,626 個 `.js` 基準測試全部通過
- **JavaScript Map 基準測試**：149 個基準測試全部通過
- **Source Map 基準測試**：156 個基準測試全部通過
- **Fourslash 語言服務器測試**：4,092/4,562 個測試群組通過

## 語言服務器（LSP）

tsrs 提供完整的 TypeScript 7 語言服務器協議實現，包括：

- 診斷（diagnostics）
- Hover（浮動提示）
- 前往定義（go to definition）
- 參考（references）
- 改名（rename）
- 自動匯入補完（completions with auto-imports）
- 程式碼修正（code fixes）
- 格式化（formatting）

### 編輯器設定

#### VS Code

```jsonc
{
  "js/ts.experimental.useTsgo": true,
  "js/ts.tsdk.path": "./node_modules/tsrs/tsdk",
  "js/ts.trace.server": "verbose"
}
```

或使用 Windows native 套件：

```jsonc
{
  "js/ts.experimental.useTsgo": true,
  "js/ts.tsdk.path": "./node_modules/@tsrs/win32-x64"
}
```

#### Neovim

```lua
vim.lsp.config('tsrs', {
  cmd = { 'tsrs', '--lsp', '-stdio' },
  filetypes = { 'typescript', 'typescriptreact', 'javascript', 'javascriptreact' },
  root_markers = { 'tsconfig.json', 'jsconfig.json', 'package.json', '.git' },
})
vim.lsp.enable('tsrs')
```

## Node.js API

tsrs 提供同步和異步的 Node.js API，支援複雜的編譯場景：

```typescript
import { createSyncSession } from 'tsrs'

const session = createSyncSession({})
const result = session.checkProgram({})
```

詳細文檔請參考 [NODE_API.md](https://github.com/oxc-project/tsrs/blob/main/docs/NODE_API.md)。

## WebAssembly 支援

tsrs 提供 WebAssembly 版本（`@tsrs/wasm`），可在 Node.js 和瀏覽器中使用：

```bash
pnpm add -D @tsrs/wasm
```

詳細文檔請參考 [tsrs-wasm README](https://github.com/oxc-project/tsrs/blob/main/npm/tsrs-wasm/README.md)。

## 類型感知Linting（Type-aware Linting）

tsrs 提供 `tsrs-lint` 命令，可用於 Oxlint 的類型感知規則後端：

```bash
# 使用 tsrs-lint
pnpm exec tsrs-lint

# Oxlint 整合（Oxlint 0.92.0 及以上）
TSRS_FAST=1 pnpm exec oxlint --type-aware --type-check
```

詳細文檔請參考 [tsgolint README](https://github.com/oxc-project/tsrs/blob/main/tools/tsgolint/README.md)。

## 版本管理

tsrs 的版本號包含支援的 TypeScript 版本和 tsrs 本身的修訂號：

- `7.1.0-beta.tsrs1`：針對 TypeScript 7.1.0-beta 的第一個 tsrs 版本
- `7.1.0-beta.tsrs2`：後續修正版本

穩定版 TypeScript 7.1.0 使用 `7.1.0-tsrs1`。

詳細版本說明請參考 [RELEASING_CRATES.md](https://github.com/oxc-project/tsrs/blob/main/docs/RELEASING_CRATES.md)。

## 系統需求

### 開發環境

- **Rust**：使用 `rustup` 安裝（版本由 `rust-toolchain.toml` 指定）
- **Node.js**：24+（由 `.node-version` 管理）
- **pnpm**：12.15.0（由 `package.json` 管理）
- **Git**

### 作業系統

tsrs 支援以下平台：

- **Linux**（x64，需 glibc 或 musl）
- **macOS**（x64 和 Apple Silicon）
- **Windows**（x64，ARM64 從 0.25.0 起支援）

## 開源授權

tsrs 使用 Apache-2.0 授權。詳細資訊請參考 [LICENSE](https://github.com/oxc-project/tsrs/blob/main/LICENSE)。

## 參考資源

- [官方倉庫](https://github.com/oxc-project/tsrs)
- [效能基準](https://github.com/oxc-project/tsrs/blob/main/bench/README.md)
- [工程筆記](https://github.com/oxc-project/tsrs/blob/main/notes/README.md)
- [版本發行記錄](https://github.com/oxc-project/tsrs/blob/main/docs/STATUS.md)
- [效能模式說明](https://github.com/oxc-project/tsrs/blob/main/docs/USAGE.md#performance-options)
