# Pi Coding Agent

- Git Repo
  - https://github.com/earendil-works/pi
- Website
  - https://pi.dev/

## 2026-06-10

- 安裝：
```bash
~/git/snippet/js/pi-coding-agent$ npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

## 2026-08-03

- 唐鳳寫了 `pi-ds4` 的文件 https://pi.audreyt.org/
  - https://github.com/audreyt/pi-ds4
  - 看起來是 fork https://github.com/mitsuhiko/pi-ds4 並加入一些文件修改

## 2026-09-01

- 目標：想要讓 Pi Coding Agent 支援使用 OpenCode Zen (Free) 的 LLM Model

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
pi code agent 可以使用 opencode zen 的模型嗎?若可以,該如何設定?
</td></tr><tr><td>A:</td><td>

是的，Pi Code Agent 可以完全支援 OpenCode Zen 的模型。 [1]

Pi Agent（pi-ai）的核心優勢之一是擁有一個統一的接口，支援包括 OpenCode 在內超過 20 家供應商的模型。設定的核心邏輯在於配置 OpenCode Zen 的 API Key，並使用 OpenAI 兼容的 API 端點（Base URL） 來進行對接。 [2, 3]

以下是具體的設定與使用步驟：

### 1. 取得 OpenCode Zen 的 API Key

   1. 前往 [OpenCode 官方後台](https://opencode.ai/)。
   2. 建立一組用於 Zen 服務的 API Key（請注意不要與免費的公共 Key 混淆，需使用個人生成的金鑰）。 [1]

### 2. 設定環境變數

為了讓 Pi Agent 能夠讀取到 OpenCode Zen 的憑證與伺服器位置，您需要在終端機（Terminal）中設定以下兩個環境變數： [3]

* OPENAI_API_KEY：填入您的 OpenCode Zen API Key。
* OPENAI_BASE_URL：填入 OpenCode Zen 的 API 接入點 https://opencode.ai/zen/go/v1/（或官方指定的 OpenAI 兼容端點）。 [1, 2]

在 Linux / macOS 設定方法：

```bash
export OPENAI_API_KEY="你的_opencode_zen_api_key"
export OPENAI_BASE_URL="https://opencode.ai/zen/go/v1/"
```

在 Windows (PowerShell) 設定方法：

```powershell
$env:OPENAI_API_KEY="你的_opencode_zen_api_key"
$env:OPENAI_BASE_URL="https://opencode.ai/zen/go/v1/"
```

(註：若希望每次開啟終端機都生效，請將上述指令寫入您的 .bashrc、.zshrc 或系統環境變數中。)

### 3. 呼叫與切換模型

設定完成後，在啟動 Pi Agent 時，使用 --model 參數來指定 OpenCode Zen 所提供的模型 ID 即可。
例如，呼叫 OpenCode Zen 平台上常見的 MiniMax M3 或 GLM 5.2 模型： [4]

```
# 使用 MiniMax M3 模型啟動 Pi Agent
pi --model minimax/m3
# 或者使用 GLM 模型
pi --model glm/5.2
```

### 💡 實用小提示

* 前綴字注意：由於是透過 OpenAI 兼容端點接入，有時根據 Pi 版本的不同，模型名稱可能需要加上前綴（例如 openai/minimax-m3 或 opencode-go/minimax-m3）。若遇到無法識別，可透過 pi models list（或對應命令）檢查當前供應商辨識出的 ID 格式。 [5, 6]
* 計費確認：OpenCode Zen 屬於按量計費（Pay-as-you-go）機制。開始高強度的 Coding 任務前，請確保您的 OpenCode 帳戶內有足夠的點數或額度。 [5]

如果您在執行 pi --model 時遇到特定的錯誤訊息，可以告訴我錯誤代碼或終端機回應，我能協助您進一步排查是網路端點（Base URL）還是憑證（API Key）的問題！

[1] [https://www.reddit.com](https://www.reddit.com/r/opencodeCLI/comments/1sv00z6/free_models_on_zen_and_pi/?tl=zh-hant)
[2] [https://github.com](https://github.com/farion1231/cc-switch/issues/4459)
[3] [https://altsol.tw](https://altsol.tw/pi-agent-install-guide)
[4] [https://opencode.ai](https://opencode.ai/docs/zh-tw/zen/)
[5] [https://laplusda.com](https://laplusda.com/posts/openclaw-opencode-go-setup/)
[6] [https://lzw.me](https://lzw.me/docs/opencodedocs/zh-tw/code-yeongyu/oh-my-opencode/platforms/provider-setup/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
可以設定在 pi code agent 的設定檔中嗎?
</td></tr><tr><td>A:</td><td>

可以，Pi Code Agent 完全支援將模型供應商與憑證直接寫在設定檔中。這樣您就不用每次開啟終端機都重新輸入環境變數。 [1]

在 Pi Agent 中，這些自訂供應商的資訊可以透過編輯 ~/.pi/agent/ 目錄下的兩個關鍵檔案來設定：models.json（配置供應商與模型列表）與 auth.json（放置 API 金鑰）。 [2, 3]

以下是將 OpenCode Zen 寫入設定檔的具體做法：

### 1. 配置模型與 API 端點 (models.json)

請在全域設定目錄 ~/.pi/agent/ 底下建立或修改 models.json 檔案，將 OpenCode Zen 偽裝成自訂的 openai 相容供應商（也可以另外命名為 opencode）： [4]

```json
{
  "providers": [
    {
      "name": "opencode-zen",
      "baseUrl": "https://opencode.ai",
      "apiKey": "$OPENCODE_ZEN_KEY"
    }
  ],
  "models": [
    {
      "provider": "opencode-zen",
      "id": "minimax/m3"
    },
    {
      "provider": "opencode-zen",
      "id": "glm/5.2"
    }
  ]
}
```

(註：apiKey 欄位如果填寫 $OPENCODE_ZEN_KEY，代表它會去抓取您在下一步 auth.json 中設定的對應變數。) [2]

### 2. 安全地配置 API 金鑰 (auth.json)

為了避免將機密金鑰直接暴露在公開的專案或模型設定中，Pi Agent 推薦將密碼類資訊獨立放在 ~/.pi/agent/auth.json 檔案內： [3, 5]

```json
{
  "OPENCODE_ZEN_KEY": "你的_opencode_zen_api_key"
}
```

### 3. 將其設定為預設啟動模型 (settings.json)

如果您希望每次直接輸入 pi 啟動時，預設就使用 OpenCode Zen 的模型，您可以去修改全域設定檔 ~/.pi/agent/settings.json： [3, 6]

```json
{
  "defaultModel": "minimax/m3"
}
```

### 💡 互動式儲存技巧（更簡單）

除了手動修改 settings.json 外，您也可以透過 Pi Agent 內建的指令直接將當前選擇儲存到設定檔中： [7]

   1. 在終端機進入 Pi Agent：輸入 pi
   2. 輸入 \model 切換到您想要的 OpenCode 模型。
   3. 停留在該模型上時，按下 Ctrl + S，Pi Agent 就會自動將該模型儲存為每次啟動的預設值！ [7]

這樣一來，不論是 OpenCode Zen 的連線 API 位置、金鑰還是預設模型，都能完美脫離臨時的環境變數，永久保存在設定檔中。您目前在設定這些 .json 檔案時，有遇到語法報錯或找不到路徑的問題嗎？

[1] [https://altsol.tw](https://altsol.tw/pi-agent-install-guide)
[2] [https://bertomill.medium.com](https://bertomill.medium.com/pi-coding-agent-setup-free-ai-models-via-openrouter-full-guide-fd40ea5dadb4)
[3] [https://github.com](https://github.com/LEUNGUU/pi-agent-config)
[4] [https://docs.ai.it.ufl.edu](https://docs.ai.it.ufl.edu/docs/navigator_toolkit/integrations/pi/)
[5] [https://github.com](https://github.com/HazAT/pi-config)
[6] [https://pi.dev](https://pi.dev/docs/latest/settings)
[7] [https://pi.dev](https://pi.dev/docs/latest/settings)

</td></tr>
</table>
- 以上實測失敗，改試以下步驟：

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
pi agent 怎麼下指令直接使用 opencode zen 的模型？
</td></tr><tr><td>A:</td><td>

在 Pi Agent (pi-coding-agent) 中，最直接、最優雅的指令下法是利用 Pi 的擴充套件系統 (Pi Packages) 或內建的交互式斜線指令 (Slash Commands)。 [1, 2]
以下是三種最推薦的直接操作指令：

### 方法一：使用最快、免 Key 的官方社群插件（強烈推薦）

Pi 社群有專門為 OpenCode Zen 封裝好的套件，完全不需要手動填寫 Base URL 或 API Key。 [1]

1.  安裝 OpenCode Zen 插件：

    在您的終端機輸入：

    ```bash
    pi install npm:pi-opencode-zen
    ```

2.  重啟或重新載入 Pi：

    ```
    pi
    ```

    *(進入交互介面後輸入 `/reload` 即可生效)*
3.  下指令切換模型：
    在對話框中輸入：

    ```
    /model
    ```

    然後直接用鍵盤上下鍵選擇 `opencode-zen` 分類下的模型（例如 `deepseek-v4-flash-free`）即可直接開用！ [1, 3, 4]

### 方法二：使用內建的 `/login` 互動指令（標準綁定）

如果您使用的是 OpenCode Zen 官方付費/個人訂閱帳戶，想使用專屬的 API Key，Pi Agent 內建了引導設定指令： [5]

1.  啟動 Pi Agent：
    ```
    pi
    ```

2.  在 Pi 的對話框中輸入登入指令：
    ```
    /login
    ```

3.  介面會跳出選單，請選擇 `Use a subscription`。
4.  在供應商列表中選擇 `OpenCode Zen` 或 `OpenCode`。
5.  終端機會提示 `Enter API key:`，直接貼上您的 OpenCode Zen API 金鑰並按下 Enter。
6.  綁定成功後，輸入 `/model` 就能直接切換到該平台底下的所有付費與免費模型了！ [5, 6]

### 方法三：使用 CLI 單行參數指令（適合腳本與自動化）

如果您不想進入 Pi 的互動視窗，想直接在終端機「一氣呵成」指定供應商與模型來執行單次任務，可以使用單行 CLI 指令： [7, 8]

-   語法格式：
    ```
    pi --provider opencode-zen --model [模型名稱] -p "[你的提示詞]"
    ```

-   實際執行範例：
    ```
    pi --provider opencode-zen --model deepseek-v4-flash-free -p "幫我檢查這個目錄下的 index.ts 有沒有記憶體洩漏"
    ```

    [3, 8]

### 💡 小提醒

如果您使用方法三，請確保已經像前一個問題提到的一樣，將 `~/.pi/agent/auth.json` 或環境變數中的 Key 設定好，否則 CLI 參數會因為找不到憑證而報錯。 [9]
您目前手上的 OpenCode 帳號是免費免登入的，還是有儲存點數的個人 API Key 呢？我可以根據您的帳號類型推薦最適合的模型 ID！

[1] [https://pi.dev](https://pi.dev/packages/pi-opencode-zen?name=%25s&page=108)
[2] [https://www.glukhov.org](https://www.glukhov.org/ai-devtools/pi/pi-coding-agent-review/)
[3] [https://github.com](https://github.com/luongnv89/pi-extensions/blob/main/extensions/opencode-pi/README.md)
[4] [https://bertomill.medium.com](https://bertomill.medium.com/pi-coding-agent-setup-free-ai-models-via-openrouter-full-guide-fd40ea5dadb4)
[5] [https://pi.dev](https://pi.dev/packages/pi-opencode-provider?page=35)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=20vcJmqAr4M)
[7] [https://aiidelist.com](https://aiidelist.com/pi-coding-agent-cheatsheet)
[8] [https://m.runoob.com](https://m.runoob.com/pi-agent/pi-agent-appendix-cli.html)
[9] [https://www.reddit.com](https://www.reddit.com/r/PiCodingAgent/comments/1vltdm9/how_to_use_deepseekv4flashfree_model_from/)
</td></tr>
</table>

- 後來用 `/login` 比較容易解決。選擇 `Open Code Zen (Free)` 然後選輸入 `API Key`

## 2026-09-04

> [!QUESTION]
> 我用指令啟動了 llama.cpp 的 server,可以給我 step-by-step 設定 Pi Coding Agent (https://pi.dev) 連上 http://127.0.0.1:8080 的方法嗎?
> ```
> 0.13.009.715 I srv llama_server: server is listening on http://127.0.0.1:8080
> ```

要讓 Pi Coding Agent ([pi.dev](https://pi.dev/)) 連上你已經啟動的 llama.cpp server (`http://127.0.0.1:8080`)，你需要透過修改 Pi 的 `models.json` 設定檔，將其作為自定義的 OpenAI 兼容端點（OpenAI-compatible endpoint）讀入。 [1]
請按照以下 Step-by-Step 步驟設定：

### 步驟 1：建立或修改 `models.json`

Pi 會自動讀取使用者家目錄下的全域設定。請在你的終端機中，於指定路徑建立或編輯 `models.json`： [2]

-   檔案路徑： `~/.pi/agent/models.json`
-   如果 `~/.pi/agent/` 資料夾不存在，請先手動建立：
    ```bash
    mkdir -p ~/.pi/agent
    ```

### 步驟 2：貼入自定義 Provider 設定

使用文字編輯器打開 `~/.pi/agent/models.json`，並填入以下內容：
```json
{
  "providers": {
    "local-llama": {
      "baseUrl": "http://127.0.0",
      "api": "openai-completions",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "your-model-name",
          "name": "Local Llama",
          "contextWindow": 32000,
          "maxTokens": 4096
        }
      ]
    }
  },
  "defaultProvider": "local-llama",
  "defaultModel": "your-model-name"
}
```

#### ⚠️ 注意事項與參數調整：

1.  `baseUrl`：務必在 `http://127.0.0.1:8080` 後面加上 /v1，因為 `llama.cpp` 的 OpenAI 兼容路由群組位於 `/v1/chat/completions`。
2.  `id`：請改為你目前在 `llama.cpp` 中載入的模型名稱（如果不知道，可以用 `curl http://127.0.0` 查詢其產生的 `id`）。
3.  `compat`：設定 `supportsDeveloperRole: false` 可以防止 Pi 誤發送新版 OpenAI 的 `developer` 角色，確保本機相容性。
4.  `contextWindow`：請根據你啟動 `llama.cpp` 時設定的 `-c`（Context Size）填寫正確數值，避免 Pi 發生 Token 溢出。
5.  模型能力提示：Coding Agent 需要模型具備強大的程式碼編輯與 Tool Calling（工具呼叫）能力。如果本機模型太小或不支援 Tooling，Agent 運作時可能會頻繁出錯。 [3, 4, 5, 6, 7, 8]

### 步驟 3：設定虛擬 API Key（若有需要）

某些版本的 Pi 或背後的連接套件會強制檢驗是否有 API Key。
如果遇到連線驗證問題，請建立 `~/.pi/agent/auth.json` 檔案： [6, 9]

```json
{
  "local-llama": {
    "type": "api-key",
    "key": "not-needed-for-local"
  }
}
```

*(註：`llama.cpp` 預設不需要 Key，這裡隨便填寫一個非空字串即可放行。)* [6]

### 步驟 4：啟動 Pi Coding Agent 測試

完成設定後，切換到你的專案目錄下，直接輸入指令啟動：
```bash
pi
```

進入介面後，你可以輸入 `/model` 或 `/status` 檢查當前使用的模型是否已成功切換為 Local Llama。

你在 `llama.cpp` 端有看到任何 `POST /v1/chat/completions` 的連線日誌跳出來嗎？如果連線時跳出特定錯誤，請告訴我，我來幫你微調 `compat` 的參數！

[1] [https://skywirex.com](https://skywirex.com/pi-agent-custom-llm/)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=N30XGyPrr6I)
[3] [https://github.com](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)
[4] [https://ofox.ai](https://ofox.ai/blog/pi-coding-agent-custom-provider-setup-2026/)
[5] [https://medium.com](https://medium.com/@michael.hannecke/building-a-sovereign-coding-agent-on-apple-silicon-with-pi-and-mlx-swift-ef9bb23cafe2)
[6] [https://zarar.dev](https://zarar.dev/run-a-local-coding-model-with-pi-and-lm-studio/)
[7] [https://voipnuggets.com](https://voipnuggets.com/2026/07/12/how-to-run-local-ai-coding-agent-mac/)
[8] [https://thomas-wiegold.com](https://thomas-wiegold.com/blog/pi-coding-agent/)
[9] [https://pi.dev](https://pi.dev/packages/pi-sub2api-provider)

> [!QEUSTION]
> 可以用 `/login` 設定嗎?

無法直接透過 `/login` 指令來完成本機 `llama.cpp` 的所有連線設定。 [1]

在 [Pi Coding Agent (pi.dev)](https://pi.dev/) 的架構中，`/login` 主要用途是設定雲端供應商的 API Key 或 OAuth 登入。雖然它能幫你寫入部分的認證金鑰，但對於你自架的本機服務，`/login` 並無法幫你設定自定義的 `baseUrl`（例如 `http://127.0.0`）或宣告自訂的模型名稱與 Context 窗口大小。 [1, 2, 3, 4, 5]

不過，如果你希望盡可能少去手動編輯 JSON 檔案，你可以利用官方社群專門為本機模型開發的擴充套件（Extension）來大幅簡化這個流程。


### 💡 替代方案：使用 `pi-local-models` 自動偵測（免手動改 JSON）

[Pi 官方包管理器](https://pi.dev/packages/pi-local-models) 提供了一個名為 `pi-local-models` 的擴充功能，它能自動掃描並綁定本機相容 OpenAI 端點的服務（包含 `llama.cpp`、`Ollama`、`LM Studio` 等）。 [6]

#### 步驟 1：在終端機安裝本機模型套件

直接使用 Pi 的內建套件管理指令進行安裝： [6]
```bash
pi install npm:pi-local-models
```

#### 步驟 2：用環境變數直接啟動 Pi

安裝完成後，你連 `models.json` 都不需要建立。只需要在啟動 `pi` 時，前面加上 `LLAMA_API_URL` 或透過預設路由，它就會自動對接。或者你可以直接一行指令把端點餵給它：

```bash
# 告訴 Pi 本機端點的位置，它會自動完成其餘的相容性對接
LOCAL_MODEL_URL="http://127.0.0.1:8080" pi
```

#### 步驟 3：進入後切換模型

進入 Pi 的互動式介面後，你就可以像平常一樣使用斜線指令來切換至你本機的模型了： [6]
```
/models
```

此時選單中會出現它從你的 `llama.cpp` 伺服器自動抓取到的本機模型名稱，點選即可直接開始使用。 [6]

如果你想確認你的 `llama.cpp` 伺服器是否有正常回應，或者在安裝過程中遇到特定報錯，歡迎隨時告訴我！

[1] [https://pi.dev](https://pi.dev/docs/latest/quickstart)
[2] [https://pi.dev](https://pi.dev/)
[3] [https://pi.dev](https://pi.dev/docs/latest/providers)
[4] [https://stackoverflow.max-everyday.com](https://stackoverflow.max-everyday.com/2026/08/pi-coding-agent-llama-server/)
[5] [https://pi.dev](https://pi.dev/docs/latest/custom-provider)
[6] [https://pi.dev](https://pi.dev/packages/pi-local-models)

## 2026-09-06

- 在參考過以下兩個連結後，發現可以從 llama.cpp Web UI 查到不同模型的參數設定，其次就是 Pi Coding Agent 該如何設定才能連上本機的 llama.cpp server。
  - https://stackoverflow.max-everyday.com/2026/08/pi-coding-agent-llama-server/
  - https://pi.dev/docs/latest/llama-cpp
- 首先，先啟動 llama.cpp 的 router mode
> [!TIP]
> 以下是實際測試過程，意外發現 llama.cpp 已經有自己的 Web UI

```bash
[09/06 15:12:06] ~$ mkdir -p .models
[09/06 15:13:06] ~$ cd .models/
[09/06 15:14:47] ~/.models$ wget -c https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-7B-Instruct-Q4_K_M.gguf
[09/06 15:15:05] ~/.models$ wget -c https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF/resolve/main/Qwen3.5-9B.Q4_K_M.gguf
[09/06 15:15:51] ~/.models$ llama-server --models-dir ~/.models
```
- 接著，手動設定
```bash
~$ vi ~/.pi/agent/models.json
```
```json
{
  "providers": {
    "llama.cpp": {
      "baseUrl": "http://127.0.0.1:8080/v1",
      "apiKey": "12345678",
      "api": "openai-completions",
      "models": [
        {
          "id": "Qwen3.5-9B.Q4_K_M",
          "name": "Qwen3.5-9B",
          "contextWindow": 26368
        },
        {
          "id": "Qwen2.5-Coder-7B-Instruct-Q4_K_M",
          "name": "Qwen2.5-Coder-7B",
          "contextWindow": 32768
        },
        {
          "id": "Qwythos-9B-v2-MTP-Q4_K_M",
          "name": "Qwythos-9B-v2-MTP",
          "contextWindow": 18176
        }
      ]
    }
  }
}
```
- 實測：
  - Qwen 2.5 Coder 7B 沒辦法跟 Pi Coding Agent 一起用（沒辦法做 Reasoning，只支援 Tool Calling）
  - Qwen 3.5 9B (Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF）做一些比較簡短的文件整理、規劃 web search 跟寫程式都可以。
    - 缺點：偶爾會遇到 context window 的限制.
    - 疑問：
      - Pi Coding Agent 為何沒有在用滿 context window 前執行 `/compact` 來釋放一些 context window 的空間呢？ 還是我應該照著 Pi Coding Agent 的官方文件建議，強制將 llama.cpp 的 context window 設定成 `-c 32768` 來避免這個問題？
      ```
      llama-server \
      --models-dir ~/models \
      --no-models-autoload \
      --jinja \
      --host 127.0.0.1 \
      --port 8080 \
      -ngl 999 \
      -c 32768
      ```
    - 驗證：
      - 看過 https://pi.dev/docs/latest/compaction
      > [!NOTE]
      > Auto-compaction triggers when:
      > contextTokens > contextWindow - reserveTokens
      > By default, reserveTokens is `16384` tokens
      - 這說明了為什麼 Pi Coding Agent 在 context window 用到 80% 左右就停止 response。
    - 實測強制將 llama.cpp 的 context window 設定成 `-c 32768`
      但 Pi 用 `/llama` 指令，使用 Enter 載入(load) 之後，下方 footer 仍顯示 `26K (auto)` 而非 `33K`
      ```
      0.0%/26k (auto)    (llama.cpp) Qwen3.5-9B.Q4_K_M
      ```
    - 在移除 pi models.json 的 `contextWindow` 設定後，
    ```
    0.0%/128k (auto)     (llama.cpp) Qwythos-9B-v2-MTP-Q4_K_M
    ```
```
Loaded Qwen3.5-9B.Q4_K_M

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 llama.cpp models
 http://127.0.0.1:8080

→ Qwen3.5-9B.Q4_K_M                   loaded · 33k context
```
```
0.0%/128k (auto)       (llama.cpp) Qwen3.5-9B.Q4_K_M
```