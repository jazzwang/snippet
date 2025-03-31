# CLI like Good Tape

## 2025-03-29

- https://g.co/gemini/share/2ff83e3e5713

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
如何用 Python 實作類似 Good Tape 逐字稿的 CLI 工具呢？
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

好的，以下是如何使用 Python 實作類似 Good Tape 逐字稿功能的 CLI 工具的基本步驟和程式碼範例。這個範例將使用 OpenAI 的 Whisper 模型，因為它提供了相對較好的準確性和易用性，並且有一個免費的 API 額度。

**請注意：** 使用 OpenAI Whisper API 需要您註冊 OpenAI 帳戶並獲取 API 金鑰。

**步驟 1：安裝必要的函式庫**

首先，您需要安裝 `openai` 函式庫來與 OpenAI API 互動，以及 `argparse` 來處理 CLI 參數。

```bash
pip install openai argparse
```

**步驟 2：建立 Python 腳本**

建立一個名為 `goodtape_cli.py` 的 Python 檔案，並加入以下程式碼：

```python
import argparse
import openai
import os

def transcribe_audio(audio_file_path, api_key):
    """
    使用 OpenAI Whisper 模型將音訊檔案轉錄為文字。

    Args:
        audio_file_path (str): 音訊檔案的路徑。
        api_key (str): 您的 OpenAI API 金鑰。

    Returns:
        str: 轉錄後的文字，如果發生錯誤則返回 None。
    """
    openai.api_key = api_key
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return transcript["text"]
    except Exception as e:
        print(f"轉錄錯誤：{e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="類似 Good Tape 的 CLI 逐字稿工具")
    parser.add_argument("audio_file", help="要轉錄的音訊檔案路徑")
    parser.add_argument("--api_key", help="您的 OpenAI API 金鑰 (如果未設定環境變數)")
    args = parser.parse_args()

    audio_file_path = args.audio_file
    api_key = args.api_key

    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("錯誤：請提供 OpenAI API 金鑰，可以透過 --api_key 參數或設定 OPENAI_API_KEY 環境變數。")
            return

    if not os.path.exists(audio_file_path):
        print(f"錯誤：找不到音訊檔案：{audio_file_path}")
        return

    print(f"正在轉錄：{audio_file_path}...")
    transcription = transcribe_audio(audio_file_path, api_key)

    if transcription:
        print("\n轉錄結果：")
        print(transcription)

if __name__ == "__main__":
    main()
```

**程式碼說明：**

1.  **`transcribe_audio(audio_file_path, api_key)` 函數：**
    * 接收音訊檔案路徑和 OpenAI API 金鑰作為輸入。
    * 設定 `openai.api_key`。
    * 使用 `with open(...)` 以二進制讀取模式開啟音訊檔案。
    * 呼叫 `openai.Audio.transcribe()` 函數，指定使用的模型為 `"whisper-1"` 並傳遞音訊檔案。
    * 從返回的 `transcript` 物件中提取轉錄後的文字 (`transcript["text"]`)。
    * 如果發生任何錯誤，會捕獲異常並印出錯誤訊息。

2.  **`main()` 函數：**
    * 使用 `argparse` 建立一個命令列參數解析器。
    * 定義一個必需的參數 `audio_file`，用於指定要轉錄的音訊檔案路徑。
    * 定義一個可選的參數 `--api_key`，用於直接在命令列中提供 API 金鑰。
    * 首先嘗試從命令列參數獲取 API 金鑰，如果沒有提供，則嘗試從名為 `OPENAI_API_KEY` 的環境變數中獲取。
    * 檢查是否提供了 API 金鑰，如果沒有則印出錯誤訊息並退出。
    * 檢查提供的音訊檔案是否存在，如果不存在則印出錯誤訊息並退出。
    * 印出正在轉錄的訊息。
    * 呼叫 `transcribe_audio()` 函數進行轉錄。
    * 如果轉錄成功，則印出 "轉錄結果：" 和轉錄後的文字。

3.  **`if __name__ == "__main__":` 區塊：**
    * 確保只有在直接執行腳本時才呼叫 `main()` 函數。

**步驟 3：設定 OpenAI API 金鑰**

您需要設定您的 OpenAI API 金鑰。您可以選擇以下兩種方式之一：

* **透過環境變數：** 在您的終端機中設定一個名為 `OPENAI_API_KEY` 的環境變數，並將其值設定為您的 API 金鑰。
    * 在 Linux/macOS 中：
        ```bash
        export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
        ```
    * 在 Windows 中：
        ```bash
        set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
        ```
* **透過命令列參數：** 在執行腳本時使用 `--api_key` 參數提供您的 API 金鑰。

**步驟 4：執行 CLI 工具**

開啟您的終端機，導航到儲存 `goodtape_cli.py` 檔案的目錄，然後執行以下命令：

```bash
python goodtape_cli.py your_audio_file.mp3
```

或者，如果您選擇透過命令列參數提供 API 金鑰：

```bash
python goodtape_cli.py your_audio_file.mp3 --api_key YOUR_OPENAI_API_KEY
```

將 `your_audio_file.mp3` 替換為您要轉錄的實際音訊檔案路徑。

**進一步的改進和功能：**

* **支援更多音訊格式：** OpenAI Whisper API 支援多種音訊格式（例如：mp3, mp4, mpeg, mpga, m4a, wav, webm）。您可以根據需求調整。
* **輸出到檔案：** 增加一個選項將轉錄結果儲存到檔案（例如：`.txt` 檔案）。
* **處理較長的音訊：** 對於非常長的音訊檔案，您可能需要將其分割成較小的片段進行轉錄，然後再將結果合併。
* **進階的 Whisper 模型參數：** OpenAI API 允許您使用更多參數來控制轉錄過程，例如 `language`、`prompt` 等。您可以將這些參數作為 CLI 選項公開。
* **錯誤處理和重試機制：** 實作更完善的錯誤處理機制，例如在 API 請求失敗時進行重試。
* **進度指示器：** 對於較大的音訊檔案，可以加入進度指示器來顯示轉錄進度。
* **使用本地 Whisper 模型：** 如果您希望完全離線使用，可以考慮使用 `whisper` Python 函式庫的本地模型。這可能需要更多的設定，並且準確性可能略有不同。您可以安裝 `whisper` 函式庫：`pip install -U openai-whisper`，然後在程式碼中直接載入和使用模型。

這個基本的 CLI 工具提供了一個起點，您可以根據自己的需求進行擴展和改進。記得查看 OpenAI Whisper API 的官方文件以了解更多進階功能和限制。

</td></tr></table>