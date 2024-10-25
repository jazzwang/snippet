# llamafile

> llamafile lets you distribute and run LLMs with a single file.

- 2023-11-29 : Introducing llamafile https://hacks.mozilla.org/2023/11/introducing-llamafile/

- Git Repo: https://github.com/Mozilla-Ocho/llamafile

## 2024-10-25

- 先前在 reddit 看到關於 llamafile 的相關討論。
- 2024-10-23 看到微軟 BitNet 這個 1-bit LLM，一直都不是很了解 `Quantization` 到底影響的是 "Model Training" 還是 "Model Serving"?
- 可以確定的是 llamafile 是整合 `llama.cpp`，用 [Cosmopolitan Libc](https://github.com/jart/cosmopolitan) 讓編譯出來的 llamafile 可以在不同 CPU 架構上運行。是個蠻有趣的想法，可以單一檔案在 x84_64 , arm64 CPU 架構運行的 Windows, Linux, macOS, BSD 運行的執行檔。

- ( 2024-10-25 16:52:19 )
- 使用 Github CodeSpace 測試一下。
```bash
jazzw@JazzBook:~$ gh cs ssh
? Choose codespace: jazzwang/snippet (master*): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Fri Oct 25 08:42:24 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $
```
- 先確認一下硬體架構。
  - CPU 是 `AMD EPYC 7763 64-Core Processor` (x86_64)
```bash
@jazzwang ➜ /workspaces/snippet (master) $ lscpu
Architecture:                       x86_64
CPU op-mode(s):                     32-bit, 64-bit
Byte Order:                         Little Endian
Address sizes:                      48 bits physical, 48 bits virtual
CPU(s):                             2
On-line CPU(s) list:                0,1
Thread(s) per core:                 2
Core(s) per socket:                 1
Socket(s):                          1
NUMA node(s):                       1
Vendor ID:                          AuthenticAMD
CPU family:                         25
Model:                              1
Model name:                         AMD EPYC 7763 64-Core Processor
Stepping:                           1
CPU MHz:                            2959.848
BogoMIPS:                           4890.86
Virtualization:                     AMD-V
Hypervisor vendor:                  Microsoft
Virtualization type:                full
L1d cache:                          32 KiB
L1i cache:                          32 KiB
L2 cache:                           512 KiB
L3 cache:                           32 MiB
NUMA node0 CPU(s):                  0,1
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Vulnerable: Safe RET, no microcode
Vulnerability Spec store bypass:    Vulnerable
Vulnerability Spectre v1:           Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; Retpolines; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected
Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext f
                                    xsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq
                                     ssse3 fma cx16 pcid sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy a
                                    bm sse4a misalignsse 3dnowprefetch osvw topoext invpcid_single vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed
                                    adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr rdpru arat npt nrip_save tsc_scale vmcb
                                    _clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip vaes vpclmulqdq rdpid fsrm
```
- 記憶體大小 = `8 GB` RAM
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cat /proc/meminfo
MemTotal:        8119864 kB
MemFree:          201424 kB
MemAvailable:    6623776 kB
Buffers:          149292 kB
Cached:          6359096 kB
SwapCached:            0 kB
Active:          2911408 kB
Inactive:        4467664 kB
Active(anon):     924116 kB
Inactive(anon):    15416 kB
Active(file):    1987292 kB
Inactive(file):  4452248 kB
Unevictable:       27844 kB
Mlocked:           27844 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Zswap:                 0 kB
Zswapped:              0 kB
Dirty:               400 kB
Writeback:             0 kB
AnonPages:        878392 kB
Mapped:           476528 kB
Shmem:             59752 kB
KReclaimable:     296128 kB
Slab:             379572 kB
SReclaimable:     296128 kB
SUnreclaim:        83444 kB
KernelStack:        5408 kB
PageTables:        12504 kB
SecPageTables:         0 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     4059932 kB
Committed_AS:    2423868 kB
VmallocTotal:   34359738367 kB
VmallocUsed:       39384 kB
VmallocChunk:          0 kB
Percpu:             1144 kB
HardwareCorrupted:     0 kB
AnonHugePages:    407552 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
Unaccepted:            0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:      118720 kB
DirectMap2M:     4075520 kB
DirectMap1G:     6291456 kB
```
- 應該是沒有 GPU，所以沒有 VRAM
- ( 2024-10-25 16:57:54 )
- 首先下載 Download llava-v1.5-7b-q4.llamafile (4.29 GB).
```bash
@jazzwang ➜ /workspaces/snippet (master) $ wget -O llava-v1.5-7b-q4 "https://huggingface.co/Mozilla/llava-v1.5-7b-llamafile/resolve/main/llava-v1.5-7b-q4.llamafile?download=true"

Length: 4288297357 (4.0G) [binary/octet-stream]
Saving to: ‘llava-v1.5-7b-q4’

llava-v1.5-7b-q4                                82%[==================================================================================>                  ]   3.31G  40.1MB/s    eta 17s
```
- 改成可執行檔
```bash
@jazzwang ➜ /workspaces/snippet (master) $ chmod a+x llava-v1.5-7b-q4
@jazzwang ➜ /workspaces/snippet (master) $ ./llava-v1.5-7b-q4
note: if you have an AMD or NVIDIA GPU then you need to pass -ngl 9999 to enable GPU offloading
{"build":1500,"commit":"a30b324","function":"server_cli","level":"INFO","line":2869,"msg":"build info","tid":"10437056","timestamp":1729847059}
{"function":"server_cli","level":"INFO","line":2872,"msg":"system info","n_threads":1,"n_threads_batch":-1,"system_info":"AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 | LLAMAFILE = 1 | ","tid":"10437056","timestamp":1729847059,"total_threads":2}
{"function":"load_model","level":"INFO","line":435,"msg":"Multi Modal Mode Enabled","tid":"10437056","timestamp":1729847059}
clip_model_load: model name:   openai/clip-vit-large-patch14-336
clip_model_load: description:  image encoder for LLaVA
clip_model_load: GGUF version: 3
clip_model_load: alignment:    32
clip_model_load: n_tensors:    377
clip_model_load: n_kv:         19
clip_model_load: ftype:        q4_0
clip_model_load: loaded meta data with 19 key-value pairs and 377 tensors from llava-v1.5-7b-mmproj-Q4_0.gguf
clip_model_load: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
clip_model_load: - kv   0:                       general.architecture str              = clip
clip_model_load: - kv   1:                      clip.has_text_encoder bool             = false
clip_model_load: - kv   2:                    clip.has_vision_encoder bool             = true
clip_model_load: - kv   3:                   clip.has_llava_projector bool             = true
clip_model_load: - kv   4:                          general.file_type u32              = 2
clip_model_load: - kv   5:                               general.name str              = openai/clip-vit-large-patch14-336
clip_model_load: - kv   6:                        general.description str              = image encoder for LLaVA
clip_model_load: - kv   7:                     clip.vision.image_size u32              = 336
clip_model_load: - kv   8:                     clip.vision.patch_size u32              = 14
clip_model_load: - kv   9:               clip.vision.embedding_length u32              = 1024
clip_model_load: - kv  10:            clip.vision.feed_forward_length u32              = 4096
clip_model_load: - kv  11:                 clip.vision.projection_dim u32              = 768
clip_model_load: - kv  12:           clip.vision.attention.head_count u32              = 16
clip_model_load: - kv  13:   clip.vision.attention.layer_norm_epsilon f32              = 0.000010
clip_model_load: - kv  14:                    clip.vision.block_count u32              = 23
clip_model_load: - kv  15:                     clip.vision.image_mean arr[f32,3]       = [0.481455, 0.457828, 0.408211]
clip_model_load: - kv  16:                      clip.vision.image_std arr[f32,3]       = [0.268630, 0.261303, 0.275777]
clip_model_load: - kv  17:                              clip.use_gelu bool             = false
clip_model_load: - kv  18:               general.quantization_version u32              = 2
clip_model_load: - type  f32:  235 tensors
clip_model_load: - type  f16:    1 tensors
clip_model_load: - type q4_0:  141 tensors
clip_model_load: CLIP using CPU backend
clip_model_load: text_encoder:   0
clip_model_load: vision_encoder: 1
clip_model_load: llava_projector:  1
clip_model_load: model size:     169.18 MB
clip_model_load: metadata size:  0.17 MB
clip_model_load: params backend buffer size =  169.18 MB (377 tensors)
clip_model_load: compute allocated memory: 32.89 MB
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from llava-v1.5-7b-Q4_K.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
llama_model_loader: - kv   2:                       llama.context_length u32              = 4096
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 11008
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 32
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                          general.file_type u32              = 15
llama_model_loader: - kv  11:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,32000]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  13:                      tokenizer.ggml.scores arr[f32,32000]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  14:                  tokenizer.ggml.token_type arr[i32,32000]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 2
llama_model_loader: - kv  17:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
llm_load_vocab: special tokens definition check successful ( 259/32000 ).
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = llama
llm_load_print_meta: vocab type       = SPM
llm_load_print_meta: n_vocab          = 32000
llm_load_print_meta: n_merges         = 0
llm_load_print_meta: n_ctx_train      = 4096
llm_load_print_meta: n_embd           = 4096
llm_load_print_meta: n_head           = 32
llm_load_print_meta: n_head_kv        = 32
llm_load_print_meta: n_layer          = 32
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 1
llm_load_print_meta: n_embd_k_gqa     = 4096
llm_load_print_meta: n_embd_v_gqa     = 4096
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 11008
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 10000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_yarn_orig_ctx  = 4096
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: model type       = 7B
llm_load_print_meta: model ftype      = Q4_K - Medium
llm_load_print_meta: model params     = 6.74 B
llm_load_print_meta: model size       = 3.80 GiB (4.84 BPW)
llm_load_print_meta: general.name     = LLaMA v2
llm_load_print_meta: BOS token        = 1 '<s>'
llm_load_print_meta: EOS token        = 2 '</s>'
llm_load_print_meta: UNK token        = 0 '<unk>'
llm_load_print_meta: PAD token        = 0 '<unk>'
llm_load_print_meta: LF token         = 13 '<0x0A>'
llm_load_tensors: ggml ctx size =    0.17 MiB
llm_load_tensors:        CPU buffer size =  3891.24 MiB
..................................................................................................
llama_new_context_with_model: n_ctx      = 2048
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 10000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:        CPU KV buffer size =  1024.00 MiB
llama_new_context_with_model: KV self size  = 1024.00 MiB, K (f16):  512.00 MiB, V (f16):  512.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.14 MiB
llama_new_context_with_model:        CPU compute buffer size =   164.01 MiB
llama_new_context_with_model: graph nodes  = 1030
llama_new_context_with_model: graph splits = 1
{"function":"initialize","level":"INFO","line":489,"msg":"initializing slots","n_slots":1,"tid":"10437056","timestamp":1729847071}
{"function":"initialize","level":"INFO","line":498,"msg":"new slot","n_ctx_slot":2048,"slot_id":0,"tid":"10437056","timestamp":1729847071}
{"function":"server_cli","level":"INFO","line":3090,"msg":"model loaded","tid":"10437056","timestamp":1729847071}

llama server listening at http://127.0.0.1:8080

opening browser tab... (pass --nobrowser to disable)
In the sandboxing block!
{"function":"server_cli","hostname":"127.0.0.1","level":"INFO","line":3213,"msg":"HTTP server listening","port":"8080","tid":"10437056","timestamp":1729847071}
{"function":"update_slots","level":"INFO","line":1659,"msg":"all slots are idle and system prompt is empty, clear the KV cache","tid":"10437056","timestamp":1729847071}
failed to open http://127.0.0.1:8080/ in a browser tab using xdg-open: No such file or directory
```
- ( 2024-10-25 17:07:33 )
- 透過 Github CodeSpace 的 VS Code 整合，可以開啟 http://127.0.0.1:8080 。會看到 llama.cpp 的 Web UI