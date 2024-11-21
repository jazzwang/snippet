# Using the Text-to-Speech API with Python

## 2024-11-21

- ( 2024-11-21 21:50:57 )
- https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3

```bash
jazzwang_tw@cloudshell:~$ gcloud auth list
jazzwang_tw@cloudshell:~$ gcloud config set project hadoop-labs
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud services enable texttospeech.googleapis.com
jazzwang_tw@cloudshell:~ (hadoop-labs)$ virtualenv venv-texttospeech
jazzwang_tw@cloudshell:~ (hadoop-labs)$ source venv-texttospeech/bin/activate
(venv-texttospeech) jazzwang_tw@cloudshell:~ (hadoop-labs)$ pip install ipython google-cloud-texttospeech
(venv-texttospeech) jazzwang_tw@cloudshell:~ (hadoop-labs)$ ipython
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.29.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from typing import Sequence
   ...:
   ...: import google.cloud.texttospeech as tts
   ...:
   ...:
   ...: def unique_languages_from_voices(voices: Sequence[tts.Voice]):
   ...:     language_set = set()
   ...:     for voice in voices:
   ...:         for language_code in voice.language_codes:
   ...:             language_set.add(language_code)
   ...:     return language_set
   ...:
   ...:
   ...: def list_languages():
   ...:     client = tts.TextToSpeechClient()
   ...:     response = client.list_voices()
   ...:     languages = unique_languages_from_voices(response.voices)
   ...:
   ...:     print(f" Languages: {len(languages)} ".center(60, "-"))
   ...:     for i, language in enumerate(sorted(languages)):
   ...:         print(f"{language:>10}", end="\n" if i % 5 == 4 else "")
   ...:

In [2]: list_languages()
---------------------- Languages: 60 -----------------------
     af-ZA     am-ET     ar-XA     bg-BG     bn-IN
     ca-ES    cmn-CN    cmn-TW     cs-CZ     da-DK
     de-DE     el-GR     en-AU     en-GB     en-IN
     en-US     es-ES     es-US     et-EE     eu-ES
     fi-FI    fil-PH     fr-CA     fr-FR     gl-ES
     gu-IN     he-IL     hi-IN     hu-HU     id-ID
     is-IS     it-IT     ja-JP     kn-IN     ko-KR
     lt-LT     lv-LV     ml-IN     mr-IN     ms-MY
     nb-NO     nl-BE     nl-NL     pa-IN     pl-PL
     pt-BR     pt-PT     ro-RO     ru-RU     sk-SK
     sr-RS     sv-SE     ta-IN     te-IN     th-TH
     tr-TR     uk-UA     ur-IN     vi-VN    yue-HK

In [3]: import google.cloud.texttospeech as tts
   ...:
   ...:
   ...: def list_voices(language_code=None):
   ...:     client = tts.TextToSpeechClient()
   ...:     response = client.list_voices(language_code=language_code)
   ...:     voices = sorted(response.voices, key=lambda voice: voice.name)
   ...:
   ...:     print(f" Voices: {len(voices)} ".center(60, "-"))
   ...:     for voice in voices:
   ...:         languages = ", ".join(voice.language_codes)
   ...:         name = voice.name
   ...:         gender = tts.SsmlVoiceGender(voice.ssml_gender).name
   ...:         rate = voice.natural_sample_rate_hertz
   ...:         print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")
   ...:

In [4]: list_voices("en")
----------------------- Voices: 106 ------------------------
en-AU    | en-AU-Journey-D          | MALE     | 24,000 Hz
en-AU    | en-AU-Journey-F          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Journey-O          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Neural2-A          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Neural2-B          | MALE     | 24,000 Hz
en-AU    | en-AU-Neural2-C          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Neural2-D          | MALE     | 24,000 Hz
en-AU    | en-AU-News-E             | FEMALE   | 24,000 Hz
en-AU    | en-AU-News-F             | FEMALE   | 24,000 Hz
en-AU    | en-AU-News-G             | MALE     | 24,000 Hz
en-AU    | en-AU-Polyglot-1         | MALE     | 24,000 Hz
en-AU    | en-AU-Standard-A         | FEMALE   | 24,000 Hz
en-AU    | en-AU-Standard-B         | MALE     | 24,000 Hz
en-AU    | en-AU-Standard-C         | FEMALE   | 24,000 Hz
en-AU    | en-AU-Standard-D         | MALE     | 24,000 Hz
en-AU    | en-AU-Wavenet-A          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Wavenet-B          | MALE     | 24,000 Hz
en-AU    | en-AU-Wavenet-C          | FEMALE   | 24,000 Hz
en-AU    | en-AU-Wavenet-D          | MALE     | 24,000 Hz
en-GB    | en-GB-Journey-D          | MALE     | 24,000 Hz
en-GB    | en-GB-Journey-F          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Journey-O          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Neural2-A          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Neural2-B          | MALE     | 24,000 Hz
en-GB    | en-GB-Neural2-C          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Neural2-D          | MALE     | 24,000 Hz
en-GB    | en-GB-Neural2-F          | FEMALE   | 24,000 Hz
en-GB    | en-GB-News-G             | FEMALE   | 24,000 Hz
en-GB    | en-GB-News-H             | FEMALE   | 24,000 Hz
en-GB    | en-GB-News-I             | FEMALE   | 24,000 Hz
en-GB    | en-GB-News-J             | MALE     | 24,000 Hz
en-GB    | en-GB-News-K             | MALE     | 24,000 Hz
en-GB    | en-GB-News-L             | MALE     | 24,000 Hz
en-GB    | en-GB-News-M             | MALE     | 24,000 Hz
en-GB    | en-GB-Standard-A         | FEMALE   | 24,000 Hz
en-GB    | en-GB-Standard-B         | MALE     | 24,000 Hz
en-GB    | en-GB-Standard-C         | FEMALE   | 24,000 Hz
en-GB    | en-GB-Standard-D         | MALE     | 24,000 Hz
en-GB    | en-GB-Standard-F         | FEMALE   | 24,000 Hz
en-GB    | en-GB-Standard-N         | FEMALE   | 24,000 Hz
en-GB    | en-GB-Standard-O         | MALE     | 24,000 Hz
en-GB    | en-GB-Studio-B           | MALE     | 24,000 Hz
en-GB    | en-GB-Studio-C           | FEMALE   | 24,000 Hz
en-GB    | en-GB-Wavenet-A          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Wavenet-B          | MALE     | 24,000 Hz
en-GB    | en-GB-Wavenet-C          | FEMALE   | 24,000 Hz
en-GB    | en-GB-Wavenet-D          | MALE     | 24,000 Hz
en-GB    | en-GB-Wavenet-F          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Journey-D          | MALE     | 24,000 Hz
en-IN    | en-IN-Journey-F          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Journey-O          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Neural2-A          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Neural2-B          | MALE     | 24,000 Hz
en-IN    | en-IN-Neural2-C          | MALE     | 24,000 Hz
en-IN    | en-IN-Neural2-D          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Standard-A         | FEMALE   | 24,000 Hz
en-IN    | en-IN-Standard-B         | MALE     | 24,000 Hz
en-IN    | en-IN-Standard-C         | MALE     | 24,000 Hz
en-IN    | en-IN-Standard-D         | FEMALE   | 24,000 Hz
en-IN    | en-IN-Standard-E         | FEMALE   | 24,000 Hz
en-IN    | en-IN-Standard-F         | MALE     | 24,000 Hz
en-IN    | en-IN-Wavenet-A          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Wavenet-B          | MALE     | 24,000 Hz
en-IN    | en-IN-Wavenet-C          | MALE     | 24,000 Hz
en-IN    | en-IN-Wavenet-D          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Wavenet-E          | FEMALE   | 24,000 Hz
en-IN    | en-IN-Wavenet-F          | MALE     | 24,000 Hz
en-US    | en-US-Casual-K           | MALE     | 24,000 Hz
en-US    | en-US-Journey-D          | MALE     | 24,000 Hz
en-US    | en-US-Journey-F          | FEMALE   | 24,000 Hz
en-US    | en-US-Journey-O          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-A          | MALE     | 24,000 Hz
en-US    | en-US-Neural2-C          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-D          | MALE     | 24,000 Hz
en-US    | en-US-Neural2-E          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-F          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-G          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-H          | FEMALE   | 24,000 Hz
en-US    | en-US-Neural2-I          | MALE     | 24,000 Hz
en-US    | en-US-Neural2-J          | MALE     | 24,000 Hz
en-US    | en-US-News-K             | FEMALE   | 24,000 Hz
en-US    | en-US-News-L             | FEMALE   | 24,000 Hz
en-US    | en-US-News-N             | MALE     | 24,000 Hz
en-US    | en-US-Polyglot-1         | MALE     | 24,000 Hz
en-US    | en-US-Standard-A         | MALE     | 24,000 Hz
en-US    | en-US-Standard-B         | MALE     | 24,000 Hz
en-US    | en-US-Standard-C         | FEMALE   | 24,000 Hz
en-US    | en-US-Standard-D         | MALE     | 24,000 Hz
en-US    | en-US-Standard-E         | FEMALE   | 24,000 Hz
en-US    | en-US-Standard-F         | FEMALE   | 24,000 Hz
en-US    | en-US-Standard-G         | FEMALE   | 24,000 Hz
en-US    | en-US-Standard-H         | FEMALE   | 24,000 Hz
en-US    | en-US-Standard-I         | MALE     | 24,000 Hz
en-US    | en-US-Standard-J         | MALE     | 24,000 Hz
en-US    | en-US-Studio-O           | FEMALE   | 24,000 Hz
en-US    | en-US-Studio-Q           | MALE     | 24,000 Hz
en-US    | en-US-Wavenet-A          | MALE     | 24,000 Hz
en-US    | en-US-Wavenet-B          | MALE     | 24,000 Hz
en-US    | en-US-Wavenet-C          | FEMALE   | 24,000 Hz
en-US    | en-US-Wavenet-D          | MALE     | 24,000 Hz
en-US    | en-US-Wavenet-E          | FEMALE   | 24,000 Hz
en-US    | en-US-Wavenet-F          | FEMALE   | 24,000 Hz
en-US    | en-US-Wavenet-G          | FEMALE   | 24,000 Hz
en-US    | en-US-Wavenet-H          | FEMALE   | 24,000 Hz
en-US    | en-US-Wavenet-I          | MALE     | 24,000 Hz
en-US    | en-US-Wavenet-J          | MALE     | 24,000 Hz

In [5]: import google.cloud.texttospeech as tts
   ...: 
   ...: 
   ...: def text_to_wav(voice_name: str, text: str):
   ...:     language_code = "-".join(voice_name.split("-")[:2])
   ...:     text_input = tts.SynthesisInput(text=text)
   ...:     voice_params = tts.VoiceSelectionParams(
   ...:         language_code=language_code, name=voice_name
   ...:     )
   ...:     audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)
   ...: 
   ...:     client = tts.TextToSpeechClient()
   ...:     response = client.synthesize_speech(
   ...:         input=text_input,
   ...:         voice=voice_params,
   ...:         audio_config=audio_config,
   ...:     )
   ...: 
   ...:     filename = f"{voice_name}.wav"
   ...:     with open(filename, "wb") as out:
   ...:         out.write(response.audio_content)
   ...:         print(f'Generated speech saved to "{filename}"')
   ...: 

In [6]: text_to_wav("en-AU-Neural2-A", "What is the temperature in Sydney?")
   ...: text_to_wav("en-GB-Neural2-B", "What is the temperature in London?")
   ...: text_to_wav("en-IN-Wavenet-C", "What is the temperature in Delhi?")
   ...: text_to_wav("en-US-Studio-O", "What is the temperature in New York?")
   ...: text_to_wav("fr-FR-Neural2-A", "Quelle est la température à Paris ?")
   ...: text_to_wav("fr-CA-Neural2-B", "Quelle est la température à Montréal ?")
Generated speech saved to "en-AU-Neural2-A.wav"
Generated speech saved to "en-GB-Neural2-B.wav"
Generated speech saved to "en-IN-Wavenet-C.wav"
Generated speech saved to "en-US-Studio-O.wav"
Generated speech saved to "fr-FR-Neural2-A.wav"
Generated speech saved to "fr-CA-Neural2-B.wav"

In [7]: !cloudshell download *.wav

In [8]: quit()

(venv-texttospeech) jazzwang_tw@cloudshell:~ (hadoop-labs)$
(venv-texttospeech) jazzwang_tw@cloudshell:~ (hadoop-labs)$ deactivate
jazzwang_tw@cloudshell:~ (hadoop-labs)$
```
