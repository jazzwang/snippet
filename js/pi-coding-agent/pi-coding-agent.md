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