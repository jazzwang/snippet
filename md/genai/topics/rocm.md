# AMD ROCm

- https://github.com/ROCm
- Windows
  - https://rocm.docs.amd.com/projects/install-on-windows/en/latest/how-to/install.html
- Linux
  - https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html

## 2025-03-17

- 安裝好 AMD-Software-PRO-Edition-24.Q4-Win10-Win11-For-HIP 以後， `ollama` 顯示有偵測到不支援的 Radeon iGPU，記憶體是 12.2 GiB.
```bash
time=2025-03-17T09:49:31.224+08:00 level=INFO source=amd_windows.go:127 msg="unsupported Radeon iGPU detected skipping" id=0 total="12.2 GiB"
```
- 而 NVidea GPU 相關訊息是
```bash
time=2025-03-17T09:49:30.588+08:00 level=INFO source=gpu.go:319 msg="detected OS VRAM overhead" id=GPU-e8624b08-30b4-9c97-b054-cf2ed44d5da2 library=cuda compute=8.9 driver=12.7 name="NVIDIA GeForce RTX 4060 Laptop GPU" overhead="858.0 MiB"
time=2025-03-17T09:49:31.227+08:00 level=INFO source=types.go:130 msg="inference compute" id=GPU-e8624b08-30b4-9c97-b054-cf2ed44d5da2 library=cuda variant=v12 compute=8.9 driver=12.7 name="NVIDIA GeForce RTX 4060 Laptop GPU" total="8.0 GiB" available="6.9 GiB"
```
```bash
jazzw@JazzBook:~$ ollama start
2025/03/17 09:49:28 routes.go:1230: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:2048 OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\jazzw\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES:]"
time=2025-03-17T09:49:28.886+08:00 level=INFO source=images.go:432 msg="total blobs: 16"
time=2025-03-17T09:49:28.890+08:00 level=INFO source=images.go:439 msg="total unused blobs removed: 0"
time=2025-03-17T09:49:28.893+08:00 level=INFO source=routes.go:1297 msg="Listening on 127.0.0.1:11434 (version 0.6.1)"
time=2025-03-17T09:49:28.893+08:00 level=INFO source=gpu.go:217 msg="looking for compatible GPUs"
time=2025-03-17T09:49:28.893+08:00 level=INFO source=gpu_windows.go:167 msg=packages count=1
time=2025-03-17T09:49:28.893+08:00 level=INFO source=gpu_windows.go:214 msg="" package=0 cores=8 efficiency=0 threads=16
time=2025-03-17T09:49:30.588+08:00 level=INFO source=gpu.go:319 msg="detected OS VRAM overhead" id=GPU-e8624b08-30b4-9c97-b054-cf2ed44d5da2 library=cuda compute=8.9 driver=12.7 name="NVIDIA GeForce RTX 4060 Laptop GPU" overhead="858.0 MiB"
time=2025-03-17T09:49:31.224+08:00 level=INFO source=amd_windows.go:127 msg="unsupported Radeon iGPU detected skipping" id=0 total="12.2 GiB"
time=2025-03-17T09:49:31.227+08:00 level=INFO source=types.go:130 msg="inference compute" id=GPU-e8624b08-30b4-9c97-b054-cf2ed44d5da2 library=cuda variant=v12 compute=8.9 driver=12.7 name="NVIDIA GeForce RTX 4060 Laptop GPU" total="8.0 GiB" available="6.9 GiB"
```

## 2025-08-27

- 2024-09-26
  - Running LLMs Locally on AMD GPUs with Ollama
  - https://www.amd.com/en/developer/resources/technical-articles/running-llms-locally-on-amd-gpus-with-ollama.html