# Warp 技術摘要

- Git Repo
  - https://github.com/warpdotdev/warp
- Website
  - https://warp.dev/

## 什麼是 Warp？

[Warp](https://www.warp.dev) 是一個 **「代理開發環境」** ，原本是為終端機設計的。它內建了一個代理（或讓你使用自己的 CLI 代理，如 Claude Code、Codex、Gemini CLI 等），讓開發者能在終端裡直接進行程式碼編寫、測試與專案管理。Warp 的 UI 框架（`warpui_core` 與 `warpui` crate）採用 **MIT licence**，而專案其餘部分則使用 **AGPL v3** 授權。

## 核心特點
- **內建代理**：直接在終端啟動代理，自動處理 issue、撰寫規格、實作 PR 等流程。
- **自訂代理**：支援多種 CLI 代理，靈活接入不同的 AI 模型。
- **Warp Factories**：透過程式碼定義的工廠系統，團隊可以快速建立屬自己的雲端軟體工廠，內建 evals、benchmarks 與自我改進功能。
- **開源貢獻流程**：項目開放原始碼，透過 Issue → PR 的輕量化流程歡迎社區貢獻。貢獻者可以貼上 `ready-to-spec` 或 `ready-to-implement` 標籤，由維護者審核後開始實作。
- **跨平台建置**：提供 `script/bootstrap` 與 `script/run` 來本地編譯與運行，`script/presubmit` 負責格式化、 clippy 與測試。

## 技術棧概觀
- **程式語言**：Rust
- **關鍵依賴**：
  - [Tokio](https://github.com/tokio-rs/tokio) – 異步運行時
  - [NuShell](https://github.com/nushell/nushell) – 新一代殼層
  - [Fig Completion Specs](https://github.com/withfig/autocomplete) – 完成提示規格
  - [Warp Server Framework](https://github.com/seanmonstar/warp) – HTTP 框架
  - [Alacritty](https://github.com/alacritty/alacritty) – 高效能終端機
  - [Hyper HTTP library](https://github.com/hyperium/hyper) – HTTP 客戶端/伺服器
  - [FontKit](https://github.com/servo/font-kit) – 字體處理
  - [Core‑foundation](https://github.com/servo/core-foundation-rs) – macOS 基礎框架
  - [Smol](https://github.com/smol-rs/smol) –輕量執行緒庫

## 如何開始貢獻
1. **搜尋 Issue**：先到 GitHub Issue 頁面檢查是否已有相關 bug 或功能請求。
2. **貼上標籤**：若設計開放，可在 Issue 上貼上 `@oss-maintainers` 申請 `ready-to-spec` 或 `ready-to-implement` 標籤。
3. **撰寫 Spec**：依照 `.md` 規格撰寫設計文件，提交後由維護者審核。
4. **實作 PR**：碼完成後發送 Pull Request，經過 fmt、clippy、測試通過後即可合併。

## 本地開發
```bash
# 下載並編譯
./script/bootstrap   # 平台特定的環境準備
./script/run        # 建置並啟動 Warp
./script/presubmit  # 執行 fmt、clippy 與測試
```
詳細的工程指南請參閱 [`AGENTS.md`](AGENTS.md)。

## 結語
Warp 結合了現代 AI 代理與強大的終端機體驗，讓開發流程更流暢、自動化。其開源的本質與社區友善的貢獻流程，使其成為一個值得關注的項目，無論是想體驗新一代終端，還是希望建立屬於自己的工廠自動化流程，Warp 都提供了豐富的功能與靈活的架構。