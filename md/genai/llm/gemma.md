# Google Gemma

## Gemma 2

### 2025-01-14

- https://huggingface.co/bartowski/gemma-2-2b-it-GGUF

- 下載 `gemma-2-9b-it-Q2_K.gguf`

```bash
jazzw@JazzBook:~$ cd .ollama/models/
jazzw@JazzBook:~/.ollama/models$ mkdir gemma-2-9b-it-gguf
jazzw@JazzBook:~/.ollama/models$ cd gemma-2-9b-it-gguf/
jazzw@JazzBook:~/.ollama/models/gemma-2-9b-it-gguf$ wget https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/resolve/main/gemma-2-9b-it-Q2_K.gguf

Connecting to cdn-lfs-us-1.hf.co (cdn-lfs-us-1.hf.co)|3.169.36.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3805397952 (3.5G) [binary/octet-stream]
Saving to: 'gemma-2-9b-it-Q2_K.gguf'

gemma-2-9b-it-Q2_K.gguf                100%[============================================================================>]   3.54G  1.73MB/s    in 34m 10s

2025-01-14 21:30:34 (1.77 MB/s) - 'gemma-2-9b-it-Q2_K.gguf' saved [3805397952/3805397952]
```

- 用最簡單的 Modelfile 匯入 Gemma 2 9B Instruct Q2_K 模型

```bash
jazzw@JazzBook:~/.ollama/models/gemma-2-9b-it-gguf$ cat > Modelfile << EOF
FROM gemma-2-9b-it-Q2_K.gguf
EOF
jazzw@JazzBook:~/.ollama/models/gemma-2-9b-it-gguf$ ollama create gemma-2-9b-it -f Modelfile
transferring model data 100%
using existing layer sha256:2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403
using autodetected template gemma-instruct
using existing layer sha256:2490e7468436707d5156d7959cf3c6341cc46ee323084cfa3fcf30fe76e397dc
creating new layer sha256:f01f72e2d77f367b87c2ef63b4deb185b031d32ed6beee859cd13207d14440de
writing manifest
success
jazzw@JazzBook:~/.ollama/models/gemma-2-9b-it-gguf$ ollama list
NAME                    ID              SIZE      MODIFIED
gemma-2-9b-it:latest    51dee1323fb5    3.8 GB    6 seconds ago
jazzw@JazzBook:~/.ollama/models/gemma-2-9b-it-gguf$ ollama run gemma-2-9b-it:latest
>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.

>>> /show model
Unknown command '/show model'. Type /? for help
>>> /show
Available Commands:
  /show info         Show details for this model
  /show license      Show model license
  /show modelfile    Show Modelfile for this model
  /show parameters   Show parameters for this model
  /show system       Show system message
  /show template     Show prompt template

>>> /show modelfile
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM gemma-2-9b-it:latest

FROM C:\Users\jazzw\.ollama\models\blobs\sha256-2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403
TEMPLATE """{{- $system := "" }}
{{- range .Messages }}
{{- if eq .Role "system" }}
{{- if not $system }}{{ $system = .Content }}
{{- else }}{{ $system = printf "%s\n\n%s" $system .Content }}
{{- end }}
{{- continue }}
{{- else if eq .Role "user" }}<start_of_turn>user
{{- if $system }}
{{ $system }}
{{- $system = "" }}
{{- end }}
{{- else if eq .Role "assistant" }}<start_of_turn>model
{{- end }}
{{ .Content }}<end_of_turn>
{{ end }}<start_of_turn>model
"""
PARAMETER stop <start_of_turn>
PARAMETER stop <end_of_turn>

>>>
>>> Send a message (/? for help)
```
- 蠻特別的，自動從 GGUF 檔中，偵測到 Template `gemma-instruct`

```bash
using autodetected template gemma-instruct
```

- ( 2025-01-14 21:46:10 )
- `ollama start` 的 log - 可以看到 GGUF 原始 Model 的 metadata
```bash
[GIN] 2025/01/14 - 21:42:14 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/14 - 21:42:14 | 200 |       539.3µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/01/14 - 21:42:37 | 200 |       519.8µs |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/14 - 21:42:49 | 201 |    8.3508931s |       127.0.0.1 | POST     "/api/blobs/sha256:2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403"
[GIN] 2025/01/14 - 21:42:49 | 200 |    107.1596ms |       127.0.0.1 | POST     "/api/create"
[GIN] 2025/01/14 - 21:42:55 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/14 - 21:42:55 | 200 |      1.0702ms |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/01/14 - 21:43:07 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/14 - 21:43:07 | 200 |     46.8456ms |       127.0.0.1 | POST     "/api/show"
time=2025-01-14T21:43:08.599+08:00 level=INFO source=sched.go:714 msg="new model will fit in available VRAM in single GPU, loading" model=C:\Users\jazzw\.ollama\models\blobs\sha256-2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403 gpu=GPU-e8624b08-30b4-9c97-b054-cf2ed44d5da2 parallel=1 available=7443841024 required="5.2 GiB"
time=2025-01-14T21:43:08.628+08:00 level=INFO source=server.go:104 msg="system memory" total="31.2 GiB" free="16.2 GiB" free_swap="14.1 GiB"
time=2025-01-14T21:43:08.629+08:00 level=INFO source=memory.go:356 msg="offload to cuda" layers.requested=-1 layers.model=43 layers.offload=43 layers.split="" memory.available="[6.9 GiB]" memory.gpu_overhead="0 B" memory.required.full="5.2 GiB" memory.required.partial="5.2 GiB" memory.required.kv="672.0 MiB" memory.required.allocations="[5.2 GiB]" memory.weights.total="3.5 GiB" memory.weights.repeating="2.8 GiB" memory.weights.nonrepeating="717.8 MiB" memory.graph.full="507.0 MiB" memory.graph.partial="1.2 GiB"
time=2025-01-14T21:43:08.638+08:00 level=INFO source=server.go:376 msg="starting llama server" cmd="C:\\Users\\jazzw\\scoop\\apps\\ollama\\current\\lib\\ollama\\runners\\cuda_v12_avx\\ollama_llama_server.exe runner --model C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403 --ctx-size 2048 --batch-size 512 --n-gpu-layers 43 --threads 8 --no-mmap --parallel 1 --port 53122"
time=2025-01-14T21:43:08.696+08:00 level=INFO source=sched.go:449 msg="loaded runners" count=1
time=2025-01-14T21:43:08.696+08:00 level=INFO source=server.go:555 msg="waiting for llama runner to start responding"
time=2025-01-14T21:43:08.697+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server error"
time=2025-01-14T21:43:09.092+08:00 level=INFO source=runner.go:945 msg="starting go runner"
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 4060 Laptop GPU, compute capability 8.9, VMM: yes
time=2025-01-14T21:43:09.751+08:00 level=INFO source=runner.go:946 msg=system info="CUDA : ARCHS = 600,610,620,700,720,750,800,860,870,890,900 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | LLAMAFILE = 1 | AARCH64_REPACK = 1 | cgo(clang)" threads=8
time=2025-01-14T21:43:09.753+08:00 level=INFO source=.:0 msg="Server listening on 127.0.0.1:53122"
time=2025-01-14T21:43:09.979+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server loading model"
llama_load_model_from_file: using device CUDA0 (NVIDIA GeForce RTX 4060 Laptop GPU) - 7099 MiB free
llama_model_loader: loaded meta data with 33 key-value pairs and 464 tensors from C:\Users\jazzw\.ollama\models\blobs\sha256-2efce51c0d774a47c247c07ec6f109f670e3da4f4eec0f9322d72e3635622403 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = gemma2
llama_model_loader: - kv   1:                               general.name str              = gemma-2-9b-it
llama_model_loader: - kv   2:                      gemma2.context_length u32              = 8192
llama_model_loader: - kv   3:                    gemma2.embedding_length u32              = 3584
llama_model_loader: - kv   4:                         gemma2.block_count u32              = 42
llama_model_loader: - kv   5:                 gemma2.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                gemma2.attention.head_count u32              = 16
llama_model_loader: - kv   7:             gemma2.attention.head_count_kv u32              = 8
llama_model_loader: - kv   8:    gemma2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv   9:                gemma2.attention.key_length u32              = 256
llama_model_loader: - kv  10:              gemma2.attention.value_length u32              = 256
llama_model_loader: - kv  11:                          general.file_type u32              = 10
llama_model_loader: - kv  12:              gemma2.attn_logit_softcapping f32              = 50.000000
llama_model_loader: - kv  13:             gemma2.final_logit_softcapping f32              = 30.000000
llama_model_loader: - kv  14:            gemma2.attention.sliding_window u32              = 4096
llama_model_loader: - kv  15:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  16:                         tokenizer.ggml.pre str              = default
llama_model_loader: - kv  17:                      tokenizer.ggml.tokens arr[str,256000]  = ["<pad>", "<eos>", "<bos>", "<unk>", ...
llama_model_loader: - kv  18:                      tokenizer.ggml.scores arr[f32,256000]  = [-1000.000000, -1000.000000, -1000.00...
llama_model_loader: - kv  19:                  tokenizer.ggml.token_type arr[i32,256000]  = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  20:                tokenizer.ggml.bos_token_id u32              = 2
llama_model_loader: - kv  21:                tokenizer.ggml.eos_token_id u32              = 1
llama_model_loader: - kv  22:            tokenizer.ggml.unknown_token_id u32              = 3
llama_model_loader: - kv  23:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  24:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  25:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  26:                    tokenizer.chat_template str              = {{ bos_token }}{% if messages[0]['rol...
llama_model_loader: - kv  27:            tokenizer.ggml.add_space_prefix bool             = false
llama_model_loader: - kv  28:               general.quantization_version u32              = 2
llama_model_loader: - kv  29:                      quantize.imatrix.file str              = /models_out/gemma-2-9b-it-GGUF/gemma-...
llama_model_loader: - kv  30:                   quantize.imatrix.dataset str              = /training_dir/calibration_datav3.txt
llama_model_loader: - kv  31:             quantize.imatrix.entries_count i32              = 294
llama_model_loader: - kv  32:              quantize.imatrix.chunks_count i32              = 128
llama_model_loader: - type  f32:  169 tensors
llama_model_loader: - type q2_K:  168 tensors
llama_model_loader: - type q3_K:  126 tensors
llama_model_loader: - type q6_K:    1 tensors
llm_load_vocab: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
llm_load_vocab: special tokens cache size = 217
llm_load_vocab: token to piece cache size = 1.6014 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = gemma2
llm_load_print_meta: vocab type       = SPM
llm_load_print_meta: n_vocab          = 256000
llm_load_print_meta: n_merges         = 0
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 8192
llm_load_print_meta: n_embd           = 3584
llm_load_print_meta: n_layer          = 42
llm_load_print_meta: n_head           = 16
llm_load_print_meta: n_head_kv        = 8
llm_load_print_meta: n_rot            = 256
llm_load_print_meta: n_swa            = 4096
llm_load_print_meta: n_embd_head_k    = 256
llm_load_print_meta: n_embd_head_v    = 256
llm_load_print_meta: n_gqa            = 2
llm_load_print_meta: n_embd_k_gqa     = 2048
llm_load_print_meta: n_embd_v_gqa     = 2048
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-06
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 14336
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 2
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 10000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 8192
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 9B
llm_load_print_meta: model ftype      = Q2_K - Medium
llm_load_print_meta: model params     = 9.24 B
llm_load_print_meta: model size       = 3.54 GiB (3.29 BPW)
llm_load_print_meta: general.name     = gemma-2-9b-it
llm_load_print_meta: BOS token        = 2 '<bos>'
llm_load_print_meta: EOS token        = 1 '<eos>'
llm_load_print_meta: EOT token        = 107 '<end_of_turn>'
llm_load_print_meta: UNK token        = 3 '<unk>'
llm_load_print_meta: PAD token        = 0 '<pad>'
llm_load_print_meta: LF token         = 227 '<0x0A>'
llm_load_print_meta: EOG token        = 1 '<eos>'
llm_load_print_meta: EOG token        = 107 '<end_of_turn>'
llm_load_print_meta: max token length = 48
llm_load_tensors: offloading 42 repeating layers to GPU
llm_load_tensors: offloading output layer to GPU
llm_load_tensors: offloaded 43/43 layers to GPU
llm_load_tensors:          CPU model buffer size =   717.77 MiB
llm_load_tensors:        CUDA0 model buffer size =  3623.33 MiB
llama_new_context_with_model: n_seq_max     = 1
llama_new_context_with_model: n_ctx         = 2048
llama_new_context_with_model: n_ctx_per_seq = 2048
llama_new_context_with_model: n_batch       = 512
llama_new_context_with_model: n_ubatch      = 512
llama_new_context_with_model: flash_attn    = 0
llama_new_context_with_model: freq_base     = 10000.0
llama_new_context_with_model: freq_scale    = 1
llama_new_context_with_model: n_ctx_per_seq (2048) < n_ctx_train (8192) -- the full capacity of the model will not be utilized
llama_kv_cache_init:      CUDA0 KV buffer size =   672.00 MiB
llama_new_context_with_model: KV self size  =  672.00 MiB, K (f16):  336.00 MiB, V (f16):  336.00 MiB
llama_new_context_with_model:  CUDA_Host  output buffer size =     0.99 MiB
llama_new_context_with_model:      CUDA0 compute buffer size =   507.00 MiB
llama_new_context_with_model:  CUDA_Host compute buffer size =    15.01 MiB
llama_new_context_with_model: graph nodes  = 1690
llama_new_context_with_model: graph splits = 2
time=2025-01-14T21:43:11.766+08:00 level=INFO source=server.go:594 msg="llama runner started in 3.07 seconds"
```
## Gemma 3

### 2025-03-13

- 火熱登場 -- Gemma 3
- LM Studio
  - https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF
- 因為 ollama 直接下載要很久，用 wget 比較快
```bash
jazzw@JazzBook:~/.ollama$ ollama run hf.co/lmstudio-community/gemma-3-12b-it-GGUF:Q4_K_M
```
```bash
jazzw@JazzBook:~/.ollama$ wget https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF/resolve/main/gemma-3-12b-it-Q4_K_M.gguf
```
- https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF/blob/main/gemma-3-12b-it-Q4_K_M.gguf
  - Size of remote file: 7.3 GB

### 2025-03-14

- get Gemma 3 modelfile from Github Codespace `codespaces-blank` (用 Codespace 下載 GGUF 模型檔網路速度比較快，雖然跑不動，但方便可以拿來觀察不同的開源 LLM 模型)
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ ollama show hf.co/lmstudio-community/gemma-3-12b-it-GGUF:Q4_K_M --modelfile
[GIN] 2025/03/14 - 04:00:10 | 200 |     700.959µs |       127.0.0.1 | HEAD     "/"
[GIN] 2025/03/14 - 04:00:10 | 200 |   52.140362ms |       127.0.0.1 | POST     "/api/show"
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM hf.co/lmstudio-community/gemma-3-12b-it-GGUF:Q4_K_M

FROM /home/codespace/.ollama/models/blobs/sha256-9610e3e07375303f6cd89086b496bcc1ab581177f52042eff536475a29283ba2
FROM /home/codespace/.ollama/models/blobs/sha256-30c02d056410848227001830866e0a269fcc28aaf8ca971bded494003de9f5a5
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 }}
{{- if or (eq .Role "user") (eq .Role "system") }}<start_of_turn>user
{{ .Content }}<end_of_turn>
{{ if $last }}<start_of_turn>model
{{ end }}
{{- else if eq .Role "assistant" }}<start_of_turn>model
{{ .Content }}{{ if not $last }}<end_of_turn>
{{ end }}
{{- end }}
{{- end }}"""
PARAMETER stop <end_of_turn>
PARAMETER temperature 0.1
```
- ( 2025-03-14 12:05:01 )
- 匯入筆電 Ollama
```bash
jazzw@JazzBook:~/.ollama$ ls -al
total 7129515
drwxr-xr-x 1 jazzw 197609          0 三月   14 11:58 .
drwxr-xr-x 1 jazzw 197609          0 三月   14 12:03 ..
-rw-r--r-- 1 jazzw 197609        461 三月   14 11:58 gemma-3-12b-it-q4_k_m
-rw-r--r-- 1 jazzw 197609 7300574976 三月   12 21:36 gemma-3-12b-it-Q4_K_M.gguf
-rw-r--r-- 1 jazzw 197609       1526 三月    8 13:56 history
-rw-r--r-- 1 jazzw 197609        387 十二月 26 23:21 id_ed25519
-rw-r--r-- 1 jazzw 197609         81 十二月 26 23:21 id_ed25519.pub
drwxr-xr-x 1 jazzw 197609          0 三月    8 12:34 models
-rw-r--r-- 1 jazzw 197609       1630 三月    8 13:53 qwen25-7b-instruct-1m-q4_k_m
FROM gemma-3-12b-it-Q4_K_M.gguf
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 }}
{{- if or (eq .Role "user") (eq .Role "system") }}<start_of_turn>user
{{ .Content }}<end_of_turn>
{{ if $last }}<start_of_turn>model
{{ end }}
{{- else if eq .Role "assistant" }}<start_of_turn>model
{{ .Content }}{{ if not $last }}<end_of_turn>
{{ end }}
{{- end }}
{{- end }}"""
PARAMETER stop <end_of_turn>
PARAMETER temperature 0.1
jazzw@JazzBook:~/.ollama$ ollama create gemma-3-12b-it:q4_k_m -f gemma-3-12b-it-q4_k_m
gathering model components
copying file sha256:9610e3e07375303f6cd89086b496bcc1ab581177f52042eff536475a29283ba2 100%
parsing GGUF
using existing layer sha256:9610e3e07375303f6cd89086b496bcc1ab581177f52042eff536475a29283ba2
creating new layer sha256:e0a42594d802e5d31cdc786deb4823edb8adff66094d49de8fffe976d753e348
creating new layer sha256:0a74a8735bf3ffff4537b6c6bc9a4bc97a28c48f2fd347e806cca4d5001560f6
writing manifest
success
jazzw@JazzBook:~/.ollama$ ollama list
NAME                            ID              SIZE      MODIFIED
gemma-3-12b-it:q4_k_m           56a4b304a208    7.3 GB    38 seconds ago
qwen25-7b-instruct-1m:q4_k_m    80b818033c9f    4.7 GB    5 days ago
qwen2.5-coder:latest            2b0496514337    4.7 GB    2 weeks ago
deepseek-r1:8b                  28f8fd6cdc67    4.9 GB    5 weeks ago
```
- 先觀察一下 context window 大小 - Gemma 3 => `131K` tokens
```bash
jazzw@JazzBook:~/.ollama$ ollama show gemma-3-12b-it:q4_k_m
  Model
    architecture        gemma3
    parameters          11.8B
    context length      131072
    embedding length    3840
    quantization        Q4_K_M

  Parameters
    stop           "<end_of_turn>"
    temperature    0.1

```
- 來測試一下 Gemma 3 的程式解析能力
```bash
jazzw@JazzBook:~/git/xxxx/YYYYY$ export OLLAMA_API_BASE=http://127.0.0.1:11434
jazzw@JazzBook:~/git/xxxx/YYYYY$ aider --model ollama/gemma-3-12b-it:q4_k_m *.pm *.pl
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
You can skip this check with --no-gitignore
Add .aider* to .gitignore (recommended)? (Y)es/(N)o [Yes]:
Added .aider* to .gitignore
Can not create C:\Users\jazzw\git\xxxx\YYYYY\*.pm, skipping.
Aider v0.75.1
Model: ollama/gemma-3-12b-it:q4_k_m with whole edit format
Git repo: .git with 7 files
Repo-map: using 4096 tokens, auto refresh
Added YYYYY_feed.pl to the chat.
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
YYYYY_feed.pl
> /tokens


Approximate context window usage for ollama/gemma-3-12b-it:q4_k_m, in tokens:

$ 0.0000      463 system messages
$ 0.0000       77 repository map  use --map-tokens to resize
$ 0.0000    9,411 YYYYY_feed.pl   /drop to remove
==================
$ 0.0000    9,951 tokens total
          121,121 tokens remaining in context window
          131,072 tokens max context window size
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
YYYYY_feed.pl
> /ask could you give me a high-level overview of this code base?

litellm.APIConnectionError: OllamaException - {"error":"llama runner process has terminated: this model is not supported by your version of Ollama. You may need to upgrade"}
Retrying in 0.2 seconds...
litellm.APIConnectionError: OllamaException - {"error":"llama runner process has terminated: this model is not supported by your version of Ollama. You may need to upgrade"}
Retrying in 0.5 seconds...
litellm.APIConnectionError: OllamaException - {"error":"llama runner process has terminated: this model is not supported by your version of Ollama. You may need to upgrade"}
Retrying in 1.0 seconds...
litellm.APIConnectionError: OllamaException - {"error":"llama runner process has terminated: this model is not supported by your version of Ollama. You may need to upgrade"}
Retrying in 2.0 seconds...
litellm.APIConnectionError: OllamaException - {"error":"llama runner process has terminated: this model is not supported by your version of Ollama. You may need to upgrade"}
Retrying in 4.0 seconds...

^C again to exit
```
- 好吧～ Ollama 還沒支援 Gemma 3 (太新了) -- 除非改用 LM Studio (畢竟我是在 LM Studio 找到的模型 HuggingFace 網址)

### 2025-03-15

- ( 2025-03-15 01:07:05 )
- upgrade ollama to `0.6.0`
```bash
jazzw@JazzBook:~/git/snippet$ scoop info ollama


Name        : ollama
Description : Get up and running with large language models locally.
Version     : 0.6.0
Bucket      : main
Website     : https://ollama.com
License     : MIT
Updated at  : 3/12/2025 4:30:03 PM
Updated by  : github-actions[bot]
Installed   : 0.6.0
Binaries    : ollama.exe
Suggestions : extras/ollama-full
Notes       : Ollama with deamon has been moved to 'extras/ollama-full'.
```
- ( 2025-03-15 01:07:45 )
```bash
jazzw@JazzBook:~/git/snippet$ ollama start
jazzw@JazzBook:~/git/snippet$ ollama run gemma-3-12b-it:q4_k_m
>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.

>>> /show
Available Commands:
  /show info         Show details for this model
  /show license      Show model license
  /show modelfile    Show Modelfile for this model
  /show parameters   Show parameters for this model
  /show system       Show system message
  /show template     Show prompt template

>>> /show info
  Model
    architecture        gemma3
    parameters          11.8B
    context length      131072
    embedding length    3840
    quantization        Q4_K_M

  Parameters
    stop           "<end_of_turn>"
    temperature    0.1

>>> /show modelfile
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM gemma-3-12b-it:q4_k_m

FROM C:\Users\jazzw\.ollama\models\blobs\sha256-9610e3e07375303f6cd89086b496bcc1ab581177f52042eff536475a29283ba2
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 }}
{{- if or (eq .Role "user") (eq .Role "system") }}<start_of_turn>user
{{ .Content }}<end_of_turn>
{{ if $last }}<start_of_turn>model
{{ end }}
{{- else if eq .Role "assistant" }}<start_of_turn>model
{{ .Content }}{{ if not $last }}<end_of_turn>
{{ end }}
{{- end }}
{{- end }}"""
PARAMETER stop <end_of_turn>
PARAMETER temperature 0.1

>>> /bye
```
- ( 2025-03-15 01:21:13 )
```bash
jazzw@JazzBook:~/git/xxxx/YYYYY$ aider --model ollama/gemma-3-12b-it:q4_k_m YYYYY_feed.pl
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.75.1
Model: ollama/gemma-3-12b-it:q4_k_m with whole edit format
Git repo: .git with 7 files
Repo-map: using 4096 tokens, auto refresh
Added YYYYY_feed.pl to the chat.
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
YYYYY_feed.pl
> /token

Approximate context window usage for ollama/gemma-3-12b-it:q4_k_m, in tokens:

$ 0.0000      463 system messages
$ 0.0000       77 repository map  use --map-tokens to resize
$ 0.0000    9,411 YYYYY_feed.pl   /drop to remove
==================
$ 0.0000    9,951 tokens total
          121,121 tokens remaining in context window
          131,072 tokens max context window size
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
YYYYY_feed.pl
> /ask cloud you give me a high-level overview of this code base?

litellm.APIConnectionError: Ollama Error - {'error': 'POST predict: Post "http://127.0.0.1:54036/completion": read tcp 127.0.0.1:54038->127.0.0.1:54036: wsarecv: An existing connection was forcibly closed by
the remote host.'}
Traceback (most recent call last):
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\litellm_core_utils\streaming_handler.py", line 1420, in __next__
    chunk = next(self.completion_stream)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\base_llm\base_model_iterator.py", line 74, in __next__
    return self._handle_string_chunk(str_line=str_line)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 390, in _handle_string_chunk
    return self.chunk_parser(json.loads(str_line))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 431, in chunk_parser
    raise e
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 395, in chunk_parser
    raise Exception(f"Ollama Error - {chunk}")
Exception: Ollama Error - {'error': 'POST predict: Post "http://127.0.0.1:54036/completion": read tcp 127.0.0.1:54038->127.0.0.1:54036: wsarecv: An existing connection was forcibly closed by the remote host.'}

Retrying in 0.2 seconds...
litellm.APIConnectionError: Ollama Error - {'error': 'POST predict: Post "http://127.0.0.1:54043/completion": read tcp 127.0.0.1:54045->127.0.0.1:54043: wsarecv: An existing connection was forcibly closed by
the remote host.'}
Traceback (most recent call last):
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\litellm_core_utils\streaming_handler.py", line 1420, in __next__
    chunk = next(self.completion_stream)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\base_llm\base_model_iterator.py", line 74, in __next__
    return self._handle_string_chunk(str_line=str_line)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 390, in _handle_string_chunk
    return self.chunk_parser(json.loads(str_line))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 431, in chunk_parser
    raise e
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Lib\site-packages\litellm\llms\ollama\completion\transformation.py", line 395, in chunk_parser
    raise Exception(f"Ollama Error - {chunk}")
Exception: Ollama Error - {'error': 'POST predict: Post "http://127.0.0.1:54043/completion": read tcp 127.0.0.1:54045->127.0.0.1:54043: wsarecv: An existing connection was forcibly closed by the remote host.'}

Retrying in 0.5 seconds...
```
- 還是失敗，看起來可以用 `ollama run` 可是不能整合 `aider`

### 2025-03-18

### Cloud Run

- 2025-03-12: [How to deploy serverless AI with Gemma 3 on Cloud Run](https://cloud.google.com/blog/products/ai-machine-learning/serverless-ai-with-gemma-3-on-cloud-run)
- Run LLM inference on Cloud Run GPUs with Ollama 
  - https://cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama
- Run LLM inference on Cloud Run GPUs with vLLM 
  - https://cloud.google.com/run/docs/tutorials/gpu-gemma2-with-vllm
- Run LLM inference on Cloud Run GPUs with Hugging Face TGI 
  - https://cloud.google.com/run/docs/tutorials/gpu-llama3-with-tgi
- Best practices: AI inference on Cloud Run with GPUs 
  - https://cloud.google.com/run/docs/configuring/services/gpu-best-practices
- GPU support for services 
  - https://cloud.google.com/run/docs/configuring/services/gpu
- 2024-08-22: How to run LLM inference on Cloud Run GPUs with vLLM and the OpenAI Python SDK
  - https://codelabs.developers.google.com/codelabs/how-to-run-inference-cloud-run-gpu-vllm#0

### News

- 2025-03-12: Gemma 3 Tech Report
  - https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf
- 2025-03-12: [Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM](https://huggingface.co/blog/gemma3)
- https://huggingface.co/ggml-org/gemma-3-12b-it-GGUF/tree/main

### 2025-03-20

- 根據 https://huggingface.co/google/gemma-3-12b-it#usage ，若要用 `transformer` 跑，得要裝特殊的版本

> ### Usage
> Below, there are some code snippets on how to get quickly started with running the model. First, install the Transformers library with the version made for Gemma 3:
> ```
> $ pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3
> ```
> Then, copy the snippet from the section that is relevant for your use case.

## Gemma 3 QAT

- 2025-04-18: Gemma 3 QAT Models: Bringing state-of-the-Art AI to consumer GPUs
  - https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/
- https://huggingface.co/collections/google/gemma-3-qat-67ee61ccacbf2be4195c265b

### 2025-05-05

- 想測一下這個針對 Coding 的 Gemma 3 fine-tune，可惜是 12B 的，縱使轉成 GGUF 本機應該還是跑不動。
  - https://huggingface.co/burtenshaw/GemmaCoder3-12B
- 另外，這個 4B 的 Speech 語音模型也挺有趣的
  - https://huggingface.co/junnei/gemma-3-4b-it-speech

### 2025-05-09

- ( 2025-05-09 00:18:59 )
```bash
~/.ollama$ wget -c https://huggingface.co/lmstudio-community/gemma-3-4B-it-qat-GGUF/resolve/main/gemma-3-4B-it-QAT-Q4_0.gguf
~/.ollama$ cat gemma-3-4B-it-qat-q4_0
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM hf.co/lmstudio-community/gemma-3-4B-it-qat-GGUF:Q4_0
# Download with wget
# ```
# wget -c https://huggingface.co/lmstudio-community/gemma-3-4B-it-qat-GGUF/resolve/main/gemma-3-4B-it-QAT-Q4_0.gguf
# ```
FROM gemma-3-4B-it-QAT-Q4_0.gguf

TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 }}
{{- if or (eq .Role "user") (eq .Role "system") }}<start_of_turn>user
{{ .Content }}<end_of_turn>
{{ if $last }}<start_of_turn>model
{{ end }}
{{- else if eq .Role "assistant" }}<start_of_turn>model
{{ .Content }}{{ if not $last }}<end_of_turn>
{{ end }}
{{- end }}
{{- end }}"""
PARAMETER stop <end_of_turn>
PARAMETER temperature 0.1
~/.ollama$ ollama create gemma-3-4b-it-qat:q4_0 -f gemma-3-4B-it-qat-q4_0
```
- ( 2025-05-09 00:21:03 )
- 裝最新版 aider 也是卡在 `g95` fortran 編譯環境的問題
```
~/git/snippet$ uv tool install aider-chat
Resolved 115 packages in 3.22s
  × Failed to build `scipy==1.13.1`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `mesonpy.build_wheel` failed (exit code: 1)

      [stdout]
      + meson setup C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src
      C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-w0uz42c3
      -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md
      --native-file=C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-w0uz42c3\meson-python-native-file.ini
      The Meson build system
      Version: 1.8.0
      Source dir: C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src
      Build dir: C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-w0uz42c3
      Build type: native build
      Project name: scipy
      Project version: 1.13.1
      C compiler for the host machine: gcc (gcc 13.2.0 "gcc (GCC) 13.2.0")
      C linker for the host machine: gcc ld.bfd 2.41
      C++ compiler for the host machine: g++ (gcc 13.2.0 "g++ (GCC) 13.2.0")
      C++ linker for the host machine: g++ ld.bfd 2.41
      Cython compiler for the host machine: cython (cython 3.0.12)
      Host machine cpu family: x86_64
      Host machine cpu: x86_64
      Program python found: YES (C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpFmRxVE\Scripts\python.exe)
      Run-time dependency python found: YES 3.13
      Program cython found: YES (C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpFmRxVE\Scripts\cython.EXE)
      Compiler for C supports arguments -Wno-unused-but-set-variable: YES
      Compiler for C supports arguments -Wno-unused-function: YES
      Compiler for C supports arguments -Wno-conversion: YES
      Compiler for C supports arguments -Wno-misleading-indentation: YES
      Library m found: YES

      ..\meson.build:78:0: ERROR: Unknown compiler(s): [['ifort'], ['gfortran'], ['flang-new'], ['flang'], ['pgfortran'], ['g95']]
      The following exception(s) were encountered:
      Running `ifort --help` gave "[WinError 2] The system cannot find the file specified"
      Running `ifort --version` gave "[WinError 2] The system cannot find the file specified"
      Running `ifort -V` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran --help` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran --version` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran -V` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new --help` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new --version` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new -V` gave "[WinError 2] The system cannot find the file specified"
      Running `flang --help` gave "[WinError 2] The system cannot find the file specified"
      Running `flang --version` gave "[WinError 2] The system cannot find the file specified"
      Running `flang -V` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran --help` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran --version` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran -V` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 --help` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 --version` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 -V` gave "[WinError 2] The system cannot find the file specified"

      A full log can be found at
      C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-w0uz42c3\meson-logs\meson-log.txt

      hint: This usually indicates a problem with the package or the build environment.
```

### 2025-06-10

- 2025-3-13: Gemma 3: What You Need To Know
  - https://gradientflow.com/gemma-3-what-you-need-to-know/

## Gemma 3n

### 2025-07-26

- 2025-06-26:
  - Introducing Gemma 3n: The developer guide
  - https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/