# Nari Labs - Dia

> Dia is a 1.6B parameter text to speech model created by Nari Labs.

> A TTS model capable of generating ultra-realistic dialogue in one pass.

- Learn from https://www.linkedin.com/feed/update/urn:li:activity:7320822069850517506/
```
模型：
https://huggingface.co/nari-labs/Dia-1.6B

程式碼：
https://github.com/nari-labs/dia/

官方網站：
https://yummy-fir-7a4.notion.site/dia
```
- Git Repo
  - https://github.com/nari-labs/dia/
- HuggingFace
  - https://huggingface.co/nari-labs/Dia-1.6B

## 2025-07-21

### Quick Start

- 根據 [HuggingFace 說明的 Quick Start](https://huggingface.co/nari-labs/Dia-1.6B#%E2%9A%A1%EF%B8%8F-quickstart)
```
~/git$ git clone https://github.com/nari-labs/dia.git
Cloning into 'dia'...
remote: Enumerating objects: 421, done.
remote: Counting objects: 100% (292/292), done.
remote: Compressing objects: 100% (114/114), done.
remote: Total 421 (delta 256), reused 178 (delta 178), pack-reused 129 (from 2)
Receiving objects: 100% (421/421), 740.32 KiB | 474.00 KiB/s, done.
Resolving deltas: 100% (272/272), done.
~/git$ cd dia && uv run app.py
Using CPython 3.10.17
Creating virtual environment at: C:\Users\jazzw\git\dia\.venv
      Built nari-tts @ file:///C:/Users/jazzw/git/dia
      Built randomname==0.2.1
      Built fire==0.7.0
      Built julius==0.2.7
      Built argbind==0.3.9
```
