# Lean 4 技術報告

## 概述

Lean 4 是一個形式化驗證定理證明器，由 Microsoft Research 開發。它提供了一種嚴謹的數學語言，用於形式化數學證明、軟體驗證和程式設計。Lean 4 相比於前一代 Lean 3，採用了更現代的功能，包括更好的模式匹配、更強的型別系統和更高效的執行速度。

---

## 系統要求

### 支援平台（Tier 1）

以下平台經過 CI 測試驗證，並提供二進位檔案：

- **Linux**: x86-64，需 glibc 2.27 以上版本
- **macOS**: x86-64 或 aarch64（Apple Silicon），需 macOS 10.15 以上
- **Windows**: x86-64，需 Windows 10 以上

### 次要平台（Tier 2）

以下平台已交叉編譯但未經過 CI 測試：

- aarch64 Linux（需 glibc 2.27+）
- x86（32-bit）Linux
- Emscripten WebAssembly

---

## 安裝步驟

### 推薦方式：使用 VS Code

Lean 的推薦安裝方式是透過 Visual Studio Code 和 Lean 4 VS Code 擴充套件。此方式會自動安裝 Lean 工具鏈，並提供語法高亮、自動補全等開發環境功能。

1. **下載並安裝 VS Code**
   - Windows/macOS/Linux 均可從 [VS Code 官方網站](https://code.visualstudio.com/) 下載
   - 安裝過程中請記住安裝位置（預設為 `%PROGRAMFILES%\Microsoft VS Code\Code.exe`）

2. **安裝 Lean 4 VS Code 擴充套件**
   - 開啟 VS Code
   - 點擊左側擴展圖示（或按 `Ctrl+Shift+X`）
   - 搜尋 "Lean"
   - 安裝 "Lean 4" 擴充套件（leanprover/lean4）

3. **等待自動安裝**
   - 開啟 `.lean` 檔案後，VS Code 會自動下載並安裝對應版本的 Lean
   - 首次使用可能需要數分鐘，後續會自動快取

### 手動安裝：使用 elan

elan 是 Lean 工具鏈管理器，負責安裝和切換不同版本的 Lean 與 lake。

#### 一、安裝 elan

**Linux / macOS（bash 或 zsh）**：

```bash
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
```

執行後會提示：
```
Do you wish to install Elan? [y/N]:
```

輸入 `y` 並按 Enter。

安裝完成後，重新載入終端機或執行：
```bash
source ~/.bash_profile   # 或 ~/.zshrc
```

**Windows（PowerShell）**：

```powershell
iwr -useb https://raw.githubusercontent.com/leanprover/elan/master/elan-init.ps1 | iex
```

#### 二、驗證 elan 安裝

```bash
elan --version
lean --version
lake --version
```

若顯示版本資訊，表示安裝成功。

#### 三、選擇 Lean 版本

elan 會根據專案的 `lean-toolchain` 檔案自動選擇版本。若無此檔案，則使用預設版本：

```bash
# 安裝最新 stable 版本
elan install leanprover/lean4:nightly

# 安裝特定版本
elan install leanprover/lean4:4.28.0

# 查看已安裝版本
elan list
```

---

## 專案建立

### 使用 lake 建立新專案

Lake 是 Lean 的構建系統和套件管理器。

**在當前目錄建立專案**：

```bash
lake init [專案名稱]
```

**在指定目錄建立專案**：

```bash
lake new [專案名稱]
```

### 專案模板選擇

| 模板 | 說明 |
|------|------|
| `std`（預設）| 包含函式庫與可執行程式 |
| `exe` | 僅可執行程式 |
| `lib` | 僅函式庫 |
| `math` | 預設配置 Mathlib、linting 與 CI |

範例：

```bash
# 建立包含函式庫和可執行程式的專案
lake new myproject

# 建立僅為可執行程式的專案
lake new myapp exe

# 建立包含 Mathlib 的證明專案
lake new myproofs math
```

---

## 測試與驗證

### 1. 編譯可執行程式

```bash
lake build
```

編譯完成後，可在終端機執行：

- **Windows**: `.\build\bin\<專案名稱>`
- **Linux/macOS**: `./build/bin/<專案名稱>`

### 2. 執行測試

```bash
lake test
```

若專案使用 Mathlib 測試架構，則會執行所有測試套件。

### 3. 使用 #eval 驗證表達式

在 Lean 程式碼中，使用 `#eval` 立即計算表達式：

```lean4
#eval 2 + 3 * 4      -- 輸出：14
#eval "Hello, World!" -- 輸出："Hello, World!"
```

### 4. 使用 #guard 進行單元測試

```lean4
#guard 1 = 1        -- 若為 true 則通過
#guard "test" ≠ ""   -- 若為 true 則通過
```

此檢查使用不信任的評估器，僅用於快速驗證。

### 5. 使用 LeanTest 測試框架

完整的測試套件可使用 [LeanTest](https://github.com/tim-br/LeanTest)：

```lean4
import LeanTest

open LeanTest

def helloWorldTests : TestSuite :=
  (TestSuite.empty "HelloWorld")
    .addTest "Say Hi!" (fun _ => assertEqual "Hello, World!" HelloWorld.hello)

def main : IO UInt32 :=
  do runTestSuitesWithExitCode [helloWorldTests]
```

執行：

```bash
lake test
```

### 6. HelloWorld 範例

[Lean 4 Samples HelloWorld](https://github.com/leanprover-community/lean4-samples/blob/main/HelloWorld) 提供了最簡單的範例：

```lean4
-- Main.lean
def hello : String := "Hello, World!"

#eval hello
```

編譯與執行：

```bash
lake build
.\build\bin\HelloWorld    -- Windows
./build/bin/HelloWorld    -- Linux/macOS
```

---

## 基本工作流

### 1. 建立專案

```bash
mkdir my-lean-project
cd my-lean-project
lake init math
```

### 2. 撰寫證明

```lean4
-- Main.lean
import Mathlib.Tactic

example : ∀ (n : Nat), n + 0 = n := by
  intro n
  rfl  -- 反射原理證明

example : 2 + 2 = 4 := by
  norm_num  -- 數值化簡
```

### 3. 驗證程式碼

```bash
lake build          -- 編譯並驗證所有證明
lake test           -- 執行測試套件
lake exec           -- 執行可執行程式
```

### 4. 錯誤診斷

若編譯失敗，Lean 會提供詳細的錯誤訊息，包括：
- 型別錯誤
- 證明失敗原因
- 建議的修正方向

---

## 範例：證明畢氏定理

```lean4
-- PythagoreanTheorem.lean
import Mathlib.Tactic

theorem pythagorean_theorem (a b c : ℝ) (h : a^2 + b^2 = c^2) :
  a^2 + b^2 = c^2 := by
  exact h  -- 直接使用假設

-- 或使用 ring  tactic 自動代數化簡
theorem sum_of_squares (a b : ℝ) : a^2 + b^2 = b^2 + a^2 := by
  ring
```

驗證：

```bash
lake build
```

---

## 進階配置

### lakefile.lean 配置

```lean4
import Lake

open Lake DSL

def myLib : Package :=
  mkPythonPackage
    name: "myproject"
   lakeFiles: ["lakefile.lean"]
    src: "src" ∷ []

@[defaultTarget]
def exe : Command :=
  .leanexe "exe"
```

### 指定 Lean 版本

在專案根目錄建立 `lean-toolchain` 檔案：

```
nightly-2023-06-27
```

或指定具體版本：

```
4.28.0
```

---

## 常見問題

### 1. elan 無法找到

**問題**：`command not found: elan`

**解決**：
```bash
# Windows
$env:PATH += ";C:\Users\<使用者>\.elan\bin"

# Linux/macOS
export PATH="$HOME/.elan/bin:$PATH"
```

### 2. lake 無法編譯

**問題**：`lake build` 報錯

**解決**：
```bash
# 清除快取
lake clean
# 重新編譯
lake build
```

### 3. VS Code 未偵測到 Lean

**解決**：
- 重新啟動 VS Code
- 確認已安裝 Lean 4 VS Code 擴充套件
- 檢查 `.lean` 檔案是否正確開啟

---

## 參考資源

- [Lean 官方網站](https://lean-lang.org/)
- [Lean 4 GitHub 倉庫](https://github.com/leanprover/lean4)
- [elan 官方文件](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/)
- [Lake 構建系統](https://lean4.dev/language/projects/lake)
- [Mathlib 函式庫](https://github.com/leanprover-community/mathlib4)
- [Theorem Proving Tutorial](https://leanprover-community.github.io/theorem_proving_in_lean4/)

---

*最後更新：2026-11-16*
