# llamafile

> llamafile lets you distribute and run LLMs with a single file.

- 2023-11-29 : Introducing llamafile https://hacks.mozilla.org/2023/11/introducing-llamafile/

- Git Repo: https://github.com/Mozilla-Ocho/llamafile

## 2024-10-25

- 先前在 reddit 看到關於 llamafile 的相關討論。
- 2024-10-23 看到微軟 BitNet 這個 1-bit LLM，一直都不是很了解 `Quantization` 到底影響的是 "Model Training" 還是 "Model Serving"?
- 可以確定的是 llamafile 是整合 `llama.cpp`，用 [Cosmopolitan Libc](https://github.com/jart/cosmopolitan) 讓編譯出來的 llamafile 可以在不同 CPU 架構上運行。是個蠻有趣的想法，可以單一檔案在 x84_64 , arm64 CPU 架構運行的 Windows, Linux, macOS, BSD 運行的執行檔。