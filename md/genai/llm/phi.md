# Phi

## 2025-01-05

- Phi-4 Technical Report
  - https://arxiv.org/html/2412.08905v1
- Hugging Face Model
  - ttps://huggingface.co/vincentoh/phi-4_f16_ollama
- https://gist.github.com/bigsnarfdude/7754cfb69f94d540da7bda7ef6a910ae
  - 應該是拿來驗證 Phi4 跑 [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://github.com/idavidrein/gpqa) 的測試

## 2025-01-09

- 模型位置：
  - https://huggingface.co/microsoft/phi-4
- Ollama phi4：
  - https://ollama.com/library/phi4
- 試用位置：
  - https://huggingface.co/spaces/akhaliq/anychat

## 2025-01-10

- 狀況：使用 `ollama pull phi4` 下載多次都沒辦法成功
```bash
jazzw@JazzBook:~$ ollama pull phi4
[GIN] 2025/01/10 - 21:50:34 | 200 |       523.9µs |       127.0.0.1 | HEAD     "/"
time=2025-01-10T21:50:36.284+08:00 level=INFO source=download.go:175 msg="downloading fd7b6731c33c in 16 565 MB part(s)"
time=2025-01-10T21:53:29.517+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:53:29.517+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:53:31.517+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:53:31.517+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:40.360+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:56:41.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T21:57:16.100+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 2 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:01:27.343+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 8 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:01:37.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:01:38.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:02:18.006+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 14 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:03:02.558+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 3 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:03:11.344+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:03:11.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:03:11.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:03:12.016+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:03:20.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:03:28.364+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:04:00.031+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 15 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:04:38.967+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 5 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:06:27.363+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:06:27.969+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:06:28.365+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:06:29.456+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:06:30.031+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:07:32.481+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 1 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:08:25.916+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 7 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:08:30.916+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:08:49.156+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 10 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:09:28.208+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 13 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:09:41.916+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:09:42.160+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:09:54.575+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 0 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:10:01.483+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 6 attempt 0 failed: unexpected EOF, retrying in 1s"
time=2025-01-10T22:12:05.868+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 8 attempt 1 failed: unexpected EOF, retrying in 2s"
[GIN] 2025/01/10 - 22:12:06 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/10 - 22:12:06 | 404 |       529.3µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/01/10 - 22:12:12 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/10 - 22:12:12 | 200 |     13.3311ms |       127.0.0.1 | POST     "/api/show"
time=2025-01-10T22:12:51.869+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:52.458+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:54.365+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:54.917+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:55.160+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:55.209+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:55.482+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:55.484+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:55.576+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:12:56.032+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:09.018+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:09.869+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.100+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.160+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.366+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.458+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.484+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:10.576+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:24.918+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:13:58.357+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 3 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:16:07.459+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:09.485+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:09.869+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:09.919+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.019+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.102+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.161+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.358+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.366+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:10.577+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:25.361+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:25.969+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:16:26.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:22.359+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:23.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:23.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:23.366+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:23.577+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:23.970+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:19:36.482+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:21:50.353+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 10 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:21:50.811+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 14 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:21:55.353+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:21:55.812+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:00.515+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 2 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:22:18.092+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 15 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:22:18.228+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 7 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:22:32.142+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 13 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:22:37.148+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:39.359+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:40.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:40.517+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:40.578+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:40.812+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.093+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.229+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.354+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.362+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.367+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.483+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:22:41.970+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:23:53.149+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:24:41.097+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 4 attempt 1 failed: unexpected EOF, retrying in 2s"
time=2025-01-10T22:24:46.098+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:25:22.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:25:26.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:27:21.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:28:59.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:04.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:05.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:05.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:05.348+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:05.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.347+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:06.348+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:14.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:45.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:29:45.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:10.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:10.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:11.348+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:15.353+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:18.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:25.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:30.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:35.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:37.353+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:43.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:43.803+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 7 attempt 0 failed: Get \"https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/fd/fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20250110%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250110T142510Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d67e438e5214a7ff2ab374fa4b088f44e531f1a2ce67a68fc7d030e03c579\": read tcp [2001:b011:7001:12b1:7906:17ba:7c4:4b3c]:57561->[2606:4700:7::12e]:443: wsarecv: An existing connection was forcibly closed by the remote host., retrying in 1s"
time=2025-01-10T22:30:51.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:52.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:56.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:30:59.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:00.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:00.354+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:09.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:12.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:12.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:16.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:17.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:17.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 11 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:17.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:17.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:17.804+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:18.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:18.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:18.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 8 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:18.354+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:19.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:19.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:19.752+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 2 attempt 0 failed: Get \"https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/fd/fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20250110%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250110T142510Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d67e438e5214a7ff2ab374fa4b088f44e531f1a2ce67a68fc7d030e03c579\": read tcp [2001:b011:7001:12b1:7906:17ba:7c4:4b3c]:57619->[2606:4700:7::12e]:443: wsarecv: An existing connection was forcibly closed by the remote host., retrying in 1s"
time=2025-01-10T22:31:19.752+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 6 attempt 0 failed: Get \"https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/fd/fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20250110%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250110T142510Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d67e438e5214a7ff2ab374fa4b088f44e531f1a2ce67a68fc7d030e03c579\": read tcp [2001:b011:7001:12b1:7906:17ba:7c4:4b3c]:57618->[2606:4700:7::12e]:443: wsarecv: An existing connection was forcibly closed by the remote host., retrying in 1s"
time=2025-01-10T22:31:29.588+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 15 attempt 0 failed: Get \"https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/fd/fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20250110%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250110T142510Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d67e438e5214a7ff2ab374fa4b088f44e531f1a2ce67a68fc7d030e03c579\": net/http: TLS handshake timeout, retrying in 1s"
time=2025-01-10T22:31:34.194+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 15 attempt 1 failed: Get \"https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/fd/fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20250110%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250110T142510Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8e9d67e438e5214a7ff2ab374fa4b088f44e531f1a2ce67a68fc7d030e03c579\": read tcp [2001:b011:7001:12b1:7906:17ba:7c4:4b3c]:57661->[2606:4700:7::12e]:443: wsarecv: An existing connection was forcibly closed by the remote host., retrying in 2s"
time=2025-01-10T22:31:37.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.354+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:39.806+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:52.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:53.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 5 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:54.754+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:54.754+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:31:54.806+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:12.755+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 2 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:17.353+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 3 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:17.354+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 10 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:17.755+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 6 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.195+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 15 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.349+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 4 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 9 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.350+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 12 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.351+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 14 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 0 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 13 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.352+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 1 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:32:18.807+08:00 level=INFO source=download.go:370 msg="fd7b6731c33c part 7 stalled; retrying. If this persists, press ctrl-c to exit, then 'ollama pull' to find a faster connection."
time=2025-01-10T22:38:18.870+08:00 level=INFO source=download.go:291 msg="fd7b6731c33c part 11 attempt 0 failed: unexpected EOF, retrying in 1s"
```
- 嘗試直接下載 GGUF 檔，然後再用 `ollama import phi-4 -f Modelfile` 方式解決。
- 參考：https://github.com/ollama/ollama/blob/main/docs/import.md#Importing-a-GGUF-based-model-or-adapter
```bash
jazzw@JazzBook:~$ cd .ollama/models/
jazzw@JazzBook:~/.ollama/models$ mkdir phi4-gguf
jazzw@JazzBook:~/.ollama/models$ cd phi4-gguf
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ wget https://huggingface.co/microsoft/phi-4-gguf/resolve/main/phi-4-q4.gguf
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ code Modelfile
```
```
FROM c:\Users\jazzw\.ollama\models\phi4-gguf\phi-4-q4.gguf
```
```bash
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama create phi-4 -f Modelfile
transferring model data 100%
using existing layer sha256:ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
creating new layer sha256:e45b3d24c6317906f450b37650208565ff162088a4dfcf5628907cdbfea54fa1
writing manifest
success
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama ls
NAME            ID              SIZE      MODIFIED
phi-4:latest    daf843ebda23    9.1 GB    28 seconds ago
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama run phi-4
Error: llama runner process has terminated: GGML_ASSERT(hparams.n_swa > 0) failed
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama show --modelfile phi-4
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM phi-4:latest

FROM C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
TEMPLATE {{ .Prompt }}
```
- 看起來跟其他 Modelfile 不一樣
  - 參考：https://github.com/ollama/ollama/blob/main/docs/modelfile.md#examples
  - 範例 Modelfile - https://github.com/ollama/ollama/blob/main/examples/modelfile-mario/Modelfile
- TODO: 找一台機器 `ollama pull phi4` 再看看實際上長怎樣。
- 備註：因為 `ollama create phi-4 -f Modelfile` 的轉換過程中，確實在 ollama 的 log 看到 GGUF 內含 Model 資訊：
```bash
time=2025-01-10T22:05:21.891+08:00 level=INFO source=server.go:104 msg="system memory" total="31.2 GiB" free="21.2 GiB" free_swap="21.3 GiB"
time=2025-01-10T22:05:21.891+08:00 level=INFO source=memory.go:356 msg="offload to cuda" layers.requested=-1 layers.model=41 layers.offload=29 layers.split="" memory.available="[6.9 GiB]" memory.gpu_overhead="0 B" memory.required.full="9.6 GiB" memory.required.partial="6.8 GiB" memory.required.kv="400.0 MiB" memory.required.allocations="[6.8 GiB]" memory.weights.total="8.2 GiB" memory.weights.repeating="7.8 GiB" memory.weights.nonrepeating="402.0 MiB" memory.graph.full="266.7 MiB" memory.graph.partial="266.7 MiB"
time=2025-01-10T22:05:21.897+08:00 level=INFO source=server.go:376 msg="starting llama server" cmd="C:\\Users\\jazzw\\scoop\\apps\\ollama\\current\\lib\\ollama\\runners\\cuda_v12_avx\\ollama_llama_server.exe runner --model C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b --ctx-size 2048 --batch-size 512 --n-gpu-layers 29 --threads 8 --no-mmap --parallel 1 --port 56786"
time=2025-01-10T22:05:21.935+08:00 level=INFO source=sched.go:449 msg="loaded runners" count=1
time=2025-01-10T22:05:21.935+08:00 level=INFO source=server.go:555 msg="waiting for llama runner to start responding"
time=2025-01-10T22:05:21.935+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server error"
time=2025-01-10T22:05:22.140+08:00 level=INFO source=runner.go:945 msg="starting go runner"
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 4060 Laptop GPU, compute capability 8.9, VMM: yes
time=2025-01-10T22:05:22.182+08:00 level=INFO source=runner.go:946 msg=system info="CUDA : ARCHS = 600,610,620,700,720,750,800,860,870,890,900 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | LLAMAFILE = 1 | AARCH64_REPACK = 1 | cgo(clang)" threads=8
time=2025-01-10T22:05:22.182+08:00 level=INFO source=.:0 msg="Server listening on 127.0.0.1:56786"
time=2025-01-10T22:05:22.187+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server loading model"
llama_load_model_from_file: using device CUDA0 (NVIDIA GeForce RTX 4060 Laptop GPU) - 7099 MiB free
llama_model_loader: loaded meta data with 33 key-value pairs and 243 tensors from C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Phi 4
llama_model_loader: - kv   3:                            general.version str              = 4
llama_model_loader: - kv   4:                       general.organization str              = Microsoft
llama_model_loader: - kv   5:                           general.basename str              = phi
llama_model_loader: - kv   6:                         general.size_label str              = 15B
llama_model_loader: - kv   7:                            general.license str              = mit
llama_model_loader: - kv   8:                       general.license.link str              = https://huggingface.co/microsoft/phi-...
llama_model_loader: - kv   9:                               general.tags arr[str,7]       = ["phi", "nlp", "math", "code", "chat"...
llama_model_loader: - kv  10:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv  11:                        phi3.context_length u32              = 16384
llama_model_loader: - kv  12:  phi3.rope.scaling.original_context_length u32              = 16384
llama_model_loader: - kv  13:                      phi3.embedding_length u32              = 5120
llama_model_loader: - kv  14:                   phi3.feed_forward_length u32              = 17920
llama_model_loader: - kv  15:                           phi3.block_count u32              = 40
llama_model_loader: - kv  16:                  phi3.attention.head_count u32              = 40
llama_model_loader: - kv  17:               phi3.attention.head_count_kv u32              = 10
llama_model_loader: - kv  18:      phi3.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  19:                  phi3.rope.dimension_count u32              = 128
llama_model_loader: - kv  20:                        phi3.rope.freq_base f32              = 250000.000000
llama_model_loader: - kv  21:              phi3.attention.sliding_window u32              = 0
llama_model_loader: - kv  22:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  23:                         tokenizer.ggml.pre str              = dbrx
llama_model_loader: - kv  24:                      tokenizer.ggml.tokens arr[str,100352]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  25:                  tokenizer.ggml.token_type arr[i32,100352]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  26:                      tokenizer.ggml.merges arr[str,100000]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  27:                tokenizer.ggml.bos_token_id u32              = 100257
llama_model_loader: - kv  28:                tokenizer.ggml.eos_token_id u32              = 100257
llama_model_loader: - kv  29:            tokenizer.ggml.padding_token_id u32              = 100257
llama_model_loader: - kv  30:                    tokenizer.chat_template str              = {% for message in messages %}{% if (m...
llama_model_loader: - kv  31:               general.quantization_version u32              = 2
llama_model_loader: - kv  32:                          general.file_type u32              = 15
llama_model_loader: - type  f32:   81 tensors
llama_model_loader: - type q4_K:  101 tensors
llama_model_loader: - type q5_K:   40 tensors
llama_model_loader: - type q6_K:   21 tensors
llm_load_vocab: special tokens cache size = 96
llm_load_vocab: token to piece cache size = 0.6151 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = phi3
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 100352
llm_load_print_meta: n_merges         = 100000
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 16384
llm_load_print_meta: n_embd           = 5120
llm_load_print_meta: n_layer          = 40
llm_load_print_meta: n_head           = 40
llm_load_print_meta: n_head_kv        = 10
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 4
llm_load_print_meta: n_embd_k_gqa     = 1280
llm_load_print_meta: n_embd_v_gqa     = 1280
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 17920
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 2
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 250000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 16384
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 14B
llm_load_print_meta: model ftype      = Q4_K - Medium
llm_load_print_meta: model params     = 14.66 B
llm_load_print_meta: model size       = 8.43 GiB (4.94 BPW)
llm_load_print_meta: general.name     = Phi 4
llm_load_print_meta: BOS token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOS token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOT token        = 100265 '<|im_end|>'
llm_load_print_meta: PAD token        = 100257 '<|endoftext|>'
llm_load_print_meta: LF token         = 128 'Ä'
llm_load_print_meta: FIM PRE token    = 100258 '<|fim_prefix|>'
llm_load_print_meta: FIM SUF token    = 100260 '<|fim_suffix|>'
llm_load_print_meta: FIM MID token    = 100259 '<|fim_middle|>'
llm_load_print_meta: EOG token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOG token        = 100265 '<|im_end|>'
llm_load_print_meta: max token length = 256
llm_load_tensors: offloading 29 repeating layers to GPU
llm_load_tensors: offloaded 29/41 layers to GPU
llm_load_tensors:          CPU model buffer size =   275.62 MiB
llm_load_tensors:    CUDA_Host model buffer size =  2622.81 MiB
llm_load_tensors:        CUDA0 model buffer size =  5731.89 MiB
llama_new_context_with_model: n_seq_max     = 1
llama_new_context_with_model: n_ctx         = 2048
llama_new_context_with_model: n_ctx_per_seq = 2048
llama_new_context_with_model: n_batch       = 512
llama_new_context_with_model: n_ubatch      = 512
llama_new_context_with_model: flash_attn    = 0
llama_new_context_with_model: freq_base     = 250000.0
llama_new_context_with_model: freq_scale    = 1
llama_new_context_with_model: n_ctx_per_seq (2048) < n_ctx_train (16384) -- the full capacity of the model will not be utilized
llama_kv_cache_init:        CPU KV buffer size =   110.00 MiB
llama_kv_cache_init:      CUDA0 KV buffer size =   290.00 MiB
llama_new_context_with_model: KV self size  =  400.00 MiB, K (f16):  200.00 MiB, V (f16):  200.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.40 MiB
llama.cpp:10939: GGML_ASSERT(hparams.n_swa > 0) failed
time=2025-01-10T22:05:24.573+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server error"
time=2025-01-10T22:05:24.824+08:00 level=ERROR source=sched.go:455 msg="error loading llama server" error="llama runner process has terminated: GGML_ASSERT(hparams.n_swa > 0) failed"
[GIN] 2025/01/10 - 22:05:24 | 500 |    3.0077555s |       127.0.0.1 | POST     "/api/generate"
time=2025-01-10T22:05:29.844+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.0158618 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
time=2025-01-10T22:05:30.093+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.2663641 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
time=2025-01-10T22:05:30.343+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.5161787 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
```
- ( 2025-01-10 22:31:17 )
- 在 Github Codespace 上 `pull phi4`
```bash
@jazzwang ➜ /workspaces/snippet (master) $ curl -fsSL https://ollama.com/install.sh | sh
@jazzwang ➜ /workspaces/snippet (master) $ ollama pull phi4
[GIN] 2025/01/10 - 22:29:17 | 200 |     236.771µs |       127.0.0.1 | HEAD     "/"
pulling manifest ⠇ time=2025-01-10T22:29:18.009+08:00 level=INFO source=download.go:175 msg="downloading fd7b6731c33c in 16 565 MB part(s)"
pulling manifest
pulling fd7b6731c33c...  26% ▕███████████████████████                                                                     ▏ 2.3 GB/9.1 GB  226 MB/s     29s[pulling manifest
pulling fd7b6731c33c...  26% ▕███████████████████████                                                                     ▏ 2.3 GB/9.1 GB  226 MB/s     29s
Error: write /home/codespace/.ollama/models/blobs/sha256-fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20-partial: no space left on device
```
- ( 2025-01-10 22:40:12 )
- 好吧～我前面在這台 codespace 上做了太多不同的實驗，把容器的空間塞爆了 :(
  要找出浪費空間的軟體並且逐一清掉也是花時間，先新開一台試試看。
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd ~/.ollama/models/blobs/
@jazzwang ➜ ~/.ollama/models/blobs $ rm *
@jazzwang ➜ ~/.ollama/models/blobs $ cd
@jazzwang ➜ ~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   30G  592M  99% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   24G  5.4G  82% /vscode
/dev/loop3       32G   30G  592M  99% /workspaces
/dev/sda1        44G   68K   42G   1% /tmp
@jazzwang ➜ ~ $ du -sh .n8n/
380K    .n8n/
@jazzwang ➜ ~ $ du -sh .npm
3.0G    .npm
@jazzwang ➜ ~ $ du -sh .minikube/
4.0K    .minikube/
@jazzwang ➜ ~ $ du -sh .python
4.0K    .python
@jazzwang ➜ ~ $ du -sh .local/
5.2G    .local/
```
- ( 2025-01-10 22:50:41 )
- 新的 Codespace 大約還剩 20G 可以放
```bash
@jazzwang ➜ /workspaces/miniperplx (main) $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   11G   20G  35% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   25G  4.8G  84% /vscode
/dev/loop4       32G   11G   20G  35% /workspaces
/dev/sdc1        44G   18G   24G  44% /tmp
@jazzwang ➜ /workspaces/miniperplx (main) $ curl -fsSL https://ollama.com/install.sh | sh
@jazzwang ➜ /workspaces/miniperplx (main) $ ollama start
```
- ( 2025-01-10 22:54:16 )
- 先動點手腳，讓 ollama 把 model 下載到 /tmp
```
@jazzwang ➜ /workspaces/miniperplx (main) $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   14G   16G  47% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   25G  4.8G  84% /vscode
/dev/loop4       32G   14G   16G  47% /workspaces
/dev/sdc1        44G   18G   24G  44% /tmp
@jazzwang ➜ /workspaces/miniperplx (main) $ cd ~/.ollama/models
@jazzwang ➜ ~/.ollama/models $ rm -rf blobs/
@jazzwang ➜ ~/.ollama/models $ rm -rf blobs/
@jazzwang ➜ ~/.ollama/models $ mkdir -p /tmp/blobs
@jazzwang ➜ ~/.ollama/models $ ln -s /tmp/blobs
@jazzwang ➜ ~/.ollama/models $ ollama pull phi4
pulling manifest
pulling fd7b6731c33c...  78% ▕████████████████████████████████████████████████████████████████████████                    ▏ 7.1 GB/9.1 GB  219 MB/s      8s
```
- ( 2025-01-10 22:57:22 )
- 用 Cloud IDE 就是下載大檔案的時候超爽的！！
```bash
@jazzwang ➜ ~/.ollama/models $ ollama pull phi4
pulling manifest
pulling fd7b6731c33c... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏ 9.1 GB
pulling 32695b892af8... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏  275 B
pulling fa8235e5b48f... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏ 1.1 KB
pulling 45a1c652dddc... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏   82 B
pulling f5d6f49c6477... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏  486 B
verifying sha256 digest ⠋
writing manifest
success
```

> [!NOTE]
> 剛剛在想，現在如果大家都會去下載 GGUF 的 Model File，如果有人利用這一點，把病毒偽裝成 Modelfile，是否也可以拿來感染或植入病毒呢？

- ( 2025-01-10 23:00:18 )
```bash
@jazzwang ➜ ~/.ollama/models $ ollama ls
NAME           ID              SIZE      MODIFIED
phi4:latest    ac896e5b8b34    9.1 GB    2 minutes ago

@jazzwang ➜ ~/.ollama/models $ ollama show --modelfile phi4
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM phi4:latest

FROM /home/codespace/.ollama/models/blobs/sha256-fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
<|im_start|>{{ .Role }}<|im_sep|>
{{ .Content }}{{ if not $last }}<|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_end|>
<|im_start|>assistant<|im_sep|>
{{ end }}
{{- end }}"""
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
PARAMETER stop <|im_sep|>
LICENSE """Microsoft.
Copyright (c) Microsoft Corporation.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
```

- ( 2025-01-10 23:02:45 )
- 試著跑 phi4 看看

```bash
@jazzwang ➜ ~/.ollama/models $ ollama run phi4
Error: model requires more system memory (11.2 GiB) than is available (6.5 GiB)
```

```bash
@jazzwang ➜ ~/.ollama/models $ tree
.
├── blobs -> /tmp/blobs
└── manifests
    └── registry.ollama.ai
        └── library
            └── phi4
                └── latest

5 directories, 1 file
@jazzwang ➜ ~/.ollama/models $ tree /tmp/blobs/
/tmp/blobs/
├── sha256-32695b892af87ef8fca6e13a1a31c67c1441d7398be037e366e2fc763857c06a
├── sha256-45a1c652dddc9efdcefa977ab81cfbe26b6e52bc8e78f2f4c698538783e0ac80
├── sha256-f5d6f49c64775df1536e9d747c6b6b4c101f6a8658108fbd18a15d046575c68b
├── sha256-fa8235e5b48faca34e3ca98cf4f694ef08bd216d28b58071a1f85b1d50cb814d
└── sha256-fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20

0 directories, 5 files
@jazzwang ➜ ~/.ollama/models $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   14G   16G  47% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   25G  4.8G  84% /vscode
/dev/loop4       32G   14G   16G  47% /workspaces
/dev/sdc1        44G   27G   16G  64% /tmp
@jazzwang ➜ ~/.ollama/models $ du -sh /tmp/blobs/
8.5G    /tmp/blobs/
@jazzwang ➜ ~/.ollama/models $ cat manifests/registry.ollama.ai/library/phi4/latest  | jq .
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
  "config": {
    "mediaType": "application/vnd.docker.container.image.v1+json",
    "digest": "sha256:f5d6f49c64775df1536e9d747c6b6b4c101f6a8658108fbd18a15d046575c68b",
    "size": 486
  },
  "layers": [
    {
      "mediaType": "application/vnd.ollama.image.model",
      "digest": "sha256:fd7b6731c33c57f61767612f56517460ec2d1e2e5a3f0163e0eb3d8d8cb5df20",
      "size": 9053114464
    },
    {
      "mediaType": "application/vnd.ollama.image.template",
      "digest": "sha256:32695b892af87ef8fca6e13a1a31c67c1441d7398be037e366e2fc763857c06a",
      "size": 275
    },
    {
      "mediaType": "application/vnd.ollama.image.license",
      "digest": "sha256:fa8235e5b48faca34e3ca98cf4f694ef08bd216d28b58071a1f85b1d50cb814d",
      "size": 1084
    },
    {
      "mediaType": "application/vnd.ollama.image.params",
      "digest": "sha256:45a1c652dddc9efdcefa977ab81cfbe26b6e52bc8e78f2f4c698538783e0ac80",
      "size": 82
    }
  ]
}
```

## 2025-01-11

- ( 2025-01-11 23:26:03 )
- 試試看把 ollama phi4 的 Modelfile 修改一下，看能否正常運作：
```
FROM c:\Users\jazzw\.ollama\models\phi4-gguf\phi-4-q4.gguf
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
<|im_start|>{{ .Role }}<|im_sep|>
{{ .Content }}{{ if not $last }}<|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_end|>
<|im_start|>assistant<|im_sep|>
{{ end }}
{{- end }}"""
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
PARAMETER stop <|im_sep|>
LICENSE """Microsoft.
Copyright (c) Microsoft Corporation.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
```
- 啟動 ollama，然後用 `ollama create <model_name> -f <Modelfile>` 指令匯入已經存在的 GGUF 模型檔。
```bash
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama start &
jazzw@JazzBook:~/.ollama/models/phi4-gguf$ ollama create phi-4 -f Modelfile
[GIN] 2025/01/11 - 23:31:19 | 200 |            0s |       127.0.0.1 | HEAD     "/"
transferring model data ⠼ [GIN] 2025/01/11 - 23:31:25 | 200 |      6.9918ms |       127.0.0.1 | POST     "/api/blobs/sha256:ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b"
[GIN] 2025/01/11 - 23:31:25 | 200 |     27.6745ms |       127.0.0.1 | POST     "/api/create"
transferring model data 100%
using existing layer sha256:ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
creating new layer sha256:32695b892af87ef8fca6e13a1a31c67c1441d7398be037e366e2fc763857c06a
creating new layer sha256:fa8235e5b48faca34e3ca98cf4f694ef08bd216d28b58071a1f85b1d50cb814d
creating new layer sha256:45a1c652dddc9efdcefa977ab81cfbe26b6e52bc8e78f2f4c698538783e0ac80
creating new layer sha256:de185479d4bce03a83e09483b4deac8a80cacfe59209736f784d2aa07ebff6c9
writing manifest
success
jazzw@JazzBook:~/.ollama/models$ tree blobs/
blobs/
├── sha256-32695b892af87ef8fca6e13a1a31c67c1441d7398be037e366e2fc763857c06a
├── sha256-45a1c652dddc9efdcefa977ab81cfbe26b6e52bc8e78f2f4c698538783e0ac80
├── sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
├── sha256-de185479d4bce03a83e09483b4deac8a80cacfe59209736f784d2aa07ebff6c9
└── sha256-fa8235e5b48faca34e3ca98cf4f694ef08bd216d28b58071a1f85b1d50cb814d

1 directory, 5 files
jazzw@JazzBook:~/.ollama/models$ tree manifests/
manifests/
└── registry.ollama.ai
    └── library
        └── phi-4
            └── latest

4 directories, 1 file
```
- ( 2025-01-12 00:47:18 )
```bash
jazzw@JazzBook:~$ ollama run phi-4
[GIN] 2025/01/11 - 23:35:14 | 200 |            0s |       127.0.0.1 | HEAD     "/"
[GIN] 2025/01/11 - 23:35:14 | 200 |     12.7661ms |       127.0.0.1 | POST     "/api/show"
time=2025-01-11T23:35:14.622+08:00 level=INFO source=server.go:104 msg="system memory" total="31.2 GiB" free="21.5 GiB" free_swap="20.6 GiB"
time=2025-01-11T23:35:14.623+08:00 level=INFO source=memory.go:356 msg="offload to cuda" layers.requested=-1 layers.model=41 layers.offload=29 layers.split="" memory.available="[6.9 GiB]" memory.gpu_overhead="0 B" memory.required.full="9.6 GiB" memory.required.partial="6.8 GiB" memory.required.kv="400.0 MiB" memory.required.allocations="[6.8 GiB]" memory.weights.total="8.2 GiB" memory.weights.repeating="7.8 GiB" memory.weights.nonrepeating="402.0 MiB" memory.graph.full="266.7 MiB" memory.graph.partial="266.7 MiB"
time=2025-01-11T23:35:14.635+08:00 level=INFO source=server.go:376 msg="starting llama server" cmd="C:\\Users\\jazzw\\scoop\\apps\\ollama\\current\\lib\\ollama\\runners\\cuda_v12_avx\\ollama_llama_server.exe runner --model C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b --ctx-size 2048 --batch-size 512 --n-gpu-layers 29 --threads 8 --no-mmap --parallel 1 --port 57271"
⠙ time=2025-01-11T23:35:14.671+08:00 level=INFO source=sched.go:449 msg="loaded runners" count=1
time=2025-01-11T23:35:14.672+08:00 level=INFO source=server.go:555 msg="waiting for llama runner to start responding"
time=2025-01-11T23:35:14.673+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server error"
⠸ time=2025-01-11T23:35:14.870+08:00 level=INFO source=runner.go:945 msg="starting go runner"
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 4060 Laptop GPU, compute capability 8.9, VMM: yes
time=2025-01-11T23:35:14.910+08:00 level=INFO source=runner.go:946 msg=system info="CUDA : ARCHS = 600,610,620,700,720,750,800,860,870,890,900 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | LLAMAFILE = 1 | AARCH64_REPACK = 1 | cgo(clang)" threads=8
time=2025-01-11T23:35:14.911+08:00 level=INFO source=.:0 msg="Server listening on 127.0.0.1:57271"
time=2025-01-11T23:35:14.924+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server loading model"
⠼ llama_load_model_from_file: using device CUDA0 (NVIDIA GeForce RTX 4060 Laptop GPU) - 7099 MiB free
llama_model_loader: loaded meta data with 33 key-value pairs and 243 tensors from C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = phi3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Phi 4
llama_model_loader: - kv   3:                            general.version str              = 4
llama_model_loader: - kv   4:                       general.organization str              = Microsoft
llama_model_loader: - kv   5:                           general.basename str              = phi
llama_model_loader: - kv   6:                         general.size_label str              = 15B
llama_model_loader: - kv   7:                            general.license str              = mit
llama_model_loader: - kv   8:                       general.license.link str              = https://huggingface.co/microsoft/phi-...
llama_model_loader: - kv   9:                               general.tags arr[str,7]       = ["phi", "nlp", "math", "code", "chat"...
llama_model_loader: - kv  10:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv  11:                        phi3.context_length u32              = 16384
llama_model_loader: - kv  12:  phi3.rope.scaling.original_context_length u32              = 16384
llama_model_loader: - kv  13:                      phi3.embedding_length u32              = 5120
llama_model_loader: - kv  14:                   phi3.feed_forward_length u32              = 17920
llama_model_loader: - kv  15:                           phi3.block_count u32              = 40
llama_model_loader: - kv  16:                  phi3.attention.head_count u32              = 40
llama_model_loader: - kv  17:               phi3.attention.head_count_kv u32              = 10
llama_model_loader: - kv  18:      phi3.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  19:                  phi3.rope.dimension_count u32              = 128
llama_model_loader: - kv  20:                        phi3.rope.freq_base f32              = 250000.000000
llama_model_loader: - kv  21:              phi3.attention.sliding_window u32              = 0
llama_model_loader: - kv  22:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  23:                         tokenizer.ggml.pre str              = dbrx
llama_model_loader: - kv  24:                      tokenizer.ggml.tokens arr[str,100352]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  25:                  tokenizer.ggml.token_type arr[i32,100352]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  26:                      tokenizer.ggml.merges arr[str,100000]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  27:                tokenizer.ggml.bos_token_id u32              = 100257
llama_model_loader: - kv  28:                tokenizer.ggml.eos_token_id u32              = 100257
llama_model_loader: - kv  29:            tokenizer.ggml.padding_token_id u32              = 100257
llama_model_loader: - kv  30:                    tokenizer.chat_template str              = {% for message in messages %}{% if (m...
llama_model_loader: - kv  31:               general.quantization_version u32              = 2
llama_model_loader: - kv  32:                          general.file_type u32              = 15
llama_model_loader: - type  f32:   81 tensors
llama_model_loader: - type q4_K:  101 tensors
llama_model_loader: - type q5_K:   40 tensors
llama_model_loader: - type q6_K:   21 tensors
⠴ llm_load_vocab: special tokens cache size = 96
llm_load_vocab: token to piece cache size = 0.6151 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = phi3
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 100352
llm_load_print_meta: n_merges         = 100000
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 16384
llm_load_print_meta: n_embd           = 5120
llm_load_print_meta: n_layer          = 40
llm_load_print_meta: n_head           = 40
llm_load_print_meta: n_head_kv        = 10
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 4
llm_load_print_meta: n_embd_k_gqa     = 1280
llm_load_print_meta: n_embd_v_gqa     = 1280
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 17920
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 2
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 250000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 16384
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 14B
llm_load_print_meta: model ftype      = Q4_K - Medium
llm_load_print_meta: model params     = 14.66 B
llm_load_print_meta: model size       = 8.43 GiB (4.94 BPW)
llm_load_print_meta: general.name     = Phi 4
llm_load_print_meta: BOS token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOS token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOT token        = 100265 '<|im_end|>'
llm_load_print_meta: PAD token        = 100257 '<|endoftext|>'
llm_load_print_meta: LF token         = 128 'Ä'
llm_load_print_meta: FIM PRE token    = 100258 '<|fim_prefix|>'
llm_load_print_meta: FIM SUF token    = 100260 '<|fim_suffix|>'
llm_load_print_meta: FIM MID token    = 100259 '<|fim_middle|>'
llm_load_print_meta: EOG token        = 100257 '<|endoftext|>'
llm_load_print_meta: EOG token        = 100265 '<|im_end|>'
llm_load_print_meta: max token length = 256
⠧ llm_load_tensors: offloading 29 repeating layers to GPU
llm_load_tensors: offloaded 29/41 layers to GPU
llm_load_tensors:          CPU model buffer size =   275.62 MiB
llm_load_tensors:    CUDA_Host model buffer size =  2622.81 MiB
llm_load_tensors:        CUDA0 model buffer size =  5731.89 MiB
⠏ llama_new_context_with_model: n_seq_max     = 1
llama_new_context_with_model: n_ctx         = 2048
llama_new_context_with_model: n_ctx_per_seq = 2048
llama_new_context_with_model: n_batch       = 512
llama_new_context_with_model: n_ubatch      = 512
llama_new_context_with_model: flash_attn    = 0
llama_new_context_with_model: freq_base     = 250000.0
llama_new_context_with_model: freq_scale    = 1
llama_new_context_with_model: n_ctx_per_seq (2048) < n_ctx_train (16384) -- the full capacity of the model will not be utilized
llama_kv_cache_init:        CPU KV buffer size =   110.00 MiB
llama_kv_cache_init:      CUDA0 KV buffer size =   290.00 MiB
llama_new_context_with_model: KV self size  =  400.00 MiB, K (f16):  200.00 MiB, V (f16):  200.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.40 MiB
llama.cpp:10939: GGML_ASSERT(hparams.n_swa > 0) failed
⠹ time=2025-01-11T23:35:19.747+08:00 level=INFO source=server.go:589 msg="waiting for server to become available" status="llm server error"
⠼ time=2025-01-11T23:35:19.999+08:00 level=ERROR source=sched.go:455 msg="error loading llama server" error="llama runner process has terminated: GGML_ASSERT(hparams.n_swa > 0) failed"
[GIN] 2025/01/11 - 23:35:20 | 500 |    5.4592604s |       127.0.0.1 | POST     "/api/generate"
Error: llama runner process has terminated: GGML_ASSERT(hparams.n_swa > 0) failed
jazzw@JazzBook:~$ time=2025-01-11T23:35:25.020+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.01692 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
time=2025-01-11T23:35:25.268+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.2673998 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
time=2025-01-11T23:35:25.517+08:00 level=WARN source=sched.go:646 msg="gpu VRAM usage didn't recover within timeout" seconds=5.5169129 model=C:\Users\jazzw\.ollama\models\blobs\sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
```

## 2025-01-14

- ( 2025-01-14 13:20:25 )
- 實驗：4-core Github Codespace (4-core, 16 GB RAM)
- 蠻奇怪的，突然變成 `Alpine` 作業系統的 container，沒辦法跑 ollama。居然會 `Segmentation fault`。感覺 Git repo 也沒有掛載成功。亂詭異一把的！
```bash
codespaces-5ea095:/workspaces/snippet$ curl -fsSL https://ollama.com/install.sh | sh
>>> Installing ollama to /usr/local
>>> Downloading Linux amd64 bundle
######################################################################## 100.0%
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
codespaces-5ea095:/workspaces/snippet$ which ollama
/usr/local/bin/ollama
codespaces-5ea095:/workspaces/snippet$ ollama start &
[1] 1396
codespaces-5ea095:/workspaces/snippet$ ls -al
total 8
drwxrwxrwx+ 2 vscode root 4096 Jan 14 00:05 .
drwxr-xrwx+ 4 vscode root 4096 Jan 14 00:05 ..
[1]+  Segmentation fault      (core dumped) ollama start
jazzw@JazzBook:~/git/snippet$ snippet logs
2025-01-14 05:16:28.332Z: Host information
2025-01-14 05:16:28.338Z: ----------------
2025-01-14 05:16:28.339Z: OS: Ubuntu 22.04.5 LTS (stable release)
2025-01-14 05:16:28.339Z: Image details: https://github.com/github/codespaces-host-images/blob/main/README.md
2025-01-14 05:16:28.339Z: ----------------

=================================================================================
2025-01-14 05:16:28.339Z: Configuration starting...
2025-01-14 05:16:28.346Z: Cloning...
2025-01-14 05:16:28.383Z: Using image: mcr.microsoft.com/devcontainers/universal

=================================================================================
2025-01-14 05:16:28.401Z: Creating container...
2025-01-14 05:16:28.447Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/snippet --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --expect-existing-container --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2025-01-14 05:16:28.675Z: @devcontainers/cli 0.68.0. Node.js v18.20.5. linux 6.5.0-1025-azure x64.
2025-01-14 05:16:28.904Z: $ docker start 42b2d8c31510b02ff92cee476a84446eb9ce465adde42ca55f63bb34ad627a03
2025-01-14 05:16:30.247Z: 42b2d8c31510b02ff92cee476a84446eb9ce465adde42ca55f63bb34ad627a03

2025-01-14 05:16:30.248Z: Stop: Run: docker start 42b2d8c31510b02ff92cee476a84446eb9ce465adde42ca55f63bb34ad627a03
2025-01-14 05:16:30.355Z: Shell server terminated (code: 126, signal: null)
2025-01-14 05:16:30.355Z: unable to find user codespace: no matching entries in passwd file
2025-01-14 05:16:30.356Z: {"outcome":"error","message":"An error occurred setting up the container.","description":"An error occurred setting up the container.","containerId":"42b2d8c31510b02ff92cee476a84446eb9ce465adde42ca55f63bb34ad627a03"}
2025-01-14 05:16:30.357Z: Error: An error occurred setting up the container.
2025-01-14 05:16:30.357Z:     at wtA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:465:1260)
2025-01-14 05:16:30.358Z:     at NH (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:465:1002)
2025-01-14 05:16:30.358Z:     at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
2025-01-14 05:16:30.358Z:     at async YtA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:482:3771)
2025-01-14 05:16:30.359Z:     at async eB (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:482:4886)
2025-01-14 05:16:30.359Z:     at async prA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:663:200)
2025-01-14 05:16:30.360Z:     at async drA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:662:14706)
2025-01-14 05:16:30.366Z: devcontainer process exited with exit code 1

====================================== ERROR ====================================
2025-01-14 05:16:30.372Z: Failed to create container.
=================================================================================
2025-01-14 05:16:30.372Z: Error: An error occurred setting up the container.
2025-01-14 05:16:30.376Z: Error code: 1302 (UnifiedContainersErrorFatalCreatingContainer)

====================================== ERROR ====================================
2025-01-14 05:16:30.388Z: Container creation failed.
=================================================================================
2025-01-14 05:16:30.520Z:

===================================== WARNING ===================================
2025-01-14 05:16:30.521Z: Creating recovery container.
=================================================================================

=================================================================================
2025-01-14 05:16:31.736Z: Creating container...
2025-01-14 05:16:31.755Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/snippet --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2025-01-14 05:16:31.926Z: @devcontainers/cli 0.68.0. Node.js v18.20.5. linux 6.5.0-1025-azure x64.
2025-01-14 05:16:32.316Z: $alpine -c echo Container started
2025-01-14 05:16:32.377Z: Unable to find image 'mcr.microsoft.com/devcontainers/base:alpine' locally
2025-01-14 05:16:32.586Z: alpine: Pulling from devcontainers/base
2025-01-14 05:16:32.990Z: da9db072f522: 2025-01-14 05:16:32.990Z: Pull complete
3cdff9e33f37: Pull complete
87dffdaee0b6: Pull complete
3f72e2f1b3f3: Pull complete
1ac829ce5af3: Pull complete
2a15ab263bdf: Pull complete
a9bdcaa5c876: Pull complete
2025-01-14 05:16:51.275Z: Digest: sha256:5212d8ed44c89bfadad14a03104ef75b09c5de8642a58721c271f2e9155f5023
2025-01-14 05:16:51.277Z: Status: Downloaded newer image for mcr.microsoft.com/devcontainers/base:alpine
2025-01-14 05:16:51.410Z: Container started
2025-01-14 05:16:51.605Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/snippet
2025-01-14 05:16:51.611Z: devcontainer process exited with exit code 0

=================================================================================
2025-01-14 05:16:52.467Z: Running blocking commands...
2025-01-14 05:16:52.495Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/snippet --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --expect-existing-container --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2025-01-14 05:16:52.702Z: @devcontainers/cli 0.68.0. Node.js v18.20.5. linux 6.5.0-1025-azure x64.
2025-01-14 05:16:52.917Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/snippet
2025-01-14 05:16:52.923Z: devcontainer process exited with exit code 0

=================================================================================
2025-01-14 05:16:52.934Z: Configuring codespace...

=================================================================================
2025-01-14 05:16:52.942Z: Finished configuring codespace.
```
- ( 2025-01-14 15:03:57 )
- 砍掉重練！
```bash
@jazzwang ➜ /workspaces/snippet (master) $ curl -fsSL https://ollama.com/install.sh | sh
@jazzwang ➜ /workspaces/snippet (master) $ ollama start &
@jazzwang ➜ /workspaces/snippet (master) $ ollama pull phi4
```
- 狀況：不管開在 Singapore 或 US West region 都 retry 好幾次，沒辦法完整從 Ollama 下載 Phi4 
- ( 2025-01-14 15:20:23 )
- 替代作法：只好從 huggingface 下載 GGUF，然後手動新增：
```
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ wget https://huggingface.co/microsoft/phi-4-gguf/resolve/main/phi-4-q4.gguf

Connecting to cdn-lfs-us-1.hf.co (cdn-lfs-us-1.hf.co)|3.165.160.38|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9053114464 (8.4G) [binary/octet-stream]
Saving to: ‘phi-4-q4.gguf’

phi-4-q4.gguf           100%[==============================>]   8.43G  39.8MB/s    in 3m 36s  

2025-01-14 07:21:05 (40.1 MB/s) - ‘phi-4-q4.gguf’ saved [9053114464/9053114464]

@jazzwang ➜ /tmp $ 
@jazzwang ➜ /tmp $ code Modelfile
```

> [!TIP]
> 在 Ubuntu Linux 上，不知道為什麼 `FROM` 後面不能加絕對路徑 `/tmp/phi-4-q4.gguf`。
> 會出現 `invalid model name` 的錯誤訊息。
> 後來把 `Modelfile` 跟 `phi-4-q4.gguf` 放在一起，就可以正常匯入了。

``` 
FROM phi-4-q4.gguf
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
<|im_start|>{{ .Role }}<|im_sep|>
{{ .Content }}{{ if not $last }}<|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_end|>
<|im_start|>assistant<|im_sep|>
{{ end }}
{{- end }}"""
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
PARAMETER stop <|im_sep|>
LICENSE """Microsoft.
Copyright (c) Microsoft Corporation.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
```
- 啟動 ollama，然後匯入 GGUF
```
@jazzwang ➜ /tmp $ ollama start &
@jazzwang ➜ / $ ollama create phi-4 -f /tmp/Modelfile
gathering model components
copying file sha256:ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b 100%
parsing GGUF
using existing layer sha256:ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
creating new layer sha256:32695b892af87ef8fca6e13a1a31c67c1441d7398be037e366e2fc763857c06a
creating new layer sha256:fa8235e5b48faca34e3ca98cf4f694ef08bd216d28b58071a1f85b1d50cb814d
creating new layer sha256:45a1c652dddc9efdcefa977ab81cfbe26b6e52bc8e78f2f4c698538783e0ac80
writing manifest
success
@jazzwang ➜ / $ cd
```
- 嘗試執行匯入成功的 `Phi-4` 模型：
```
@jazzwang ➜ ~ $ ollama run phi-4
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
    architecture        phi3
    parameters          14.7B
    context length      16384
    embedding length    5120
    quantization        Q4_K_M

  Parameters
    stop    "<|im_start|>"
    stop    "<|im_end|>"
    stop    "<|im_sep|>"

  License
    Microsoft.
    Copyright (c) Microsoft Corporation.

>>> /show modelfile
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM phi-4:latest

FROM /home/codespace/.ollama/models/blobs/sha256-ab704ffa097f5902b937ca5d0c166226f1201e7492da30fa4e1c086c217afd6b
TEMPLATE """{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
<|im_start|>{{ .Role }}<|im_sep|>
{{ .Content }}{{ if not $last }}<|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_end|>
<|im_start|>assistant<|im_sep|>
{{ end }}
{{- end }}"""
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
PARAMETER stop <|im_sep|>
LICENSE """Microsoft.
Copyright (c) Microsoft Corporation.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
```

- ( 2025-01-14 17:09:35 )
- 在 Phi4 運行的同時，觀察一下 linux process 跟開了哪些檔案：

```bash
@jazzwang ➜ /workspaces/snippet (master) $ ps ax
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:00 /sbin/docker-init -- /bin/sh -c echo Container started trap "exit 0" 15 /usr/local/share/ssh-init.sh /usr/local/share/docker-in
      7 ?        S      0:00 sleep infinity
     35 ?        S<s    0:00 sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
   1514 ?        Sl     0:00 dockerd --dns 168.63.129.16
   1523 ?        Ssl    0:00 containerd --config /var/run/docker/containerd/containerd.toml
   1858 ?        S<s    0:00 sshd: codespace [priv]
   1868 ?        S<     0:00 sshd: codespace@pts/0
   1869 pts/0    S<s    0:00 -bash
   2638 ?        S<s    0:00 sshd: codespace [priv]
   2648 ?        S<     0:00 sshd: codespace@pts/1
   2649 pts/1    S<s    0:00 -bash
   3790 pts/0    S<l+   0:21 ollama start
   4911 ?        S<s    0:00 sshd: codespace [priv]
   4921 ?        R<     0:00 sshd: codespace@pts/2
   4922 pts/2    S<s    0:00 -bash
   5645 pts/1    S<l+   0:00 ollama run phi-4
   5654 pts/0    S<l+   1:55 /usr/local/lib/ollama/runners/cpu_avx2/ollama_llama_server runner --model /home/codespace/.ollama/models/blobs/sha256-ab704ffa0
   6230 pts/2    R<+    0:00 ps ax
@jazzwang ➜ /workspaces/snippet (master) $ lsof -p 5654
COMMAND    PID      USER   FD      TYPE DEVICE SIZE/OFF    NODE NAME
ollama_ll 5654 codespace  cwd       DIR    8,1     4096 1310721 /tmp
ollama_ll 5654 codespace  rtd       DIR   0,46     4096 1187864 /
ollama_ll 5654 codespace  txt       REG   0,46  9860720 1188916 /usr/local/lib/ollama/runners/cpu_avx2/ollama_llama_server
ollama_ll 5654 codespace  mem       REG    7,7          1188916 /usr/local/lib/ollama/runners/cpu_avx2/ollama_llama_server (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180585 /usr/lib/x86_64-linux-gnu/libc-2.31.so (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180610 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1 (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180627 /usr/lib/x86_64-linux-gnu/libm-2.31.so (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180695 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28 (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180679 /usr/lib/x86_64-linux-gnu/libpthread-2.31.so (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180681 /usr/lib/x86_64-linux-gnu/libresolv-2.31.so (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180596 /usr/lib/x86_64-linux-gnu/libdl-2.31.so (path dev=0,46)
ollama_ll 5654 codespace  mem       REG    7,7          1180563 /usr/lib/x86_64-linux-gnu/ld-2.31.so (path dev=0,46)
ollama_ll 5654 codespace    0r      CHR    1,3      0t0      50 /dev/null
ollama_ll 5654 codespace    1u      CHR  136,0      0t0       3 /dev/pts/0
ollama_ll 5654 codespace    2w     FIFO   0,14      0t0  107762 pipe
ollama_ll 5654 codespace    3u     IPv4 106239      0t0     TCP localhost:39393 (LISTEN)
ollama_ll 5654 codespace    4u     IPv4 112431      0t0     TCP localhost:39393->localhost:35696 (ESTABLISHED)
ollama_ll 5654 codespace    5u  a_inode   0,15        0    2084 [eventpoll]
ollama_ll 5654 codespace    6w      CHR    1,3      0t0      50 /dev/null
ollama_ll 5654 codespace    7u  a_inode   0,15        0    2084 [eventfd]
```

- ( 2025-01-14 17:14:11 )
- 讓 Phi4 靠 4-core 16 GB RAM 的 Codespace 容器產生貪吃蛇遊戲：

```bash
>>> create a python snake game
```

- 以下是 Phi4 的回應：

-----

Creating a simple Snake game in Python can be done using the `turtle` graphics library, which provides an easy way to draw shapes and handle events.
Below is a basic implementation of the Snake game.

```python
import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

segments = []

# Functions to control the snake's movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Main game loop
while True:
    screen.update()

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

    screen.update()
```

### Explanation:

- **Setup**: We use `turtle` to create a window and initialize the snake's head and food.

- **Movement Functions**: These functions change the direction of the snake based on user input.

- **Main Game Loop**: The game continuously checks for collisions with borders, food, or itself. It updates the position of the snake and handles
growth when food is eaten.

- **Collision Detection**: If the snake hits the border or itself, it resets to the starting position.

This code provides a basic framework for a Snake game. You can expand upon it by adding features like score tracking, increasing difficulty, or
improving graphics.

```
>>> Send a message (/? for help)
>>> /bye
```
-----

- ( 2025-01-14 17:18:52 )
<div style='background-color: lightgreen; padding: 3px; margin: 3px;'>

初步證實，Phi4 模型，純靠 CPU 的話，需要搭配約 11GB 的 System RAM。
回應速度比較慢，暫時還沒找到可以量測生成 token 的速度。
或許要在 `ollama start` 的視窗看一下 API call history 是否有統計結果。

</div>