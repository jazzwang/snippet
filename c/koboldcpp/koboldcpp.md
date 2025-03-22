# koboldcpp

> Run GGUF models easily with a KoboldAI UI. One File. Zero Install.

- Git Repo
  - https://github.com/LostRuins/koboldcpp

## 2025-03-22

- 在 ["DeepSeek 本地部署 | llama.cpp 與 ollama"](https://medium.com/@cch.chichieh/deepseek-%E6%9C%AC%E5%9C%B0%E9%83%A8%E5%B1%AC-llama-cpp-%E8%88%87-ollama-78f24809604f) 看到這張圖，總算比較理解不同框架的定位。

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4OZ7nN2mRUj5SUXiP5KUkg.png)

### Install 安裝

- 查了一下，`koboldcpp` 在 Windows 上可以用 `scoop` 安裝
```bash
jazzw@JazzBook:~/git/snippet/c/koboldcpp$ scoop search koboldcpp
Results from local buckets...

Name      Version Source Binaries
----      ------- ------ --------
koboldcpp 1.86.2  extras
```
- ( 2025-03-22 16:31:30 )
- 安裝
```
jazzw@JazzBook:~/git/snippet/c/koboldcpp$ scoop install koboldcpp
```