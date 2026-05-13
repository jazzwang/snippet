# browser-harness

> Browser Harness | Self-healing harness that enables LLMs to complete any task.

- Git Repo
  - https://github.com/browser-use/browser-harness
- Website
  - https://browser-harness.com/

## 2025-05-13

- Learn from https://www.linkedin.com/feed/update/urn:li:activity:7451625476818640896/

```
不只有 Harness Agent，連瀏覽器也需要 Browser Harness！

Browser Use 團隊最近開源出一個有趣的專案 Browser Harness，整個框架只有約 592 行程式碼，卻能讓 LLM 完整操控瀏覽器。

其中最特別的設計叫 self-healing，也就是 Agent 執行任務時若發現工具不夠用，能直接修改 harness 原始碼把函式補上，然後繼續完成任務。

這種自我修復能成立，關鍵在於 Browser Harness 刻意把抽象層減到最少，它直接建構在 Chrome DevTools Protocol 之上，中間沒有任何多餘的包裝。作者認為，厚重的框架反而會拖累 LLM 的推理能力，包裝越少，Agent 越能發揮全部實力。

這套「讓 Agent 自己補上缺口」的邏輯，還延伸到了 domain-skills 資料夾。Agent 處理某個網站時累積的Selector、流程與限制條件，會由 Agent 自己寫成 skill 檔案供日後共用。下次再處理同樣的網站，這個 skill 會被載入，Agent 就不用重新摸索一次。
```