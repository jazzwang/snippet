---
title: "Modern Web Guidance 1.0：您的程式碼開發代理所欠缺的網路平台專業知識 | 部落格"
source: "https://developer.chrome.com/blog/modern-web-guidance-v1"
author:
published: 2026-11-10
created: 2026-11-17
description: "Modern Web Guidance 1.0 將經過專家審核的網路平台技能、瀏覽器相容性資料和程式庫現代化功能帶到您的 AI 程式碼開發代理。"
tags:
  - "clippings"
---

Philip Walton

在代理網路開發這個嶄新時代，開發者**期待**他們的程式碼開發代理能成為網路開發的專家。雖然最新的 frontier coding 模型能力相當強，通常也能產生可運作的程式碼，但如果您請網路開發專家來審閱 AI 產生的程式碼，他們幾乎都能找到讓程式碼更快、更無障礙或更安全的方法。

Chrome 正大力投資未來代理網路開發的未來，為了應對這項挑戰，我們於五月在 Google I/O 上推出了 [Modern Web Guidance 的早期預覽](https://www.youtube.com/watch?v=bo3i0FzDUYo)。Modern Web Guidance 是一組技能，將網路平台專業知識、最佳實踐和瀏覽器相容性資料直接嵌入到您的程式碼開發代理中。

今天，我們很高興宣佈 Modern Web Guidance 1.0 版的穩定版發行，其中包括：

- **新的現代化工作流程**，掃描您現有的程式庫，協助您的代理找出安全現代化的機會。
- **擴充的指南資料庫**，針對數百個經驗證的 AI 知識缺口提供專家審核、跨瀏覽器的解決方案。
- **更深入的專家審核**，每項指南都有內容領域技術主管的簽名認可，我們面向使用者的指南還經過專門的無障礙審查。
- **完整的評估覆蓋率**，所有指南都透過 [公開的評估儀表板](https://goo.gle/mwg-evals) 進行評估，顯示與沒有使用 Modern Web Guidance 的代理相比的可測量改進。

隨著 1.0 版的推出，我們也很高興地分享，Modern Web Guidance 現在正成為跨瀏覽器的努力，[Firefox 和 Edge 已加入 Chrome](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/GOVERNANCE.md#owners) 一起支援、改進跨瀏覽器相容性，並為專案做出贡献。基於我們與 [Baseline](https://web.dev/baseline) 的協同工作，我們的目標是確保任何使用代理進行編程的人都能充分發揮現代網路平台的能力和潛力。

無論您使用什麼模型或代理整合，如果您正在開發網路應用，Modern Web Guidance 都應包含在您的代理工作流程中。

要安裝 Modern Web Guidance，請從您的專案目錄執行以下命令：

```
npx modern-web-guidance@latest install
```

如果您已經安裝了早期版本，可以執行以下命令更新到 1.0：

```
npx modern-web-guidance@latest update
```

如需更多安裝說明或了解更多資訊，請查看 [Modern Web Guidance 文件](https://developer.chrome.com/docs/modern-web-guidance)，或觀看此影片獲得簡要概述：

![](https://www.youtube.com/watch?v=PsrHq5F_BAc)

## 為什麼開發者和企業應該使用 Modern Web Guidance

毋庸置疑，程式碼開發代理已幫助開發者以前所未有的速度編寫程式碼。但在所有人都使用程式碼開發代理的時代，速度已不再是競爭優勢。

如今，在基本因素如易用性和體驗品質上做出差異化比以往更重要。以下是 Modern Web Guidance 能協助的幾種方式：

### 強化模型常忽略的最佳實踐

雖然 frontier coding 模型確實掌握了不少最佳實踐，但我們的 [評估顯示](https://goo.gle/mwg-evals)，它們仍有一些重要領域有所不足，例如：

- **無障礙性**：鍵盤焦點與 inert 管理、reduced-motion 支援、無障礙的表單驗證。
- **使用者體驗**：滑動和觸控手勢、對話框和彈出框的動畫轉換、亮色/暗色主題的實作。
- **效能**：主執行緒任務排程、離屏渲染隔離、版面跳動防止。
- **安全性**：安全的 HTML 清理、嚴格的 Content Security Policies、通行密鑰憑證管理。

無障礙最佳實踐尤其重要，因為錯誤如糟糕的 ARIA 標註反而會讓頁面比完全不使用 ARIA 更難以無障礙使用。就 1.0 版本而言，我們的面向使用者指南已由依賴這些工具的日常無障礙專家進行審核和測試。

想了解模型在各個領域中犯下的具體錯誤，請閱讀 [AI 在網路開發中常犯的十大錯誤](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)。

### 為工作選擇最佳的網路功能

AI 模型在 figuring out 如何用 JavaScript 實現某個功能方面非常擅長，但在許多情況下，HTML 或 CSS 功能可以用更少的程式碼達成同樣效果。而且由於這些功能由瀏覽器處理，通常效能更好，並具備無障礙可用性。例如：

- 用於動畫化彈出框和對話框的功能
- 增強滾動和滑動互動的功能
- 更佳的頁面平滑流暢轉換 API

新功能的推出也能以對使用者重要的方式提升網站體驗。例如：

- **通行密鑰和 WebAuthn**：提供更快速且安全的登入體驗
- **自動填寫**：改善結帳流程（尤其在行動裝置上），這些流程在使用自訂 JavaScript 表單控制時常會失敗

Modern Web Guidance 設計為根據您的瀏覽器支援需求推薦最適合的工作功能。其指南已嵌入 Baseline 和瀏覽器相容性資料，因此可以根據專案需求調整建議。

### 掃描程式庫並找出現代化機會

大多數網路開發不是在全新的專案中進行，而是在累積了數年過時 workaround、不必要依賴和 polyfills 的現有程式庫中進行。

1.0 版本新增了 [現代化工作流程](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow)，可以分析您現有的 HTML、CSS、JavaScript 和 `package.json`，找出安全升級的機會，然後引導您的代理進行變更。

```
/modern-web-guidance Modernize the code in this directory
```

在此次初始發布中，現代化工作流程使用靜態分析檢查有限的模式集合。我們選擇以狹窄範圍開始，產出可預測的結果，然後再逐步擴展。未來我們計劃涵蓋更多領域，包括代理審計（agentic audits），讓您的代理直接推理您的程式碼，而不僅僅是匹配已知模式。

### 隨著網路平台的演進而保持更新

網路平台是一個不斷移動的目標。瀏覽器每個里程碑都會推出新功能，而您之前可能無法使用的一些現有功能，隨著每次新的瀏覽器發行都正在 [成為 Baseline](https://web.dev/baseline#the-baseline-monthly-digest)。

由於 Modern Web Guidance 是建立在 Baseline 相容性資料之上，且其建議由瀏覽器工程師、網路標準專家和無障礙專家維護，這些建議會隨著平台本身一同演進，現在您的專案也能如此。

### 了解新的網路功能和最佳實踐

雖然 Modern Web Guidance 主要是作為代理的工具而設計，但許多開發者告訴我們，他們實際上發現指南本身就非常實用——作為學習資源。

即使在代理編程這個時代，建立領域專業知識仍有價值。而 Modern Web Guidance 可以協助您做到這一點：透過閱讀指南本身，或使用 CLI 搜尋使用案例並發現可能與您的專案相關的新技術。

## 將 Modern Web Guidance 與 Chrome DevTools 搭配使用於代理開發

在代理網路開發中，撰寫程式碼只是工作流程的一部分。您還需要執行該程式碼以確保其按預期運作。這就是為什麼我們建議開發者將 Modern Web Guidance 與 [Chrome DevTools for agents](https://developer.chrome.com/docs/devtools/agents) 一併使用。

- **Modern Web Guidance** 賦予您的代理撰寫符合現代最佳實踐程式碼所需的先驗專業知識。
- **Chrome DevTools for agents** 賦予您的代理執行時可見性，讓它能驗證、除錯並優化程式碼，涵蓋廣泛的裝置能力、使用者偏好和網路條件。

兩者結合可協助您的代理以更少的輪次達到更好的解決方案。以下是如何使用這些工具搭配以最大化效能的幾個範例：

### 優化直到達成績效目標

Modern Web Guidance 可以教導您的代理如何有效地將長執行緒的 JavaScript 任務拆分，但它無法測試您的程式碼，看看這些 JavaScript 任務實際上阻塞主執行緒多久。

使用 Chrome DevTools for agents，您可以在模擬的低端 CPU 上運行效能追蹤，看看是否有問題，然後使用 Modern Web Guidance 的效能建議進行迭代，直到您的程式碼不再阻塞主執行緒超過 50 毫秒（因此不會對 INP 品質產生負面影響）。

### 測試並優化動畫效果

Modern Web Guidance 可以告訴您的代理如何正確且高效地動畫化功能，例如模態對話框、工具提示和彈出選單，但即使有這些指南，您仍然需要驗證這些動畫在您的完整應用程式背景下實際運作且外觀良好。

Chrome DevTools for agents 可以運行您的程式碼、與頁面互動，並錄製動畫實際運作的螢幕錄影。接著它會分析這段錄影，確保動畫確實運作，且符合網站其餘部分的風格和感覺。

您也可以使用 Chrome DevTools for agents 驗證當設定 `prefers-reduced-motion` 時，元件是否尊重使用者的偏好。

### 無記憶體洩漏地快取檢視頁面

Modern Web Guidance 可以教導您的代理如何透過在記憶體中渲染和快取檢視頁面，同時正確地將它們從無障礙樹中隱藏，讓 SPA 的轉換感覺瞬間完成。

然而，在執行此操作時，重要的是確保您正確清理未使用的檢視頁面，以免使用者長時間停留在頁面上時造成記憶體洩漏。Chrome DevTools for agents 具有記憶體除錯工具，因此您的代理可以確保記憶體使用量不會無限制地增加。

若要更詳細地了解如何將 Modern Web Guidance 和 Chrome DevTools for agents 一併使用，請觀看此影片：

![](https://www.youtube.com/watch?v=mogYbZ4CFB8)

## 成功案例

世界各地的工程團隊已經開始使用 Modern Web Guidance 和 Chrome DevTools for agents 來提升程式碼品質、加速交付，並消除手動除錯瓶頸：

### Pensionbazaar 和 Policybazaar

Pensionbazaar 是印度金融科技公司 Paisabazaar 推出的新退休規劃平台，[將 Modern Web Guidance 與 Chrome DevTools for agents 搭配使用](https://developer.chrome.com/blog/policybazaar-agentic-audit) 來建立和驗證新頁面，將返工時間縮短**超過 90%**（從約四天縮短到數小時），並使新螢幕上的 UI 錯誤減少**超過 90%**。其姊妹平台 Policybazaar 是印度領先的保險平台之一，擁有超過 9700 萬名註冊客戶，使用 Chrome DevTools for agents 自動化約 30 個高流量落地頁的效能審計，將手動審計工作減少**92%**：

> "對於 Pensionbazaar，我們的優先事項是從第一天起就建立高品質的程式碼，以避免未來的技術債務。Modern Web Guidance 引導我們的程式碼代理採用現代網路標準和效能最佳實踐，同時尊重我們特定的瀏覽器相容性目標。這使我們的前端程式碼審查變得 substantially 更輕鬆快速，最終改善了我們的開發返工時間。"
> 
> — **Aman Soni**，Policybazaar 工程經理

### WeTV

WeTV 是騰訊的國際串流視訊平台，[在其 CI/CD 流程中加入了 AI 程式碼開發代理](https://developer.chrome.com/blog/wetv-agentic-performance-debugging)，該代理使用 Chrome DevTools for agents 診斷效能退步，並使用 Modern Web Guidance 透過現代網路平台功能修復這些問題。現在該代理可以自動診斷和解決**90% 的效能檢查失敗**，將除錯和解決時間縮短**87%**（從四小時縮短到 30 分鐘，包括人工評估）：

> "結果在速度和品質方面都非常有效。Chrome DevTools for agents 和 Modern Web Guidance 提供的診斷洞察為我們修復複雜版面問題提供了可靠的參考。我們每次修復後都進行嚴格驗證，目前的成功率和穩定性已顯著提升了我們的發布信心。"
> 
> — **Yangjie Zheng**，WeTV（騰訊）工程主管

### note inc.

note inc. 是日本最大的創作人和媒體平台之一，擁有超過 9000 萬名月活躍用戶，[在現代化其 Next.js 前端的持續努力中，將 Modern Web Guidance 與內部設計系統一併使用](https://developer.chrome.com/blog/mwg-with-internal-component)。在對其生產程式庫的 180 次運行評估中，Modern Web Guidance 透過引導代理使用原生 HTML 和 CSS 功能（而非自訂 JavaScript 用於滾動動畫、工具提示和手風琴），將現代網路檢查的通過率從**61% 提升到 94%**。它還通過**431 個已合併的 PR 將正確的 LCP 圖片優先處理提升了 28%**：

> "note 的使命是『開始並持續創作』，因此我們的平台必須對每個創作人和讀者保持快速且無障礙。隨著更多程式碼由 AI 程式碼代理撰寫，Modern Web Guidance 幫助他們追求現代、基於標準的解決方案，而不是退回到較舊的 JavaScript 模式。它也會指出容易忽略的細節，例如圖片載入優先順序和表單無障礙性。結合我們的设计系統，它讓我們在保持 UI 一致性的同時持續改進 note。"
> 
> — **Takehiko Itabashi**，note inc. 技術副總裁

### MetaMask

MetaMask 是一個自託管的金融平台，已在約 190 個國家下載超過 1 億次，[將 Modern Web Guidance 作為自動化審查機器人](https://developer.chrome.com/blog/metamask-modern-web-guidance) 運行在每個對其開源瀏覽器擴展程式的 pull request 上，僅配置了三行的提示。在首五週，該機器人審查了約 480 個 pull request，並針對其中 64 個進行評論，導致工程師修復了**43 項發現**（主要是無障礙性、HTML 語意和表單問題，這些是 linter 無法捕捉的），從評論到修復的中位數時間為**15 分鐘**：

> "這些審查非常有用。它們幫助凸顯並讓我們的工程師熟悉現代 API，例如 Interest 觸發器和 Popover API。這並沒有增加 PR 審查時間，如果有的話，可能還減少了。MWG 捕捉到的問題，否則需要熟悉這些現代網路技術的人類審查員來處理。"
> 
> — **Francis Nepomuceno**，MetaMask UX 工程師

## 生態系和社群支援

Modern Web Guidance 起源於 Chrome 內部的倡議，但達到這個 1.0 里程碑是與網路社群眾多專家協同努力的结果。

感謝監督每個網路平台領域的內容技術主管、Firefox 和 Edge 的瀏覽器合作伙伴、撰寫和測試指南的獨立網路標準與無障礙專家，以及所有在 [GitHub 上做出贡献的開源貢獻者](https://github.com/GoogleChrome/modern-web-guidance-src/graphs/contributors)，他們共同塑造了此次發布！

如果您發現程式碼代理在網路知識上有缺失，或想協助改進現有指南，請查看 [貢獻指南](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/CONTRIBUTING.md) 參與其中。

## 開始使用 Modern Web Guidance

要將 Modern Web Guidance 加入您的專案，請從專案目錄執行 CLI 安裝程式：

```
npx modern-web-guidance@latest install
```

如果您已經安裝了早期版本，可以執行以下命令更新到 1.0：

```
npx modern-web-guidance@latest update
```

除了 CLI 之外，您還可以直接透過大多數流行程式碼開發代理的插件市場安裝和更新 Modern Web Guidance，包括 Claude Code、Codex、Cursor、Antigravity、Copilot、WebStorm、Kimi Code 和 Grok Build。

![支援 Modern Web Guidance 的程式碼代理和 IDE 的標誌：Codex、Cursor、Kimi、Google Antigravity、Grok、JetBrains WebStorm 和 GitHub Copilot。](https://developer.chrome.com/static/blog/modern-web-guidance-v1/image/agent-marketplaces_2880.jpg)

若要了解更多，請查看以下資源：

- [Modern Web Guidance 文件](https://developer.chrome.com/docs/modern-web-guidance)
- [評估儀表板](https://goo.gle/mwg-evals)
- [GitHub 儲存庫](https://github.com/GoogleChrome/modern-web-guidance)
- [YouTube 影片播放清單](https://www.youtube.com/playlist?list=PLKkLHHhafabo)
- [AI 在網路開發中常犯的十大錯誤](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev)
