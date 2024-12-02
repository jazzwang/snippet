# Google Cloud Translate API

- 緣起：
  - 在測試了 Gemini API 以後，覺得「翻譯」這部份應該用 Google Translate API 就可以了。
  - 其次，Chrome 也正在積極開發 Local (Edge) 佈署 Gemini Nano，也包含了 translate 跟 summary 的 Local API
- 待確認：
  - Google Cloud Translate API 的 Pricing
    - 因為 https://immersivetranslate.com/ 這個瀏覽器延伸套件預設用 Bing 跟 Google Translate 來免費翻譯，因此或許用 RESTful API 跟 Python Client Library 呼叫的 Pricing 也有差異。
  - 先前有感覺 OpenAI LLM 模型翻譯的結果與 Google Translate 品質上有落差。當然目前 Google Translate 跟 Gemini 1.5 Flash 生成的翻譯到底是否有差異，仍有待比較與確認。

## 2024-11-26

- ( 2024-11-26 08:47:03 )
- 參考：
  - https://codelabs.developers.google.com/codelabs/cloud-translation-python3
- 環境：
  - Github Codespace
  - 須參考 `google-cloud-texttospeech` 的實驗紀錄，生成 `google-cloud-translate` 的 JSON 金鑰。
- 步驟：
- 開啟 Github Codespace
```bash
jazzw@JazzBook:~/git/snippet$ gh cs code -R jazzwang/snippet
@jazzwang ➜ /workspaces/snippet (master) $ cd python/
@jazzwang ➜ /workspaces/snippet/python (master) $ mkdir google-cloud-translate
@jazzwang ➜ /workspaces/snippet/python (master) $ cd google-cloud-translate
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ code MEMO.md
```
- 在 Google CloudShell 中產生所需的金鑰 - https://shell.cloud.google.com/?show=terminal
- 用 `gcloud iam service-accounts keys create` 來產生 service account 的 JWT JSON 檔。
```bash
jazzwang_tw@cloudshell:~$ gcloud config set project "hadoop-labs"
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud iam service-accounts create trans-lab
jazzwang_tw@cloudshell:~ (hadoop-labs)$ export PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud iam service-accounts keys create trans-lab.json --iam-account trans-lab@$PROJECT_ID.iam.gserviceaccount.com
jazzwang_tw@cloudshell:~ (hadoop-labs)$ cloudshell download trans-lab.json
```
- 複製金鑰到 Github Codespace
```bash
jazzw@JazzBook:~/Downloads$ gh cs cp trans-lab.json 'remote:/tmp' -R jazzwang/snippet
trans-lab.json                                                                                                            100% 2345    15.0KB/s   00:00
```
```bash
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ cp /tmp/trans-lab.json .
```
- 安裝套件
```bash
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ pip3 install google-cloud-translate
```
- 實驗執行範例
```bash
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ export GOOGLE_APPLICATION_CREDENTIALS=trans-lab.json 
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ ipython3
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from google.cloud import translate
   ...: 
   ...: def print_supported_languages(display_language_code: str):
   ...:     client = translate.TranslationServiceClient()
   ...: 
   ...:     response = client.get_supported_languages(
   ...:         parent=PARENT,
   ...:         display_language_code=display_language_code,
   ...:     )
   ...: 
   ...:     languages = response.languages
   ...:     print(f" Languages: {len(languages)} ".center(60, "-"))
   ...:     for language in languages:
   ...:         language_code = language.language_code
   ...:         display_name = language.display_name
   ...:         print(f"{language_code:10}{display_name}")
   ...: 

In [2]: def translate_text(text: str, target_language_code: str) -> translate.Translation:
   ...:     client = translate.TranslationServiceClient()
   ...: 
   ...:     response = client.translate_text(
   ...:         parent=PARENT,
   ...:         contents=[text],
   ...:         target_language_code=target_language_code,
   ...:     )
   ...: 
   ...:     return response.translations[0]
   ...: 
In [3]: text = "Hello World!"
   ...: target_languages = ["tr", "de", "es", "it", "el", "zh", "ja", "ko"]
   ...: 
   ...: print(f" {text} ".center(50, "-"))
   ...: for target_language in target_languages:
   ...:     translation = translate_text(text, target_language)
   ...:     source_language = translation.detected_language_code
   ...:     translated_text = translation.translated_text
   ...:     print(f"{source_language} → {target_language} : {translated_text}")
   ...: 
------------------ Hello World! ------------------
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
```
- 遇到一些 Error，試著排查後發現忘了 enable Google Translate API
```bash
PermissionDenied: 403 Cloud Translation API has not been used in project 69xxxxxxxx56 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=69xxxxxxxx56 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry. [links {
  description: "Google developers console API activation"
  url: "https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=69xxxxxxxx56"
}
, reason: "SERVICE_DISABLED"
domain: "googleapis.com"
metadata {
  key: "service"
  value: "translate.googleapis.com"
}
metadata {
  key: "consumer"
  value: "projects/69xxxxxxxx56"
}
]
```
- 用網頁或在 GCP CloudShell 下指令啟用 API
```bash
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud services enable translate.googleapis.com
```
- 回到 Github Codespace，再試一次
```bash
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ export GOOGLE_APPLICATION_CREDENTIALS=trans-lab.json 
@jazzwang ➜ /workspaces/snippet/python/google-cloud-translate (master) $ ipython3
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from google.cloud import translate
   ...: 
   ...: def print_supported_languages(display_language_code: str):
   ...:     client = translate.TranslationServiceClient()
   ...: 
   ...:     response = client.get_supported_languages(
   ...:         display_language_code=display_language_code,
   ...:     )
   ...: 
   ...:     languages = response.languages
   ...:     print(f" Languages: {len(languages)} ".center(60, "-"))
   ...:     for language in languages:
   ...:         language_code = language.language_code
   ...:         display_name = language.display_name
   ...:         print(f"{language_code:10}{display_name}")
   ...: 

In [2]: print_supported_languages("en")
---------------------------------------------------------------------------
InvalidArgument                           Traceback (most recent call last)
Cell In[2], line 1
----> 1 print_supported_languages("en")

... 略 ...

InvalidArgument: 400 Empty 'parent'.; Empty resource name.;  Resource type: location

In [3]: PARENT = f"projects/hadoop-labs"

In [4]: def print_supported_languages(display_language_code: str):
   ...:     client = translate.TranslationServiceClient()
   ...: 
   ...:     response = client.get_supported_languages(
   ...:         parent=PARENT,
   ...:         display_language_code=display_language_code,
   ...:     )
   ...: 
   ...:     languages = response.languages
   ...:     print(f" Languages: {len(languages)} ".center(60, "-"))
   ...:     for language in languages:
   ...:         language_code = language.language_code
   ...:         display_name = language.display_name
   ...:         print(f"{language_code:10}{display_name}")
   ...: 

In [5]: print_supported_languages("en")
---------------------------------------------------------------------------
PermissionDenied                          Traceback (most recent call last)
Cell In[5], line 1
----> 1 print_supported_languages("en")

... 略 ...

PermissionDenied: 403 Cloud IAM permission 'cloudtranslate.generalModels.get' denied. 

In [6]: exit()
```
- 看樣子 Google Translate API 可能要額外的 IAM 設定（畢竟我剛剛順序上不正確，先 create service account 才 enable API）
- ( 2024-11-26 09:27:53 )