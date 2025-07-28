# DEVELOPMENT NOTES

## 2024-11-21

- ( 2024-11-21 21:55:08 )
- 緣起：
  - 想試試看如果在非 Google Cloud Shell 的環境，該如何使用 Google Cloud API
  - 想產生小孩要用的 Spelling Bee "Say - Spell - Say" 的單字音檔 MP3
- 參考：
  - https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#5
  - https://cloud.google.com/text-to-speech/docs/libraries#use
- 整合 codelabs 跟 text-to-speech 文件的範例，大致上得到幾個結論：
  - 如果要在非 Google Cloud 的環境上使用，必須安裝 Google Cloud Toolkit 才能做認證（或許需要某個 service json 檔來放在 local 當完成身份認證的參考）
    - https://cloud.google.com/text-to-speech/docs/libraries#authentication 提到 Production 環境要設置 `Application Default Credentials (ADC)`
      - https://cloud.google.com/docs/authentication/application-default-credentials
      - `GOOGLE_APPLICATION_CREDENTIALS` environment variable
      - 參考：https://joehuang-pop.github.io/2020/06/25/Google-API-Google-%E8%AA%9E%E9%9F%B3%E7%94%9F%E6%88%90-API-%E5%AF%A6%E4%BD%9C-Google-Text-to-Speech/#Step-2-Create-a-service-account
      - 提到用 `gcloud iam service-accounts keys create` 來產生 service account 的 JWT JSON 檔。
      ```bash
      ~$ gcloud iam service-accounts create tts-qwiklab
      ~$ export PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
      ~$ gcloud iam service-accounts keys create tts-qwiklab.json --iam-account tts-qwiklab@$PROJECT_ID.iam.gserviceaccount.com
      ~$ export GOOGLE_APPLICATION_CREDENTIALS=tts-qwiklab.json
      ```
      - 備註：看截圖跟命名，這是在 qwiklab (cloudskillsboost) 上實作的練習。
  - 取決於 `AudioConfig` 使用那一種編碼 `AudioEncoding`
    - WAV 格式：`tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)`
    - MP3 格式：`tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)`
- 實驗：
  - 先在 Github Codespace 上裝 `google-cloud-texttospeech`
```bash
jazzw@JazzBook:~/git/snippet/python$ mkdir google-cloud-texttospeech
jazzw@JazzBook:~/git/snippet/python$ cd google-cloud-texttospeech/
jazzw@JazzBook:~/git/snippet/python/google-cloud-texttospeech$ gh cs ssh
? Choose codespace: jazzwang/snippet (master*): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Thu Nov 21 05:50:00 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp
@jazzwang ➜ /tmp $ pip install google-cloud-texttospeech
Downloading google_cloud_texttospeech-2.21.1-py2.py3-none-any.whl (170 kB)
Installing collected packages: google-cloud-texttospeech
Successfully installed google-cloud-texttospeech-2.21.1
@jazzwang ➜ /tmp $ ipython
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import google.cloud.texttospeech as tts

In [2]: def text_to_mp3(voice_name: str, text: str):
   ...:     language_code = "-".join(voice_name.split("-")[:2])
   ...:     text_input = tts.SynthesisInput(text=text)
   ...:     voice_params = tts.VoiceSelectionParams(
   ...:         language_code=language_code, name=voice_name
   ...:     )
   ...:     audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)
   ...:     client = tts.TextToSpeechClient()
   ...:     response = client.synthesize_speech(
   ...:         input=text_input,
   ...:         voice=voice_params,
   ...:         audio_config=audio_config,
   ...:     )
   ...:     filename = f"{voice_name}.mp3"
   ...:     with open(filename, "wb") as out:
   ...:         out.write(response.audio_content)
   ...:         print(f'Generated speech saved to "{filename}"')
   ...:

In [3]: text_to_mp3("en-US-Studio-O", "shoemaker s-h-o-e-m-a-k-e-r shoemaker")
---------------------------------------------------------------------------
DefaultCredentialsError                   Traceback (most recent call last)
Cell In[4], line 1
----> 1 text_to_mp3("en-US-Studio-O", "shoemaker s-h-o-e-m-a-k-e-r shoemaker")

Cell In[3], line 8, in text_to_mp3(voice_name, text)
      4 voice_params = tts.VoiceSelectionParams(
      5     language_code=language_code, name=voice_name
      6 )
      7 audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)
----> 8 client = tts.TextToSpeechClient()
      9 response = client.synthesize_speech(
     10     input=text_input,
     11     voice=voice_params,
     12     audio_config=audio_config,
     13 )
     14 filename = f"{voice_name}.mp3"

File /usr/local/python/3.10.13/lib/python3.10/site-packages/google/cloud/texttospeech_v1/services/text_to_speech/client.py:635, in TextToSpeechClient.__init__(self, credentials, transport, client_options, client_info)
    627 transport_init: Union[
    628     Type[TextToSpeechTransport], Callable[..., TextToSpeechTransport]
    629 ] = (
   (...)
    632     else cast(Callable[..., TextToSpeechTransport], transport)
    633 )
    634 # initialize with the provided callable or the passed in class
--> 635 self._transport = transport_init(
    636     credentials=credentials,
    637     credentials_file=self._client_options.credentials_file,
    638     host=self._api_endpoint,
    639     scopes=self._client_options.scopes,
    640     client_cert_source_for_mtls=self._client_cert_source,
    641     quota_project_id=self._client_options.quota_project_id,
    642     client_info=client_info,
    643     always_use_jwt_access=True,
    644     api_audience=self._client_options.api_audience,
    645 )

File /usr/local/python/3.10.13/lib/python3.10/site-packages/google/cloud/texttospeech_v1/services/text_to_speech/transports/grpc.py:153, in TextToSpeechGrpcTransport.__init__(self, host, credentials, credentials_file, scopes, channel, api_mtls_endpoint, client_cert_source, ssl_channel_credentials, client_cert_source_for_mtls, quota_project_id, client_info, always_use_jwt_access, api_audience)
    148             self._ssl_channel_credentials = grpc.ssl_channel_credentials(
    149                 certificate_chain=cert, private_key=key
    150             )
    152 # The base transport sets the host, credentials and scopes
--> 153 super().__init__(
    154     host=host,
    155     credentials=credentials,
    156     credentials_file=credentials_file,
    157     scopes=scopes,
    158     quota_project_id=quota_project_id,
    159     client_info=client_info,
    160     always_use_jwt_access=always_use_jwt_access,
    161     api_audience=api_audience,
    162 )
    164 if not self._grpc_channel:
    165     # initialize with the provided callable or the default channel
    166     channel_init = channel or type(self).create_channel

File /usr/local/python/3.10.13/lib/python3.10/site-packages/google/cloud/texttospeech_v1/services/text_to_speech/transports/base.py:100, in TextToSpeechTransport.__init__(self, host, credentials, credentials_file, scopes, quota_project_id, client_info, always_use_jwt_access, api_audience, **kwargs)
     96     credentials, _ = google.auth.load_credentials_from_file(
     97         credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
     98     )
     99 elif credentials is None and not self._ignore_credentials:
--> 100     credentials, _ = google.auth.default(
    101         **scopes_kwargs, quota_project_id=quota_project_id
    102     )
    103     # Don't apply audience if the credentials file passed from user.
    104     if hasattr(credentials, "with_gdch_audience"):

File /usr/local/python/3.10.13/lib/python3.10/site-packages/google/auth/_default.py:697, in default(scopes, request, quota_project_id, default_scopes)
    689             _LOGGER.warning(
    690                 "No project ID could be determined. Consider running "
    691                 "`gcloud config set project` or setting the %s "
    692                 "environment variable",
    693                 environment_vars.PROJECT,
    694             )
    695         return credentials, effective_project_id
--> 697 raise exceptions.DefaultCredentialsError(_CLOUD_SDK_MISSING_CREDENTIALS)

DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
```
- 所以還是需要設定 ADC。先把程式碼另存成 text2mp3.py
```bash
In [4]: %save text2mp3.py
The following commands were written to file `text2mp3.py`:
import google.cloud.texttospeech as tts
def text_to_mp3(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)
    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )
    filename = f"{voice_name}.mp3"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
text_to_mp3("en-US-Studio-O", "shoemaker s-h-o-e-m-a-k-e-r shoemaker")

In [5]: quit()
```
- ( 2024-11-21 22:42:10 )
- 把範例程式加到
```bash
@jazzwang ➜ /tmp $ mv text2mp3.py /workspaces/snippet/python/google-cloud-texttospeech/
@jazzwang ➜ /tmp $ popd
/workspaces/snippet/python/google-cloud-texttospeech
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ git add text2mp3.py
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ git commit -a -m "feat: [py][google-cloud-texttospeech] example text-to-mp3 scri
pt using Google Cloud Text-to-Speech Client Library"
[master 3aef24b] feat: [py][google-cloud-texttospeech] example text-to-mp3 script using Google Cloud Text-to-Speech Client Library
 1 file changed, 22 insertions(+)
 create mode 100644 python/google-cloud-texttospeech/text2mp3.py
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ git push
```
- ( 2024-11-21 22:45:49 )
- 我們先來處理 ADC 的 JWT 檔。首先回到 Google Cloud Shell，登入 PROJECT_ID。
```bash
jazzwang_tw@cloudshell:~$ gcloud config set project hadoop-labs
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud iam service-accounts create tts-labs
jazzwang_tw@cloudshell:~ (hadoop-labs)$ export PROJECT_ID=$(gcloud config get-value project 2> /dev/null)
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud iam service-accounts keys create tts-labs.json --iam-account tts-labs@$PROJECT_ID.iam.gserviceaccount.com
jazzwang_tw@cloudshell:~ (hadoop-labs)$ cloudshell download tts-labs.json
```
- 讓我們把下載下來的 `tts-labs.json` 上傳到 Github Codespace
```bash
jazzw@JazzBook:~/Downloads$ gh cs cp tts-labs.json 'remote:/workspaces/snippet/'
? Choose codespace: jazzwang/snippet (master*): snippet
tts-labs.json                                                                                                             100% 2343    15.7KB/s   00:00
jazzw@JazzBook:~/Downloads$ gh cs ssh -R jazzwang/snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Thu Nov 21 13:54:04 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $ cd python/google-cloud-texttospeech/
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ mv /workspaces/snippet/tts-labs.json .
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ export GOOGLE_APPLICATION_CREDENTIALS=tts-labs.json
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ python3 text2mp3.py
Generated speech saved to "en-US-Studio-O.mp3"
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ mv en-US-Studio-O.mp3 /tmp/
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ exit
logout
Connection to localhost closed.
```
- 把生成的 MP3 下載來聽看看。
```
jazzw@JazzBook:~/Downloads$ gh cs cp 'remote:/tmp/en-US-Studio-O.mp3' .
? Choose codespace: jazzwang/snippet (master*): snippet
en-US-Studio-O.mp3                                                                                                        100%   26KB  57.5KB/s   00:00
jazzw@JazzBook:~/Downloads$ open .
```
- 結果是可以，只是聲音語速有點太快了。再來找一下怎麼調慢。接著就是把這個程式變成吃參數 '語系', '文字', '輸出檔名'

## 2024-11-22

- ( 2024-11-22 23:34:25 )
- 改成可以讀檔案。
- 語系 跟 [voice](https://cloud.google.com/text-to-speech/docs/voices) / [voice type](https://cloud.google.com/text-to-speech/docs/voice-types#journey_voices) 固定：
  - en-US-Standard-C (機器感比較重一點)
  - en-US-Standard-E (機器感比較重一點)
  - en-US-Studio-O (女生，比較流暢一點)
  - en-US-Studio-Q (男生，比較流暢一點)
- 輸出檔名等於 "單字.mp3"

## 2024-11-25

- ( 2024-11-25 22:15:52 )
- 實驗產生空白的 15 秒 MP3
- 根據 [Gemini 的建議](https://g.co/gemini/share/a1081dfe2622)，可以用 [python-soundfile](https://github.com/bastibe/python-soundfile)
- 先用 ipython 測試一下：
```bash
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ pip3 install soundfile
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ ipython3
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import soundfile as sf
   ...:
   ...: # Define parameters for the blank audio
   ...: duration = 15  # seconds
   ...: samplerate = 44100  # samples per second
   ...: channels = 2  # stereo
   ...:
   ...: # Create an array of zeros for the audio data
   ...: audio_data = np.zeros((samplerate * duration, channels))
   ...:
   ...: # Write the audio data to a file
   ...: sf.write('blank_audio.mp3', audio_data, samplerate)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 9
      6 channels = 2  # stereo
      8 # Create an array of zeros for the audio data
----> 9 audio_data = np.zeros((samplerate * duration, channels))
     11 # Write the audio data to a file
     12 sf.write('blank_audio.mp3', audio_data, samplerate)

NameError: name 'np' is not defined
```
- 查了一下 `np.zeros` 結果是 `numpy`
```python
In [2]: import soundfile as sf
   ...: import numpy as np
   ...:
   ...: # Define parameters for the blank audio
   ...: duration = 15  # seconds
   ...: samplerate = 44100  # samples per second
   ...: channels = 2  # stereo
   ...:
   ...: # Create an array of zeros for the audio data
   ...: audio_data = np.zeros((samplerate * duration, channels))
   ...:
   ...: # Write the audio data to a file
   ...: sf.write('blank_audio.mp3', audio_data, samplerate)
```
- 將 Python 程式從 `spelling-bee.py` 更名為 `spelling_bee.py`
- 這樣就可以在 `ipython` 裡 `import spelling_bee` 並且呼叫定義的函數了!!
- 用這種方法，就可以拿來測試合併空白音檔與單純只念單字三次的音檔。
```python
@jazzwang ➜ /workspaces/snippet/python/google-cloud-texttospeech (master) $ ipython3
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import spelling_bee

In [2]: spelling_bee.blank_mp3(10)

In [3]: spelling_bee.question("test")
Generated speech saved to "_test.mp3"
```

## 2025-07-24

### from Gemini 2.5 Flash

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
is there a easy way to put a long text and create speech using Google Cloud text-to-speech? any Web UI that I don't need to write code and use API?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You're looking for a way to use Google Cloud Text-to-Speech (TTS) for long texts without needing to write code or interact directly with APIs, ideally through a web UI.

While Google Cloud Text-to-Speech is primarily designed for developers to integrate into applications via APIs, there isn't an official, public-facing web UI directly from Google Cloud that allows you to simply paste long text and generate speech for free without any setup.

However, here's a breakdown of options and considerations:

**1. Google Cloud Text-to-Speech Demo (Limited)**

* Google Cloud does offer a small demo on its Text-to-Speech product page. You can type or paste short text segments (usually limited in character count) and hear the synthesized speech. This is great for testing voices and basic functionality, but not for long texts or saving the output.

**2. Third-Party Web UIs/Tools that Integrate with Google Cloud TTS**

* Many third-party services and platforms leverage Google Cloud Text-to-Speech (and other TTS engines) to provide a user-friendly web interface. These are often designed for content creators, marketers, and individuals who want to generate audio from text without coding.
* **How they work:** You upload or paste your text, choose a voice (often from Google's extensive library), and the service handles the API calls to Google Cloud on the backend, then provides you with the audio file.
* **Examples of such services (you'll need to search for current ones as they can change):** Look for "text-to-speech online converter," "AI voice generator," or "audio from text" tools. Many of these offer free tiers with limitations (e.g., character limits, fewer voices) and paid plans for more features and longer content.
* **Pros:** Easy to use, no coding required, often offer additional features like background music, different speaker options, and more.
* **Cons:** You're relying on a third-party service, so pricing, privacy, and long-term availability depend on that provider.

**3. Setting up your own basic Web UI (Requires some effort, but no complex coding)**

If you're willing to do a *little* initial setup, you could potentially create a very simple local solution:

* **Google Cloud Console and Service Account:** You would need a Google Cloud account, enable the Text-to-Speech API, and create a Service Account with the appropriate permissions. This gives you a JSON key file.
* **Simple Script (e.g., Python):** While you said "no code," a very basic Python script could be written to take text from a file (or even a simple HTML input if you run a local web server) and send it to the Google Cloud TTS API using your service account key. The script would then save the audio output as an MP3.
    * This is not a "web UI" in the traditional sense, but it would avoid direct API calls or complex programming each time you want to convert text. You'd essentially have a local tool.
* **Tools like Make.com (formerly Integromat) or Zapier:** These "no-code" automation platforms can connect various services. You could potentially set up a workflow where, for example, you upload a text file to a cloud storage service, and it triggers a Google Cloud TTS action to convert it to audio, then saves the audio back to storage. This involves some setup but requires no traditional coding.

**Key considerations for long texts:**

* **Character Limits:** The Google Cloud Text-to-Speech API has character limits per request. For very long texts (e.g., entire books), you'll need to break them into smaller chunks and synthesize each chunk separately. Most robust third-party UIs will handle this automatically.
* **Cost:** Google Cloud Text-to-Speech is a paid service after a free tier. The cost is based on the number of characters processed. Be mindful of this when converting very long texts.

**In summary:**

For a truly "easy way" with a web UI and no coding, your best bet is to explore reputable **third-party web-based text-to-speech converters** that integrate with Google Cloud TTS. These services abstract away the API complexities and provide a user-friendly experience for generating audio from long texts. Just be sure to check their pricing, features, and terms of service.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me reference url links of Third-Party Web UIs/Tools that Integrate with Google Cloud TTS?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You're looking for third-party web UIs that specifically integrate with Google Cloud Text-to-Speech (TTS) for converting long texts, without needing to write code.

It's important to note that the landscape of online tools changes frequently. While I can't guarantee every single one will be the perfect fit or perpetually free, here's a general approach and some types of tools to look for, along with examples that often leverage Google's underlying technology:

**General Advice for Finding and Using These Tools:**

1.  **Search Terms:** Use terms like:
    * "online text to speech Google Cloud"
    * "AI voice generator Google TTS"
    * "long text to speech converter free" (then check if they use Google's voices)
    * "text to audio converter with Google voices"
2.  **Look for "Powered by Google" or Similar:** Many tools will proudly state if they use Google's (or Amazon's, IBM's, Microsoft's, etc.) powerful AI voices.
3.  **Check Free Tiers and Limitations:** Most offer a free tier with character limits or limited voices. For "long texts," you'll likely hit these limits quickly and might need to consider a paid plan.
4.  **Read Reviews:** See what other users say about quality, ease of use, and customer support.
5.  **Data Privacy:** If you're using sensitive information, review their privacy policies.

**Types of Tools and Potential Examples (Always Verify Current Features and Integrations):**

* **General Purpose Online TTS Converters:** Many websites offer a simple text box where you can paste text, choose a voice, and download the audio. Some of these use Google's voices as an option.
    * **Speechify:** (speechify.com) - This is a popular text-to-speech tool that often highlights its use of advanced AI voices, including those similar to Google's. They offer a Chrome extension and mobile apps, and are designed for reading long-form content.
    * **PlayHT:** (play.ht) - Focuses on realistic AI voices for various content creation needs. They explicitly mention using different AI models, which can include Google's.
    * **Murf.ai:** (murf.ai) - Another prominent AI voice generator that offers a wide range of voices and customization options. While they develop their own AI voices, they are in the same market space and offer similar functionality.
    * **Listnr.ai:** (listnr.ai) - A platform for converting text to podcasts, audiobooks, and voiceovers, often leveraging various advanced TTS engines.

* **Content Creation Platforms with TTS Integration:** Some platforms designed for creating videos, podcasts, or e-learning content will have built-in TTS features that might use Google Cloud TTS on the backend.
    * Look for video editors or podcast creation tools that offer text-to-speech functionality.

* **No-Code Automation Platforms (for more advanced "no-code" workflows):** If you're willing to set up a slightly more involved process for recurring long texts, platforms like Zapier or Make (formerly Integromat) can connect Google Cloud TTS with other services. This isn't a simple "web UI" for a one-off conversion, but it can automate workflows if you regularly need to convert text from a specific source (e.g., a Google Doc, an RSS feed).
    * **Latenode:** (latenode.com) - As seen in search results, they specifically mention integrating with Google Cloud Text-to-Speech for automated workflows, which could involve non-coding approaches.

**Important Note on Google's Own Offerings:**

* **Google Cloud Text-to-Speech Demo:** As mentioned previously, Google provides a small demo directly on their Text-to-Speech product page: [https://cloud.google.com/text-to-speech](https://cloud.google.com/text-to-speech)
    * This is very limited in character count and doesn't allow saving the audio, but it lets you quickly sample their voices.
* **Google AI Studio (for Gemini API with TTS):** More recently, Google has integrated TTS capabilities into its Gemini API, and you can test this in Google AI Studio. While it's primarily for developers, AI Studio offers a web interface to experiment with the Gemini models, including their text-to-speech capabilities. This is also often limited for direct long text conversion without further integration. You can find more about it here: [https://ai.google.dev/gemini-api/docs/speech-generation](https://ai.google.dev/gemini-api/docs/speech-generation)

Always visit the specific website to understand their current features, pricing, and how they implement text-to-speech, as these details can change.
</td></tr></table>

### from Perplexity

- https://www.perplexity.ai/search/could-you-give-me-reference-ur-.qX_y_svR1GO8anRmZSVbg

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me reference url links of Third-Party Web UIs/Tools that Integrate with Google Cloud TTS?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here are some reference URLs for third-party web UIs/tools that integrate with Google Cloud Text-to-Speech (TTS):

1. **Latenode** – A low-code/no-code integration platform that connects Google Cloud Text-to-Speech with other services and code for automation and workflow creation.  
   URL: https://latenode.com/integrations/google-drive/google-cloud-text-to-speech  
   URL: https://latenode.com/integrations/code/google-cloud-text-to-speech

2. **Genesys Cloud** – A cloud contact center platform that provides integration with Google Cloud TTS for speech synthesis in customer interactions. Guidance on activation and configuration available.  
   URL: https://help.mypurecloud.com/articles/activate-and-configure-the-google-tts-integration/

3. **LiveKit** – Offers a Google Cloud TTS integration as part of its voice AI application framework, enabling realistic text-to-speech voice generation in applications.  
   URL: https://docs.livekit.io/agents/integrations/tts/google/

4. **UiPath Integration Service** – Provides a Google Text-to-Speech connector to automate processes involving speech synthesis using Google Cloud TTS.  
   URL: https://docs.uipath.com/integration-service/automation-suite/2024.10/user-guide/uipath-google-texttospeech

5. Additionally, for technical developers interested in building their own web applications with Google Cloud TTS, there is a tutorial video demonstrating how to integrate it with Node.js and React:  
   URL: https://www.youtube.com/watch?v=jOrqR6FK-_M

These links point to platforms and tools that facilitate or demonstrate integration with Google Cloud Text-to-Speech, offering web UIs or developer-friendly workflows to leverage Google's TTS capabilities.

[1] https://latenode.com/integrations/google-drive/google-cloud-text-to-speech
[2] https://help.mypurecloud.com/articles/activate-and-configure-the-google-tts-integration/
[3] https://latenode.com/integrations/code/google-cloud-text-to-speech
[4] https://www.youtube.com/watch?v=jOrqR6FK-_M
[5] https://cloud.google.com/text-to-speech/docs/libraries
[6] https://docs.livekit.io/agents/integrations/tts/google/
[7] https://docs.uipath.com/integration-service/automation-suite/2024.10/user-guide/uipath-google-texttospeech
[8] https://cloud.google.com/text-to-speech/docs/reference/rest
[9] https://cloud.google.com/translate
[10] https://stackoverflow.com/questions/35002003/how-to-use-google-translate-tts-with-the-new-v2-api
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
is there a easy way to put a long text and create speech using Google Cloud text-to-speech? any Web UI that I don't need to write code and use API?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
**Easy Ways to Use Google Cloud Text-to-Speech Without Coding**

There are convenient ways to use Google Cloud Text-to-Speech (TTS) for generating speech from long text, without manually writing code or calling APIs. Most “no code” solutions involve third-party platforms or web UIs that connect to Google Cloud's TTS service, letting you simply paste in your text and generate speech.

**Web UIs & Tools for Non-Developers**

1. **Online Integration Platforms with Google TTS**
Platforms like **Latenode** let you connect Google Cloud TTS to a no-code web interface. You can often set up a workflow where you paste or upload your text and receive audio output.

- Example: Latenode Google Cloud TTS Integration  
  - You can use Latenode to create a text-to-speech workflow with a simple UI and no programming[1].

2. **Text-to-Speech Marketplace Apps**

- **Google Workspace Marketplace** features AI voice generator apps, some of which integrate Google Cloud TTS. These typically offer a UI for pasting large text blocks, selecting the voice, and downloading the audio.  
  - Example: “Text to Speech - AI Voice Generator” app[2].

3. **Demo and Playground Pages**
- **Google Cloud Official Demo Page:**  
  Google’s own [Text-to-Speech demo page](https://cloud.google.com/text-to-speech) provides a quick way to paste short-to-medium text and preview voices, but it has limits on input length and isn’t intended for bulk production[1].
- **Third-Party Web Tools:**  
  Sites like PlayHT and other TTS services sometimes let you choose Google Cloud as the voice engine, accept sizable text input, and produce speech files—all from a browser without any coding[3].

**Limitations**

- **Text Length:**  
  Web demo interfaces often have limits on how much text you can paste per session (e.g., 5,000 characters on the official Google demo; longer texts may require chunking or batch processing[4]).
- **Advanced Features:**  
  For extremely long-form (multi-page) text, some platforms may still require you to authenticate with a Google account and set up minimal configuration, especially if generating many files or using premium voices.

**Steps to Get Started**

1. Visit a web UI like Latenode or a Google Workspace Marketplace text-to-speech app.
2. Paste your text into the provided field.
3. Select the language, voice, and output format.
4. Generate and download your audio—no coding or API call necessary.

**Notable Examples**

| Tool/App                               | Need to Write Code? | Supports Long Text? | Quick Setup?     |
|-----------------------------------------|---------------------|---------------------|------------------|
| Latenode                               | No                  | Yes                 | Yes[1]           |
| Google Workspace TTS Marketplace apps   | No                  | Medium-Long         | Yes[2]          |
| Google Cloud Demo Page                  | No                  | Short-Medium        | Yes[1][4]       |
| PlayHT (Google TTS Option)              | No                  | Medium-Long         | Yes[3]          |

**Key Takeaway**

You can generate speech from long text using Google Cloud TTS without writing code by leveraging web UIs and online integrator platforms. For the most seamless experience and longest text limits, third-party tools like Latenode and select marketplace apps offer user-friendly interfaces with support for Google’s TTS service[1][2][3].

---
[1]: https://latenode.com/integrations/google-drive/google-cloud-text-to-speech  
[2]: https://workspace.google.com/marketplace/app/text_to_speech_ai_voice_generator/743993646804  
[3]: https://play.ht/blog/ai-apps/google-text-to-speech/  
[4]: https://www.googlecloudcommunity.com/gc/AI-ML/Google-TTS-can-t-convert-text-longer-than-500-600-characters/m-p/517771

[1] https://cloud.google.com/text-to-speech
[2] https://workspace.google.com/marketplace/app/text_to_speech_ai_voice_generator/743993646804
[3] https://play.ht/blog/ai-apps/google-text-to-speech/
[4] https://www.googlecloudcommunity.com/gc/AI-ML/Google-TTS-can-t-convert-text-longer-than-500-600-characters/m-p/517771
[5] https://cloud.google.com/speech-to-text
[6] https://www.youtube.com/watch?v=x6ZMVcsSoTM
[7] https://www.youtube.com/watch?v=jOrqR6FK-_M
[8] https://developers.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1
[9] https://murf.ai/blog/how-to-use-text-to-speech-on-google-cloud
[10] https://stackoverflow.com/questions/76725897/google-cloud-tts-synthesizelongaudio-no-file-created
[11] https://github.com/GoogleCloudPlatform/text-to-speech-epg-demo
[12] https://cloud.google.com/text-to-speech/docs/reference/rest
[13] https://cloud.google.com/text-to-speech/docs/create-audio-text-long-audio-synthesis
[14] https://www.reddit.com/r/googlecloud/comments/9x4y6t/total_noob_want_to_use_the_speechtotext_api_and/
[15] https://www.googlecloudcommunity.com/gc/AI-ML/Google-TTS-Long-form-synthesis-working-sporadically/m-p/894253
[16] https://www.googlecloudcommunity.com/gc/AI-ML/Major-Bug-for-Text-to-Speech-Still-Not-Fixed/m-p/896767
[17] https://developers.google.com/text-to-speech/docs/reference/rpc
[18] https://community.openhab.org/t/text-based-configuration-of-google-cloud-text-to-speech-settings/132174
[19] https://chromewebstore.google.com/detail/text-to-speech-tts/cpnomhnclohkhnikegipapofcjihldck
[20] https://videotronicmaker.com/arduino-tutorials/lm-studio-local-inference-server-nlp-upgrade-using-free-google-text-to-speech-api/
</td></tr></table>