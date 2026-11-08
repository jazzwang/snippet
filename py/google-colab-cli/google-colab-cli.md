# Google Colab CLI

- Git Repo
  - https://github.com/googlecolab/google-colab-cli

## 2026-06-11

- Read from: https://www.linkedin.com/feed/update/urn:li:activity:7470771669742063616
> 一行指令，就能即時取得免費 GPU？！
> Google 推出 Colab CLI，包含四大功能:
> 1. 即時配置GPU
> 2. 遠端執行
> 3. 取回資料
> 4. 互動存取
- 2026-06-05
  - Introducing the Google Colab CLI
  - https://developers.googleblog.com/introducing-the-google-colab-cli/

## 2026-06-12

- Windows 11 實測
```bash
~$ uv tool install google-colab-cli
~$ colab
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\scoop\persist\uv\tools\shims\colab.exe\__main__.py", line 5, in <module>
    from colab_cli.cli import main
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\cli.py", line 26, in <module>
    from colab_cli.commands import session, execution, files, automation, run, utility
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\commands\execution.py", line 28, in <module>
    from colab_cli.console import connect_console
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\console.py", line 20, in <module>
    import termios
ModuleNotFoundError: No module named 'termios'
~$ uv tool install google-colab-cli --with termios
  × No solution found when resolving dependencies:
  ╰─▶ Because termios was not found in the package registry and you require termios, we can conclude that your requirements are unsatisfiable.
~$ uv tool uninstall google-colab-cli
Uninstalled 1 executable: colab.exe
```
- 改用 WSL 測試看看
```bash
~$ wsl
/mnt/c/Users/jazzw$ which uv
/home/jazz/.local/bin/uv
/mnt/c/Users/jazzw$ uv tool install google-colab-cli
/mnt/c/Users/jazzw$ colab

 Usage: colab [OPTIONS] COMMAND [ARGS]...

 Colab CLI

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --client-oauth-config  -c      TEXT          Path to client OAuth config JSON file                                 │
│                                              [default: /home/jazz/.colab-cli-oauth-config.json]                    │
│ --config                       TEXT          Path to session state file (~/.config/colab-cli/sessions.json)        │
│ --logtostderr                                Log all output to stderr                                              │
│ --auth                         [oauth2|adc]  Authentication strategy to use: 'oauth2' (public InstalledAppFlow),   │
│                                              or 'adc' (Application Default Credentials).                           │
│                                              [default: oauth2]                                                     │
│ --install-completion                         Install completion for the current shell.                             │
│ --show-completion                            Show completion for the current shell, to copy it or                  │
│                                              customize the installation.                                           │
│ --help                 -h                    Show this message and exit.                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ console         Connect to raw TTY console                                                                         │
│ download        Download a file from a session                                                                     │
│ drivemount      Mount Google Drive at path                                                                         │
│ edit            Edit a file on a running Colab session                                                             │
│ exec            Execute code in a session                                                                          │
│ help            Show help for a command.                                                                           │
│ install         Install python packages on the VM                                                                  │
│ log             Manage and view session history logs                                                               │
│ ls              List files in a session                                                                            │
│ new             Create a new session                                                                               │
│ pay             Open the Colab signup page to manage compute units                                                 │
│ readme          Print the bundled README.md file                                                                   │
│ repl            Start an interactive REPL                                                                          │
│ restart-kernel  Restart a session's kernel                                                                         │
│ rm              Remove a remote file                                                                               │
│ run             Run a Python script on a fresh Colab VM, then release the VM                                       │
│ sessions        List all active sessions                                                                           │
│ skill           Print the bundled COLAB_SKILL.md file                                                              │
│ status          Show session status                                                                                │
│ stop            Stop a session                                                                                     │
│ update          Check for latest version and print if an update is available                                       │
│ upload          Upload a file to a session                                                                         │
│ url             Print a browser URL that connects to an existing session.                                          │
│ version         Show the version of the Colab CLI                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
/mnt/c/Users/jazzw$
```

## 2026-11-08

> [!NOTE]
> 根據 "https://developers.googleblog.com/introducing-the-google-colab-cli/ https://developers.googleblog.com/introducing-the-google-colab-cli/" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "py/google-colab-cli/google-colab-cli.md" .

## Google Colab CLI 技術報告

> 根據 Google 官方公告與 GitHub 倉庫文件撰寫
> 
> **公告日期**：2026 年 6 月 5 日  
> **GitHub 倉庫**：[https://github.com/googlecolab/google-colab-cli](https://github.com/googlecolab/google-colab-cli)  
> **平台支援**：Linux、macOS（Windows 暫不支援）

### 1. 簡介

Google Colab CLI（Command-Line Interface）是 Google 最新推出的終端機介面工具，橋接本地終端機與遠端 Colab 運算環境，提供無障礙的 AI 開發體驗。此工具特別適合開發者、自動化工作流與 AI Agent 使用，讓使用者能直接在終端機中管理高階運算資源、執行 Python 程式碼、管理遠端檔案與自動化 ML 流程。

#### 核心功能

| 功能 | 說明 |
|------|------|
| **無縫資源配發** | 透過 `colab --gpu` 或 `colab --tpu` 指令，幾秒鐘即可配發高階 GPU/TPU 環境（如 T4、L4、A100、TPU v5e1/v6e1） |
| **遠端程式碼執行** | 使用 `colab exec` 執行本地 Python 腳本、Jupyter Notebook 或管道輸入的程式碼 |
| **互動式環境** | `colab repl` 或 `colab console` 提供遠端互動式 Python REPL 或 TTY Shell 環境 |
| **資源管理** | `colab new`、`colab stop` 等指令管理虛擬機生命週期 |
| **檔案操作** | `colab upload`、`colab download`、`colab ls` 等遠端檔案系統操作 |
| **自動化支援** | `colab run` 提供 ephemeral 模式，自動配發、執行、回收資源 |

### 2. 系統需求

| 項目 | 需求 |
|------|------|
| **作業系統** | Linux 或 macOS |
| **Python** | 建議使用 `uv`（推薦）或標準 `pip` |
| **網路連線** | 需能連接到 Google Colab API |
| **認證方式** | Google 帳戶（支援 OAuth2 或 Application Default Credentials） |

> **注意**：使用高階加速器（GPU/TPU）需要 Colab Pro 或 Pro+ 訂閱方案。

### 3. 安裝步驟

#### 3.1 使用 `uv` 安裝（推薦）

```bash
## 使用 uv 套件管理工具安裝
uv tool install google-colab-cli
```

#### 3.2 使用 `pip` 安裝

```bash
## 使用標準 pip 安裝
pip install google-colab-cli
```

#### 3.3 檢查安裝是否成功

```bash
## 查看版本資訊
colab version

## 檢查是否有可用更新
colab update
```

#### 3.4 認證設定

首次使用時，CLI 會自動偵測認證方式：

```bash
## 使用 Application Default Credentials（預設）
## 通常用於本地開發環境

## 或使用 OAuth2 認證
colab auth
```

認證設定會儲存於：
- 會話金鑰：`~/.config/colab-cli/sessions.json`
- 全域設定：`~/.config/colab-cli/settings.json`

### 4. 快速開始

#### 4.1 建立會話並執行程式碼

```bash
## 步驟 1：配發新的 CPU 會話
colab new

## 步驟 2：透過 stdin 執行程式碼
echo 'print("Hello from Google Colab!")' | colab exec

## 步驟 3：停止並釋放資源
colab stop
```

#### 4.2 使用 GPU 加速器

```bash
## 配發 T4 GPU 環境
colab new --gpu T4

## 執行需要 GPU 的程式碼
echo 'import torch; print(torch.cuda.is_available())' | colab exec

## 停止會話
colab stop
```

#### 4.3 使用 ephemeral 模式（推薦用於自動化）

```bash
## 單一指令完成：配發、執行、回收
colab run --gpu T4 train.py

## 保留會話以便後續操作
colab run --gpu T4 --keep train.py
```

### 5. 主要指令說明

#### 5.1 會話管理

| 指令 | 說明 |
|------|------|
| `colab new [-s NAME] [--gpu GPU] [--tpu TPU] [--high-mem]` | 配發新的 CPU、GPU 或 TPU 虛擬機環境 |
| `colab sessions` | 列出所有目前活躍的會話 |
| `colab status [-s NAME]` | 顯示會話的硬體、機器型號、狀態與本機元資料 |
| `colab restart-kernel [-s NAME]` | 重啟會話的 Jupyter 核心 |
| `colab stop [-s NAME]` | 終止會話並釋放資源 |
| `colab url [-s NAME] [--open]` | 列印或開啟瀏覽器 URL 連接到活躍會話 |

#### 5.2 程式碼執行

| 指令 | 說明 |
|------|------|
| `colab run [--gpu GPU] [--tpu TPU] [--high-mem] [--keep] SCRIPT [ARGS...]` | 在新鮮虛擬機上執行本地腳本，自動回收資源 |
| `colab exec [-s NAME] [-f FILE] [--output-image PATH]` | 從 stdin、本地 `.py` 檔案或 `.ipynb` Notebook 執行 Python 程式碼 |
| `colab repl [-s NAME] [--output-image PATH]` | 在虛擬機啟動互動式 Python REPL（管道 EOF 時乾淨退出） |
| `colab console [-s NAME]` | 連接到遠端虛擬機的原始互動式 TTY Shell（tmux） |
| `colab ssh [-s NAME] [--proxy-mode] [-i KEY]` | 透過 WebSocket 開啟 SSH Shell，或作為 IDE 遠端開發的 OpenSSH ProxyCommand |

#### 5.3 檔案操作

| 指令 | 說明 |
|------|------|
| `colab ls [-s NAME] [PATH]` | 列出虛擬機上的遠端檔案 |
| `colab upload [-s NAME] LOCAL REMOTE` | 將本地檔案上傳到虛擬機檔案系統 |
| `colab download [-s NAME] REMOTE LOCAL` | 從虛擬機檔案系統下載遠端檔案 |
| `colab rm [-s NAME] PATH` | 刪除虛擬機上的遠端檔案 |
| `colab edit [-s NAME] PATH` | 使用本地 `$EDITOR` 就地編輯遠端檔案 |

#### 5.4 自動化與工具

| 指令 | 說明 |
|------|------|
| `colab auth [-s NAME]` | 為虛擬機認證 GCP 服務（BigQuery、GCS 等） |
| `colab drivemount [-s NAME] [PATH]` | 在虛擬機上掛載 Google Drive（預設：`/content/drive`） |
| `colab install [-s NAME] [-r FILE \| PKG...]` | 使用 `uv` 在虛擬機上安裝套件（fallback 到 `pip`） |
| `colab log [-s NAME] [-n N] [-o FILE]` | 查看或匯出會話歷史記錄（`.ipynb`、`.md`、`.txt`、`.jsonl`） |
| `colab usage` | 顯示帳戶運算單元使用率與餘額 |
| `colab pay` | 開啟 Colab 訂閱頁面管理運算單元 |

### 6. 實作範例

#### 6.1 GPU 加速訓練與權重檢索

```bash
## 配發 A100 GPU
colab new -s trainer --gpu A100

## 安裝需求套件
colab install -s trainer torch transformers

## 執行本地訓練腳本
colab exec -s trainer -f train.py

## 下載訓練產生的模型權重
colab download -s trainer checkpoints/model.bin ./model.bin

## 停止並回收資源
colab stop -s trainer
```

#### 6.2 整合 Google Drive 的 Notebook 執行

```bash
## 配發會話
colab new -s analysis

## 掛載 Google Drive
colab drivemount -s analysis

## 執行本地 Notebook
colab exec -s analysis -f report.ipynb

## 匯出執行記錄為 Markdown
colab log -s analysis -o execution_log.md

## 停止會話
colab stop -s analysis
```

#### 6.3 Shebang 執行支援

在 Python 腳本中加入 shebang，可直接透過 shebang 指定 `colab run`：

```python
##!/usr/bin/env -S colab run --gpu L4 --keep
import torch

print("L4 GPU Available:", torch.cuda.is_available())
print("Device Name:", torch.cuda.get_device_name(0))
```

使腳本可執行並運行：

```bash
chmod +x script.py
./script.py
```

`--keep` 選項會保留會話虛擬機，允許後續執行或檢視記錄。

#### 6.4 AI Agent 自動化 ML 流程範例

以下範例展示如何使用 Colab CLI 進行完整的 QLoRA 微調流程：

```bash
## 1. 配發 T4 GPU 環境
colab new --gpu T4

## 2. 安裝必要的 ML 套件
colab install transformers datasets peft trl bitsandbytes accelerate

## 3. 執行遠端微調腳本
colab exec -f finetune_run.py

## 4. 下載微調後的 adapter 模型
colab download -s trainer adapter_model.safetensors ./models/

## 5. 保存 Notebook 記錄
colab log --output gemma_finetune_log.ipynb

## 6. 停止會話
colab stop
```

### 7. 驗證測試步驟

#### 7.1 安裝驗證

```bash
## 檢查 CLI 版本
colab version

## 檢查是否有更新
colab update
```

#### 7.2 基本功能測試

```bash
## 測試 1：會話建立與執行
colab new
echo 'print("Hello, Colab CLI!")' | colab exec
colab stop

## 測試 2：GPU 可用性
colab new --gpu T4
echo 'import torch; print("GPU Available:", torch.cuda.is_available())' | colab exec
colab stop

## 測試 3：檔案操作
colab new
echo "Hello from Colab" > test.txt
colab upload -s test.txt test.txt ./local_file.txt
cat ./local_file.txt
colab download -s test.txt test.txt ./downloaded.txt
cat ./downloaded.txt
colab stop
```

#### 7.3 自動化流程驗證

```bash
## 測試 ephemeral 模式
colab run --gpu T4 -f <<EOF
import torch
print("CUDA version:", torch.version.cuda)
print("GPU count:", torch.cuda.device_count())
EOF
```

#### 7.4 整合測試（Google Drive）

```bash
## 測試 Drive 掛載
colab new
colab drivemount
echo 'import os; print("Drive path:", os.listdir("/content/drive"))' | colab exec
colab stop
```

#### 7.5 互動模式測試

```bash
## 測試 REPL 模式
echo 'print("Repl test:", 2 + 2)' | colab repl

## 測試 Console 模式
echo 'import sys; print(sys.version)' | colab console
```

### 8. 注意事項

#### 8.1 平台限制

- 目前僅支援 **Linux** 和 **macOS**
- Windows 平台暫不支援

#### 8.2 認證與授權

- 使用高階加速器（GPU/TPU）需要 **Colab Pro** 或 **Pro+** 訂閱
- 認證方式支援：
  - OAuth2（預設）
  - Application Default Credentials（ADC）

#### 8.3 會話管理

- 當只有單一會話活躍時，可省略 `-s, --session` 選項
- CLI 會自動識別唯一活躍會話
- 會話狀態可透過 `colab sessions` 或 `colab status` 查詢

#### 8.4 互動模式要求

- `repl` 和 `console` 指令需要本地 TTY
- 自動化腳本或流程中，請透過管道輸入（如 `echo "print(1)" | colab repl`）觸發非互動模式

#### 8.5 檔案傳輸

- 執行 `colab exec -f file.py` 時，CLI 會自動讀取本地檔案並傳輸到遠端核心
- 無需手動上傳檔案即可執行

#### 8.6 儲存與狀態

- 會話金鑰與元資料儲存於 `~/.config/colab-cli/sessions.json`
- 全域 CLI 設定位於 `~/.config/colab-cli/settings.json`
- 可透過 `--config` 參數自訂或隔離設定路徑

### 9. 進階使用技巧

#### 9.1 環境變數設定

```bash
## 設定 OAuth 客戶端配置
export COLAB_CLI_OAUTH_CONFIG=~/.colab-cli-oauth-config.json

## 設定日誌輸出到 stderr
colab exec --logtostderr -f script.py
```

#### 9.2 自動化腳本範例

```bash
##!/bin/bash
## automated_training.sh

## 配發環境
colab new -s training_job --gpu A100

## 安裝套件
colab install -s training_job torch transformers datasets

## 執行訓練
colab exec -s training_job -f train.py -- --epochs 10

## 下載結果
colab download -s training_job checkpoints/best_model.pt ./output/

## 匯出記錄
colab log -s training_job -o training_log.ipynb

## 停止
colab stop -s training_job

echo "Training completed!"
```

#### 9.3 使用 `uv` 進行套件管理

```bash
## 使用 uv 安裝（比 pip 更快）
colab install -s session --uv torch torchvision

## 指定 requirements 檔案
colab install -s session -r requirements.txt
```

### 10. 參考資源

- **官方 GitHub 倉庫**：[https://github.com/googlecolab/google-colab-cli](https://github.com/googlecolab/google-colab-cli)
- **官方公告**：[https://developers.googleblog.com/introducing-the-google-colab-cli/](https://developers.googleblog.com/introducing-the-google-colab-cli/)
- **Colab 使用條款**：[https://research.google.com/colaboratory/tos_v6.html](https://research.google.com/colaboratory/tos_v6.html)
- **Google 隱私政策**：[https://policies.google.com/privacy](https://policies.google.com/privacy)

### 11. 相關項目

- **[Colab MCP Server](https://github.com/googlecolab/colab-mcp)**：針對 Notebook 內互動式 Agent 輔助編碼的替代方案
- **[Google Colab](https://colab.research.google.com/)**：原始 Colab 網頁版平台

*本文檔最後更新：2026 年 6 月 5 日*

---
title: "Introducing the Google Colab CLI- Google Developers Blog"
source: "https://developers.googleblog.com/introducing-the-google-colab-cli/"
author:
  - "[[Spencer Shumway]]"
  - "[[Tyler Pirtle]]"
  - "[[Seth Troisi]]"
published: 2026-06-05
created: 2026-11-08
description: "Google 宣佈推出新的 Google Colab CLI，這是一款輕量級工具，可串接本地終端機與遠端執行環境，提供無阻礙的 GPU/TPU 離線運算。了解開發者和 AI 代理如何執行遠端腳本、下載模型並自動化機學習流程。"
---

## 推出 Google Colab CLI

[Spencer Shumway](https://developers.googleblog.com/search/?author=Spencer+Shumway) Google Colab 產品經理

[Tyler Pirtle](https://developers.googleblog.com/search/?author=Tyler+Pirtle) 軟體工程師

[Seth Troisi](https://developers.googleblog.com/search/?author=Seth+Troisi) 軟體工程師

![Screenshot 2026-06-05 at 12.53.56 PM](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Screenshot_2026-06-05_at_12.53.56PM.original.png)

今天我們正式宣佈推出 [Google Colab 指令行介面](https://github.com/googlecolab/google-colab-cli)（CLI），這項工具可填補您的本地終端機與遠端 Colab 執行環境之間的差距，為開發者和 AI 代理提供零阻礙的執行平台。Colab CLI 提供：

- **零阻礙加速器資源配置：** 立即請求高階 GPU 或 TPU（例如 `colab --gpu A100` 或 `colab --gpu T4`）。
- **簡單的遠端執行：** 使用 `colab exec` 直接在 Colab 執行環境上執行您的本地 Python 腳本和複雜的機學習流程。
- **無縫的產物恢復：** 透過 `colab download` 和 `colab log` 輕鬆取得模型、資料集以及可重播的 `.ipynb` 記錄檔。
- **互動式存取：** 使用 `colab repl` 或 `colab console` 進入遠端 Colab 執行環境的互動式環境。

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/ColabCLILarge.mp4" type="video/mp4"><p>抱歉，您的瀏覽器不支援播放此視頻</p></video>

### 代理驅動的實際工作流程

由於 Colab CLI 可無縫整合至標準終端機環境，任何擁有終端機存取權的代理都可以使用。為了確保您的 AI 助手可以立即投入工作，CLI 包含一個預先打包的 Colab [技能檔案](https://github.com/googlecolab/google-colab-cli/blob/main/skills/colab-operator/SKILL.md)，讓代理獲得有關如何充分利用 CLI 的即時、內建背景知識。讓我們看看用戶或代理使用 Colab CLI 時可能嘗試的實際範例。

*請注意，雖然以下範例顯示 [Antigravity](https://antigravity.google/) 代理將 Colab CLI 作為工具使用，但 Colab CLI 也很容易被 Claude Code、Codex 和其他代理使用。

以下是代理如何使用 Colab CLI 進行實際的機學習工作流程：

#### 微調 Gemma 3-1B

CLI 可用於執行完整的 QLoRA 流程，只需幾個命令即可完成。透過指示 Antigravity（或您選擇的代理）建立遠端微調工作，將繁重的運算任務無須輸入任何雲端配置命令就交由 GPU 處理。在此情境中，我們要求代理使用 Colab CLI 在 [Text-to-SQL 資料集](https://huggingface.co/datasets/philschmid/gretel-synthetic-text-to-sql) 上微調 [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it)，使模型更擅長撰寫 SQL 查詢。

**Antigravity 的提示詞：**  
使用 Colab CLI (https://github.com/googlecolab/google-colab-cli) 使用 QLoRA 微調 Gemma 3 1B。配置一個 Colab T4 GPU 執行環境，安裝所需的機學習套件（transformers、datasets、peft、trl 等），遠端執行我的本地 ~ [finetune_run](https://github.com/googlecolab/google-colab-cli/blob/main/examples/finetune_run.py)[.py](https://gist.github.com/spencersgoogle/05be7d5b8a86785284a72032d11e7214) 腳本，下載產生的 safetensors 適配器，儲存筆記本記錄檔，並進行清理。

**Antigravity 執行：**

```shell
$ colab new --gpu T4
$ colab install transformers datasets peft trl bitsandbytes accelerate
$ colab exec -f finetune_run.py
$ colab log --output gemma_finetune_log.ipynb
$ colab stop
```

Antigravity 也使用 "colab download" 命令下載適配器模型、適配器配置、分詞器配置和分詞器，這些可用於在本地載入並執行您的微調模型。現在您擁有一個可在本地設備上進行服務的遠端微調模型！

### 立即嘗試

Colab CLI 讓強大的 Colab 運算能力可存取、可程式化並準備好供代理使用。它輕量且可被任何基於終端機的 AI 代理輕鬆存取。若要開始自行使用 Colab CLI，請前往 [Google Colab CLI GitHub 儲存庫](https://github.com/googlecolab/google-colab-cli) 查看設定說明。

我們很期待看到這如何加速您的開發流程，並樂見您和您的代理所建造的成果！
