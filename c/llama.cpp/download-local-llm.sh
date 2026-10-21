#!/bin/bash
## [09/07 14:31:21] - 下載測試
## wget -c https://huggingface.co/empero-ai/Qwythos-9B-v2-GGUF/resolve/main/Qwythos-9B-v2-MTP-Q4_K_M.gguf
## [10/16 22:39:03] rm Qwythos-9B-v2-MTP-Q4_K_M.gguf
## 移除原因：(1) 基底仍是 Qwen/Qwen3.5-9B-Base (2) 實測 8G VRAM 只能有 29K context window (3) unsloth/Qwen3.5-9B （降到 38K context window）已經很夠用

## [09/26 12:01:20] - 下載測試
## wget -c https://huggingface.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF/resolve/main/Qwen2.5-7B-Instruct-1M-Q4_K_M.gguf
## [10/16 22:37:18] rm Qwen2.5-7B-Instruct-1M-Q4_K_M.gguf
## 移除原因：(1) 跟 Pi Agent 相容性不佳，因為沒有 Reasoning，所以很多時候都只能做 Tool Calling 進行 web search

## [10/13 17:45:28] - 下載測試
wget -c https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/resolve/main/Qwen3.5-9B-Q4_K_M.gguf

## [10/15 16:08:04] - 下載測試
## wget -c https://huggingface.co/tedslin/gemma-3-4B-T1-it-Q4_K_M-GGUF/resolve/main/gemma-3-4b-t1-it-q4_k_m.gguf
## [10/16 22:39:16] rm gemma-3-4b-t1-it-q4_k_m.gguf
## 移除原因：llama.cpp 載入失敗，原因待查

## [10/20 00:20:05] - 下載測試
wget -c https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF/resolve/main/MiMo-V2.6-Distill-Qwen-9B-Q4_K_M.gguf

## [10/20 10:12:04] - 下載測試
## wget -c https://huggingface.co/mradermacher/translategemma-12b-it-GGUF/resolve/main/translategemma-12b-it.Q4_K_S.gguf
## 移除原因：llama.cpp 載入失敗，原因待查
