# sha256sum 

- 2024-05-11: Generating an SHA-256 Hash From the Command Line
  - https://www.baeldung.com/linux/sha-256-from-command-line

## 需求

- 2025-03-19: 
  - 遇到奇怪的狀況，ollama 0.6.0 以後因為導入 Gemma 3 模型的支援，原本用起來效果不錯，沒動過檔案的 Qwen2.5 Coder 7B 模型突然變笨了，不管問什麼都回答一樣的句子。
  - 為了想要回溯回 ollama 0.5.13，根據 scoop 定義的 `ollama.json` 0.5.13 版，本機從 Github 下載 ZIP 檔很慢很慢，
    所以改用 Github Codespace 跟 Google Cloud Shell 先下載再下載，會快一點。
  - 因為在不同的平台上下載了不同版本 0.6.2 跟 0.5.13，檔名都一樣，結果分不出來 ZIP 是哪個版本。所以只好把腦筋動到 checksum 上。

| Github URL | version | checksum |
|------------|---------|----------|
| https://github.com/ollama/ollama/releases/download/v0.6.2/ollama-windows-amd64.zip | 0.6.2 | 40519cbb53aaf866c63f3b20e63e72f2e7606c7b43453c83e7d22003e139d3ee |
| https://github.com/ollama/ollama/releases/download/v0.6.1/ollama-windows-amd64.zip | 0.6.1 | 979ae70a4ed8cff8f2c70df73e1233f75e8e5f3be59efe95ac3cd116eeef5c91 |
| https://github.com/ollama/ollama/releases/download/v0.5.13/ollama-windows-amd64.zip | 0.5.13 | 20ca8745085f18b61dfd3b41681a3325f0500a4e2eb6096d971808a7529c3dbd |

## 用法

- ( 2025-03-19 23:34:14 )
```bash
jazzwang_tw@cloudshell:~$ sha256sum ollama-windows-amd64.zip 
20ca8745085f18b61dfd3b41681a3325f0500a4e2eb6096d971808a7529c3dbd  ollama-windows-amd64.zip
```
- 這個是 0.5.13 版。
- Google CloudShell 下指令觸發檔案下載：
```bash
jazzwang_tw@cloudshell:~$ cloudshell download ollama-windows-amd64.zip
```