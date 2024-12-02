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