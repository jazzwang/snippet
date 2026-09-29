# VoiceStudio

- Git Repo
  - https://github.com/debpalash/VoiceStudio
- Website
  - https://voicestudio.sh/

## 2026-09-28

- Learn from Alpha Signal

> [!QUESTION]
> 參考 https://github.com/debpalash/VoiceStudio 撰寫一篇技術簡介，並說明如何 step-by-step 測試，最後使用 speak-human-tw skill 潤飾詞句，不必列清單，請直接修改，最後將結果新增至 voicestudio.md

## VoiceStudio 技術簡介與測試指南

VoiceStudio 是一個開源、主打在地端運行的語音工作平台，支援多達 646 種語言。它把語音複製、語音設計、影片配音、語音聽寫以及有聲書製作等功能，全部整合進一個乾淨、流暢的 Electron 桌面應用程式中。

這款工具最大的特色在於它不依賴外部雲端服務，所有運算都在你自己的電腦硬體上跑，完全不用擔心個人隱私外洩。

---

### 技術架構剖析

VoiceStudio 採用雙通訊埠（Port）的分工架構，把系統底層控制與機器學習資料流切分得非常清楚：

#### Python FastAPI 後端（Port 3900）
這個服務負責處理核心的 AI 與機器學習模型。為了讓語音合成（TTS）與轉寫（ASR）的反應足夠靈敏，後端會常駐於記憶體中，讓模型保持在「暖機」狀態。
* **語音合成（TTS）**：預設採用 `k2-fsa/OmniVoice`，同時相容 CosyVoice 3、IndexTTS 2.5、MOSS-TTS 等多種開源模型。
* **語音辨識與聽寫（ASR）**：預設採用 `WhisperX`，並支援適合即時聽寫、資源佔用更低的 `sherpa-onnx`。
* **開發者友善介面**：提供與 OpenAI 相容的 API 端點、用於即時語音串流的 WebSocket 介面，以及能直接讓 AI 代理（如 Claude Code 或 Pi）串接的 MCP（Model Context Protocol）伺服器。

#### Rust 控制側車（Port 3902）
隨 Electron 桌面程式一同啟動的背景控制元件，專門解決跨平台作業系統的硬體與輸入權限問題：
* **原生系統控制**：接管麥克風啟用狀態，並精準捕捉當前作業系統的游標焦點。
* **安全文字遞送**：利用剪貼簿防護機制，將辨識出的文字自動打進你目前正在輸入的視窗（例如 Notion、VS Code 或瀏覽器），不會干擾原本的操作節奏。
* **本機安全性防護**：這個元件僅綁定本機的 `127.0.0.1` 迴圈位址，並主動拒絕非信任來源的瀏覽器 `Origin` 要求，防止惡意網頁偷偷啟用你的麥克風。

---

### Step-by-Step 測試指南

以下是完整的環境建立與功能驗證流程。不論你是想直接測試打包好的桌面程式，還是想從原始碼建置開發版，都可以依照這些步驟進行。

#### 步驟一：準備測試環境

你可以到 GitHub Releases 頁面下載編譯好的 Electron 安裝檔，或者在本地端從原始碼直接跑起來：

1. 複製 GitHub 專案：
   ```bash
   git clone https://github.com/debpalash/VoiceStudio.git
   cd VoiceStudio
   ```
2. 安裝 Node.js 前端依賴（本專案使用 Bun 套件管理器）：
   ```bash
   bun install
   ```
3. 初始化 Python 後端虛擬環境並下載必要的相依套件：
   ```bash
   bun run setup:api
   ```
4. 啟動 Electron 開發版介面：
   ```bash
   bun run dev
   ```

*(備註：如果你想快速驗證打包封裝後的版本是否正常，可以執行 `bun run smoke-test` 進行煙霧測試。)*

---

#### 步驟二：驗證後端 API 與健康狀態

當桌面程式成功啟動後，後端服務會預設在 `http://127.0.0.1:3900` 運作。

我們可以用終端機發送幾條簡單的請求，確認語音資料面是否準備就緒：

1. **確認後端健康狀態**：
   ```bash
   curl http://127.0.0.1:3900/health
   ```
   *若正常運作，會回傳代表後端健康的 JSON 資訊。*

2. **探索語音功能宣告**：
   ```bash
   curl http://127.0.0.1:3900/.well-known/voicestudio-speech
   ```
   *這會回傳類似 `voicestudio.speech.v1` 的通訊協議規格，代表 ASR 與 TTS 資料通道已準備就緒。*

---

#### 步驟三：管理與安裝本地語音模型

在開始合成語音前，必須先確保所需的模型已經下載到你的電腦中。

1. **查詢本機模型狀態**：
   ```bash
   curl http://127.0.0.1:3900/models
   ```
   *這會列出本機上所有的語音合成與轉寫模型。如果 OmniVoice 的 `"installed"` 顯示為 `false`，代表尚未下載。*

2. **觸發模型下載**（以預設的 OmniVoice 為例）：
   ```bash
   curl -X POST http://127.0.0.1:3900/models/install \
     -H "Content-Type: application/json" \
     -d '{"repo_id": "k2-fsa/sherpa-onnx-tts-cosyvoice-zh-2024-07-07"}'
   ```
   *你可以透過 `GET http://127.0.0.1:3900/models/install/status` 輪詢下載進度，直到狀態顯示為下載完成，且 `/models` 列表中的 `"installed"` 轉為 `true`。*

---

#### 步驟四：測試語音合成（TTS）與複製

1. 開啟 VoiceStudio 桌面程式。
2. 點選進入 **Voice cloning**（語音複製）工作區。
3. 匯入或現場錄製一段乾淨的參考聲音範例（WAV 格式）。
4. 在文字輸入框中打入你想合成的對話。
5. 點擊 **Generate**（生成），生成完畢後點擊播放。確認聲音沒有嚴重雜音、語速正常且語調自然。

---

#### 步驟五：測試全局聽寫與原生文字輸入

這個步驟用來驗證 Rust 側車（Port 3902）跟系統輸入焦點的協作是否完美：

1. 打開一個你常用的文字編輯器（例如 Windows 記事本或 VS Code），並將游標停留在編輯區域。
2. 在終端機執行指令，啟動聽寫：
   ```bash
   curl -X POST http://127.0.0.1:3902/v1/dictation/start
   ```
3. 對著麥克風說幾句話，結束後執行指令停止聽寫：
   ```bash
   curl -X POST http://127.0.0.1:3902/v1/dictation/stop
   ```
4. **觀察結果**：語音辨識結束後，辨識出來的文字會自動在剛才游標停駐的位置輸入。這證明 Rust 側車的原生輸入與剪貼簿安全遞送功能均正常運作。
