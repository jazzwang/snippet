# Interpretab 技術摘要

- Git repo
  - https://github.com/kazunori279/interpretab
- Guide
  - https://kazunori279.github.io/interpretab/
- Slides
  - https://kazunori279.github.io/interpretab/slides/#13

## 2026-08-28

- 這是一個非常有趣的專案，概念有點類似「多拉 A 夢的『翻譯蒟蒻』」。
- 從 LinkedIn 看到以前有互動的 GCP 傳教士 Kaz Sato 看到的貼文
- https://kazunori279.github.io/interpretab/slides/ 超讚的，原來還可以讓投影片自己說話～佩服！！

## 2026-09-01

> 本文根據 [`kazunori279/interpretab`](https://github.com/kazunori279/interpretab) 儲存庫的 README、原始碼、Manifest V3 設定與隱私政策整理。專案版本以 `manifest.json` 所標示的 `1.0.4` 為準。

## 1. 專案定位

Interpretab 是一個 Chrome Manifest V3 擴充功能，將瀏覽器分頁正在播放的音訊，或使用者的麥克風輸入，即時送至 Google Gemini Live API，取得翻譯後的語音與文字字幕。它可用於影片、線上研討會、Google Meet 等情境，也支援將使用者的翻譯語音送回 Meet 通話。

專案採 **Bring Your Own API Key** 模式：沒有自建後端或中繼伺服器，擴充功能直接以 WebSocket 連接 `generativelanguage.googleapis.com`。API 金鑰保存在本機 `chrome.storage.local`，連線時以 WebSocket URL 的 `key` 參數傳送。

核心取捨是低延遲與瀏覽器端實作的簡潔性：音訊不先上傳至專案伺服器，也不落盤保存；但 Gemini API 的使用量與資料處理政策仍由使用者所使用的 Google Cloud 專案與方案決定。

## 2. 功能與翻譯模式

### 2.1 兩個獨立方向

一次執行可同時啟用兩個方向，而且每個方向建立一個獨立的 Gemini Live session：

- **Tab audio**：擷取目前分頁播放的音訊，來源語言由模型自動偵測，翻譯成指定目標語言。
- **Microphone**：擷取麥克風聲音，翻譯成指定語言；可選擇即時同聲翻譯或雙向對話模式。

由於兩個方向各自使用 WebSocket、音訊處理鏈與翻譯狀態，因此同時開啟兩者約等於同時承擔兩個 Live session 的成本。

### 2.2 模型與模式

- **Simultaneous translation**：用於分頁音訊，以及麥克風的預設模式。輸入不中斷地送出，模型不等待完整句子結束即可回傳翻譯；只需要設定目標語言。
- **Two-way conversation**：使用於兩人共用一支麥克風的對話。使用者指定來源與目標語言，透過 `systemInstruction` 要求模型把兩種語言互相轉換。此模式等待 turn 結束，因此延遲較高，但能套用術語表（glossary）。

分頁音訊固定使用 simultaneous 模型，原因是分頁內容可能在不同講者或不同來源語言間切換，預先指定來源語言並不可靠。模型名稱由 `lib/languages.js` 與可選的遠端設定共同決定；`lib/remote-config.js` 可在模型淘汰或更替時提供候選模型，避免必須等待 Chrome Web Store 審核才能更新模型名稱。

## 3. 整體架構

### 3.1 Chrome Extension 上下文

專案將不同生命週期的工作分散到三個主要上下文：

1. **Side panel（`sidepanel.html/js`）**
   - 提供啟停、語言選擇、字幕、靜音、費用與狀態顯示。
   - 面板以分頁為範圍，不會隨意把某一分頁的控制項帶到其他分頁。
   - 重新建立面板時，從 service worker 與 offscreen document 重新取得 transcript、狀態與使用量。

2. **Service worker（`service-worker.js`）**
   - 作為訊息交換與瀏覽器 API 的協調者，不直接持有長時間的音訊、AudioContext 或 WebSocket。
   - 負責建立 offscreen document、呼叫 `chrome.tabCapture.getMediaStreamId()`、處理 action click、保存跨上下文狀態，以及注入字幕與 Meet 麥克風 shim。
   - 因 MV3 service worker 可能在閒置約 30 秒後終止，持久狀態放在 `chrome.storage.session`，不能依賴模組層級變數。

3. **Offscreen document（`offscreen.html/js`）**
   - 以 `USER_MEDIA` 與 `AUDIO_PLAYBACK` 原因建立，負責持有長生命週期的 MediaStream、AudioContext、AudioWorklet 與 Gemini WebSocket。
   - 翻譯引擎、音訊圖與 session reconnect 都集中於此，避免 side panel 關閉或 service worker 重啟時中斷翻譯。

Manifest 使用的主要權限包括 `tabCapture`、`offscreen`、`sidePanel`、`storage`、`activeTab` 與 `scripting`；主機權限只宣告 Gemini API 網域。最低 Chrome 版本為 116。

## 4. 音訊資料流

Offscreen document 中的主要音訊圖如下：

```text
分頁音訊 MediaStream
  ├─ ctxPass（原始取樣率）→ duckGain → 揚聲器
  └─ ctxUp（16 kHz）→ recorder worklet → Tab Live session

麥克風 MediaStream
  └─ ctxUp（16 kHz）→ recorder worklet → Mic Live session

兩個 Live session 的回傳音訊
  └─ ctxDown（24 kHz）→ player worklet → 揚聲器

麥克風翻譯輸出（選擇指定輸出裝置時）
  └─ ctxMicOut（24 kHz、sinkId）→ player worklet → 虛擬音訊線或其他輸出裝置
```

### 4.1 上行音訊

`audio/pcm-recorder-processor.js` 使用 AudioWorklet 讀取 Float32 音訊，將音訊複製後傳回主執行緒。`lib/live-session.js` 將其轉換成 16-bit PCM，取樣率固定為 16 kHz，並以約 32 ms 為單位合併資料，減少 JSON 與 Base64 envelope 的額外負擔。

Gemini Live WebSocket 的上行格式為 JSON，其中 PCM 位元組會 Base64 編碼並包在 `realtimeInput` 結構中；下行訊息則從 `serverContent` 解析出音訊、輸入/輸出轉錄文字、turn boundary 與 usage 資訊。

### 4.2 下行音訊與播放

`audio/pcm-player-processor.js` 以 24 kHz ring buffer 播放 Gemini 回傳的 Int16 PCM。模型可能以高於即時播放速度的 burst 回傳一整句語音，因此播放端以 playhead 連續排程 AudioBuffer，而不是每收到一幀就立即播放。靜音時會清除已排入的音訊佇列，避免按下按鈕後仍持續播放數秒。

分頁擷取會使 Chrome 不再直接把原音播放給使用者，因此 `ctxPass` 負責把原始音訊重新播放出來。翻譯語音播放期間，`duckGain` 將原音降至設定值（預設 15%），翻譯結束後再恢復，形成語音啟動式 ducking，而不是全程降低音量。

## 5. Gemini Live session 設計

`lib/live-session.js` 的 `LiveSession` 代表一條 WebSocket 連線，且不自行重連。它在收到 `setupComplete` 後才將連線視為可用，因為 WebSocket `onopen` 並不代表 API key、模型或 voice 設定已被伺服器接受。

建立 setup frame 時：

- 回應模式設定為 `AUDIO`，並指定預設或使用者選擇的 voice。
- `inputAudioTranscription` 與 `outputAudioTranscription` 放在 setup 層級。
- simultaneous 模式使用 `generationConfig.translationConfig`，設定目標語言與 `echoTargetLanguage: false`。
- conversation 模式使用雙語 `systemInstruction`，並把 glossary 內容編入指令。

### 5.1 Session expiry 與無縫交接

Gemini Live session 會在有限時間後過期，伺服器會先傳送 `goAway`，再關閉連線。`lib/session-loop.js` 將一次翻譯呈現為連續服務：

1. 收到 `goAway` 後立即建立下一條 session。
2. 舊 session 在新 session 完成 handshake 前繼續提供輸出。
3. 舊 session 完成 turn、長時間無回應，或接近期限時，才切換到新 session。
4. 若切換時句子被截斷，保留最近一段有上限的 PCM frame，作為 `preroll` 送入新 session。
5. 對於不會送出 `turnComplete` 的 simultaneous 模式，必要時產生合成的 turn boundary，避免字幕永遠維持開啟狀態。

網路錯誤採用 200 ms 起始、最高 4 秒的退避，連續失敗達上限後停止。配額錯誤與模型已淘汰則不盲目重試，而是直接回報清楚的錯誤或切換候選模型。

## 6. 字幕、轉錄與 glossary

`content/captions.js` 將字幕注入原頁面，使用 Shadow DOM 隔離頁面 CSS，字幕位於畫面底部中央，保留最多三行並支援 fullscreen。字幕大小以 16–64 px 的絕對像素設定，避免受到網站根字型大小影響。

Side panel 保留較完整的 transcript history；offscreen document 會保存有限數量的歷史行（原始碼設定上限為 200），使面板關閉再開啟時能恢復內容，而不讓長時間會議造成無界限的記憶體成長。

Glossary 由 CSV 匯入，格式為：

```csv
source,pronunciation,transcript
Kubernetes,クバネティス,Kubernetes
Cloud Run,クラウドラン,Cloud Run
```

- `source`：原始術語。
- `pronunciation`：要求模型實際說出的發音。
- `transcript`：字幕中顯示的文字，可避免字幕也被改成音標式拼寫。

此功能只對 conversation 模式有效，因為 simultaneous translation 模型不接受 system instruction。

## 7. Google Meet 翻譯麥克風

Meet 整合是專案較特殊的瀏覽器端設計。擴充功能無法在作業系統層註冊新的音訊輸入裝置，因此 `content/mic-shim.js` 只注入 `https://meet.google.com/` 的頁面主世界（`world: "MAIN"`），攔截該頁面的：

- `navigator.mediaDevices.enumerateDevices()`：加入 `Interpretab (translated)` 虛擬音訊輸入。
- `getUserMedia()`：只有當 Meet 明確以該裝置 ID 請求麥克風時，才回傳由 Web Audio 合成的 MediaStream；一般 `{ audio: true }` 維持原本行為。

`content/mic-bridge.js` 位於 isolated world，負責與擴充功能通訊；shim 與 bridge 透過 `window.postMessage` 傳送 24 kHz Base64 Int16 PCM 及狀態。這種分層是必要的：主世界可修改 Meet 所使用的 `navigator.mediaDevices`，但沒有 `chrome.runtime`；isolated world 可與擴充功能通訊，卻看不到頁面真正使用的 JavaScript 物件。

合成麥克風使用 `MediaStreamAudioDestinationNode`，並為 Meet 每次重新取得麥克風建立獨立 destination，避免停止某一條 track 時影響後續重新取得的 track。若 Meet 同時要求攝影機，原始影像 track 會一併保留。

若不使用 Meet 的原生整合，其他網站可透過 `micOutput` 把麥克風翻譯語音送至虛擬音訊裝置（例如 BlackHole 或 VB-Cable），再在會議軟體選取該裝置作為麥克風。原生 Zoom、Teams 桌面程式沒有可注入的分頁，因此不具備同樣的頁面 shim 整合。

## 8. 回音、雙工閘門與靜音

Conversation 模式會在自己的翻譯語音播放期間丟棄麥克風 frame，避免「A 翻成 B、B 又翻回 A」的回音循環；這由 `usesDuplexGate()` 控制。Simultaneous 模式不能使用同樣的閘門，因為其設計就是在使用者仍說話時同步回應，若在第一句翻譯開始播放後封鎖麥克風，後續輸入會全部消失。其他情境依靠瀏覽器 echo cancellation，並建議使用耳機。

兩個即時控制項不會重新建立 session：

- **Microphone mute**：在送出前丟棄麥克風 frame，因此不翻譯，也不計入該段輸入成本。
- **Sound mute**：丟棄尚未播放的翻譯音訊，並清空播放佇列；文字 transcript 仍會繼續接收。

## 9. 狀態、權限與使用者體驗

`lib/next-step.js` 將啟動前置條件統一排序，面板依序提示：API key、至少啟用一個方向，以及麥克風權限。麥克風權限不能由 side panel 可靠地觸發 Chrome 提示框，因此使用者會被導向 Options 頁面完成授權，再由 `navigator.permissions.query()` 監看權限變更。

一次只能存在一個全域翻譯執行，但執行歸屬於特定分頁。其他分頁的面板會顯示目前執行所在的分頁並提供 Stop，而不是讓第二個分頁靜默接管 session。關閉執行所屬分頁時，service worker 會停止整次執行，避免留下使用者看不到但仍持續計費的 session。

## 10. 隱私與資料流

根據 `PRIVACY.md`，擴充功能沒有 analytics、telemetry、廣告、crash reporting 或自建後端。主要資料流如下：

| 資料 | 去向 | 保存位置 |
|---|---|---|
| 分頁音訊 | Google Gemini Live API | 僅在執行期間串流，不落盤 |
| 麥克風音訊 | Google Gemini Live API | 僅在執行期間串流，不落盤 |
| API key | `generativelanguage.googleapis.com` | 本機 `chrome.storage.local` |
| 設定與 glossary | 不上傳 | 本機 `chrome.storage.local` |
| transcript/translation | 面板與頁面字幕 | 主要存在記憶體，面板關閉後消失 |
| 模型名稱與價格設定 | GitHub Pages 靜態設定檔 | 本機短期快取 |

為支援 session 交接，最近數秒的 PCM 會暫存在記憶體中，但停止後會清除。使用者應將 API key 視為密碼，並在 Google Cloud 將其限制為 Gemini API；免費方案是否允許 Google 用資料改善產品，則依 Google Gemini API 的方案條款而定。

## 11. 測試與工程特性

專案以 Node.js 內建測試執行器執行 `tests/**/*.test.js`，測試範圍涵蓋：

- Live session frame 解析、setup 結構與 Base64 PCM 轉換。
- session expiry、重連、退避、配額與模型淘汰。
- 字幕去重、CJK 空白清理與 glossary 顯示映射。
- 麥克風 shim 的裝置列舉、constraints、AudioStream 合成與 teardown。
- tab marker、preflight、設定、使用量計算與多語系訊息。

原始碼大量將跨上下文規則集中成可重用函式，例如 `callMicOn()`、`isSimul()`、`usesDuplexGate()`、`LIVE_KEYS`，降低 side panel、service worker 與 offscreen document 行為不一致的風險。對具有外部副作用的元件，則透過可替換的 Session class、clock 與 fake window 進行測試。

## 12. 限制與評估

1. **需要使用者自己的 Gemini API key**，且費用與配額由該 key 所屬專案承擔。
2. **一次只有一個執行中的翻譯 run**，不能同時翻譯多個分頁。
3. **Chrome/分頁限制**：需要 Chrome 116 以上；tab capture 依賴使用者在目標分頁點擊擴充功能圖示以取得 `activeTab` 授權。
4. **翻譯延遲與模型限制**：simultaneous 模式較低延遲但不支援 glossary；conversation 模式可套用 glossary，但必須等待 turn。
5. **Meet shim 是特定網站整合**：主世界注入增加了與網站實作相容性及商店審查的風險，不能直接推論適用 Zoom 或 Teams。
6. **網路與服務依賴**：Gemini Live preview 模型可能變更或淘汰，雖有遠端模型設定、候選模型與 session handover，仍受 Google API 可用性影響。
7. **輸入/輸出裝置問題**：系統預設麥克風可能是虛擬線、未連接耳機或 HDMI 裝置；專案提供裝置選擇與八秒無聲提示，但無法替使用者判斷實際的聲學環境。

## 結論

Interpretab 的主要技術價值不只是「把語音送進翻譯模型」，而是將 Gemini Live 的即時串流特性與 Chrome MV3 的短生命週期、音訊捕捉限制及會議軟體整合問題一起處理。其設計重點包括：以 offscreen document 保存長生命週期資源、以 AudioWorklet 建立 16 kHz 上行與 24 kHz 下行音訊管線、用雙 session 支援雙向翻譯、以 preroll 與提前交接處理 Live session expiry，以及透過 Meet 頁面主世界 shim 提供合成翻譯麥克風。整體架構偏向本機直連、資料最小化與明確的瀏覽器權限邊界，同時以測試與集中化規則降低多個 extension context 之間的狀態漂移。

**主要參考檔案**：`README.md`、`manifest.json`、`service-worker.js`、`offscreen.js`、`lib/live-session.js`、`lib/session-loop.js`、`lib/settings.js`、`content/mic-shim.js`、`content/mic-bridge.js`、`content/captions.js`、`audio/pcm-recorder-processor.js`、`audio/pcm-player-processor.js`、`PRIVACY.md`。
