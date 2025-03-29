# TAIDE

## 2025-03-29

- 雖然曾關切 TAIDE 的歷史發展，不過沒真正拿來應用。今天來測試用 ollama 跑跑看。
- 剛好看到 TAIDE 的問答集裡提到 https://huggingface.co/tetf/Llama-3.1-TAIDE-LX-8B-Chat-GGUF
- 是可以用這個方式直接下載來跑
```bash
ollama run hf.co/tetf/Llama-3.1-TAIDE-LX-8B-Chat-GGUF:Q4_K_M
```
- 不過這樣的缺點是 model 名稱會很長，所以簡單做了個小微調
```bash
jazzw@JazzBook:~/git/snippet/go/ollama$ cat taide-lx-8b-chat-q4_k_m
FROM hf.co/tetf/Llama-3.1-TAIDE-LX-8B-Chat-GGUF:Q4_K_M
jazzw@JazzBook:~/git/snippet/go/ollama$ ollama create taide-lx-8b-chat:q4_k_m -f taide-lx-8b-chat-q4_k_m
gathering model components
pulling manifest ⠧
pulling 2ec5d4641b0e...  39% ▕███████████████████████████████████                                                         ▏ 2.0 GB/5.3 GB  1.7 MB/s  30m49s
```
- 等抓好就可以做測試啦 :P