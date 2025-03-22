## 2025-03-22

### Ollama

- 看起來 Ollama 只要有 `Tools` 標籤就是支援 Function Calling
  - https://ollama.com/search?c=tools
- 所以像是 DeepSeek R1 就要找
  - https://ollama.com/MFDoom/deepseek-r1-tool-calling:14b-qwen-distill-fp16
- 相關討論：
  - https://github.com/QwenLM/Qwen2.5/issues/378

### 試用 Google Deep Research

- 結果： https://g.co/gemini/share/59fcd398f381


Q: 第一次的 Prompt 
```
請試著整理以下大語言模型 LLM 的 Function Call 函數調用外部工具 Tool 的支援情形，
結果請以 Markdown 表格方式呈現。
LLM 包括：Gemma 3, Qwen 2.5, QwQ, DeepSeek R1
框架包括：Ollama, vLLM, llama.cpp, LM Studio, AnythingLLM
```
第二次的 Prompt 
```
請試著整理以下大語言模型 LLM 的 Function Call 函數調用外部工具 Tool 的支援情形，
結果請以 Markdown 表格方式呈現。
LLM 包括：Qwen 2.5, QwQ, DeepSeek R1, Gemma 3
框架包括：Ollama, llama.cpp
```

A: 
> 第一次的 Prompt 可能排列組合複雜度太高，
  卡在搜尋兩百多個網頁一個小時，所以手動強制終止。
  縮小範圍後，第二次的 Prompt 得到以下結果：

-----

# 大語言模型 Function Call 函數調用外部工具支援情況分析報告

## 1\. 前言

函數調用 (Function Call) 或工具調用 (Tool Calling) 是指大型語言模型 (LLM) 能夠識別使用者查詢中需要外部工具或函數來完成任務或回答問題的情況 。這項能力對於提升 LLM 的應用範圍至關重要，因為它允許模型與現實世界的數據和系統進行互動 。函數調用通常涉及 LLM 生成結構化的輸出（通常為 JSON 格式），指定要調用的函數以及所需的參數 。  

本報告旨在基於所提供的研究資料，分析 Qwen 2.5、QwQ、DeepSeek R1 和 Gemma 3 這四種大型語言模型在 Ollama 和 llama.cpp 這兩個推論框架下的函數調用支援情況。報告的目標是清晰地闡述每種 LLM 與框架組合的當前支援狀態，以便開發者和研究人員能夠更好地理解和選擇適合其專案的工具。

## 2\. Qwen 2.5 的函數調用支援

Qwen 2.5 具備原生的工具調用支援，這與函數調用的概念通常可以互換使用 。官方部落格文章強調了 Qwen 2.5 在理解結構化數據方面的改進，以及更可靠地生成結構化輸出（尤其是 JSON 格式）的能力，這對於函數調用至關重要 。此外，Qwen 2.5 在預訓練階段就已使用支援函數調用的範本 。  

在使用 Ollama 框架時，Qwen 2.5 也支援工具調用功能 。這可以通過啟動 Ollama 的 OpenAI 相容服務來實現 。Ollama 函式庫中 Qwen 2.5 的頁面也明確指出通過 "tools" 標籤提供工具支援 。Ollama 中的提示範本 (prompt template) 經過設計，有助於工具的使用 。Reddit 上的使用者經驗也證實了 Qwen 2.5 在 Ollama 中可以正常進行工具調用 。然而，需要注意的是 Ollama 的預設最大上下文長度可能會影響包含 JSON 結構描述的工具的使用 。  

至於 llama.cpp 框架，Qwen 2.5 也受到支援 。相關文件提到可以使用 GGUF 檔案與最新的 llama.cpp 版本 。llama.cpp 近期新增了對 OpenAI 風格函數調用的支援，並且 Qwen 2.5 被明確列為原生支援的工具調用格式之一 。目前 llama.cpp 中的 `llama-cli` 工具正在開發中，以期完全整合函數調用功能 。在 llama.cpp 中使用 Qwen 2.5 可能需要利用 `llama-cli` 範例程式 。  

整體而言，Qwen 2.5 在 Ollama 和 llama.cpp 這兩個框架下都展現了強大的函數調用支援。官方文件和社群回饋都證實了這一點。Ollama 的整合似乎特別順暢，這得益於其 OpenAI 相容的 API 和專用的提示範本。對於 llama.cpp 而言，雖然支援存在，但使用者可能需要依賴命令列介面，並確保使用的是包含函數調用功能的最新版本。

## 3\. QwQ 的函數調用支援

QwQ 是 Qwen 系列中專注於推理的模型 。其主要優勢在於進階的推理和批判性思考能力 。  

QwQ 可以在 Ollama 框架下運行 。Ollama 函式庫中 QwQ 的頁面包含一個 "tools" 標籤 。QwQ 在 Ollama 中可以通過 OpenAI 相容的 API 進行存取 。然而，相較於 Qwen 2.5，所提供的研究資料並未明確說明 QwQ 在 Ollama 中函數調用實現的程度或易用性。資料的重點似乎更多地放在其推理能力上 。  

由於 QwQ 是基於 Qwen 2.5 開發的 ，理論上應該與支援 Qwen 2.5 的 llama.cpp 相容 。然而，研究資料並未提供關於 QwQ 在 llama.cpp 中函數調用支援的明確確認或詳細資訊。Snippet 列出了 "Qwen 2.5" 和 "Qwen 2.5 Coder" 具有 llama.cpp 的原生工具調用格式支援，但並未提及 "QwQ"。  

總結來說，雖然 QwQ 可以與 Ollama 共同使用，並且由於其基於 Qwen 2.5，可能也與 llama.cpp 相容，但相較於 Qwen 2.5，其直接函數調用支援的程度尚不明朗。模型設計的重點在於推理，這可能意味著函數調用功能的發展程度較低，或者需要特定的提示策略才能實現。Ollama 中 "tools" 標籤的存在暗示了某種程度的支援，但要獲得確切答案，需要查閱這些摘要之外的更多資訊。

## 4\. DeepSeek R1 的函數調用支援

DeepSeek R1 本身並不原生支援函數調用或結構化輸出 。DeepSeek 團隊在官方 GitHub issue 中確認了這一點，並提及未來計劃增加對這些功能的支援 。該模型主要針對需要大量推理的任務進行了優化 。  

DeepSeek R1 可以在 Ollama 框架下運行 。值得注意的是，Ollama 上存在一些社群修改版的 DeepSeek R1，它們試圖通過自訂的聊天範本來增加工具調用支援 。例如，`MFDoom/deepseek-r1-tool-calling` 這個 Ollama 模型明確聲明通過自訂範本提供工具調用支援 。部分摘要發布時，官方 DeepSeek API 的 `deepseek-chat` 模型的功能調用能力尚不穩定 。此外，使用 LangChain 和 OllamaFunctions 的變通方法也曾被探索，但據報告存在潛在問題 。  

至於 llama.cpp 框架，DeepSeek R1 受到支援 。然而，llama.cpp 對 OpenAI 風格函數調用的支援列表中，DeepSeek R1 的狀態標記為 "WIP / 似乎不願意調用任何工具？" 。這表示雖然框架具備此能力，但 DeepSeek R1 在沒有特定配置或提示的情況下可能不容易使用它。社群也在積極努力優化 DeepSeek R1 在 llama.cpp 上的性能 。  

總而言之，DeepSeek R1 在其官方版本中不支援函數調用。然而，社群已積極致力於克服此限制，尤其是在 Ollama 框架內，通過創建具有自訂範本的修改模型來實現。llama.cpp 中的支援仍在開發中，可能需要特定的配置或提示工程才能實現函數調用。使用者應注意這些解決方案的非官方性質以及潛在的不穩定性。

## 5\. Gemma 3 的函數調用支援

Gemma 3 官方支援函數調用和結構化輸出 。Google 的官方文件和部落格文章都證實了這一功能 。值得注意的是，Gemma 模型不輸出工具特定的 token，這意味著框架需要根據提示的函數輸出規範來檢測工具調用 。函數調用可以通過仔細的指令和提示工程來實現 。  

Gemma 3 受到 Ollama 框架的支援 。儘管 Ollama 函式庫中 Gemma 3 的頁面描述中並未明確提及 "tools"，但對該模型的一般支援表明整合是可能的 。Reddit 上的使用者報告稱，他們通過變通方法或增強版本在 Ollama 中成功實現了 Gemma 3 的工具調用 。Ollama 提供了配置模型的方法，這可能可以用於啟用 Gemma 3 的函數調用 。  

至於 llama.cpp 框架，Gemma 3 也受到支援 。`llama.cpp` 已經更新以支援 Gemma 3，並且使用者報告稱使用順利 。新增的 `llama-gemma3-cli` 為 Gemma 3 提供了一個專用介面，包括聊天和完成模式，這表明 Gemma 3 本身支援的函數調用應該可以實現 。此外，Gemma.cpp 是一個受到 llama.cpp 啟發的極簡實現，也支援 Gemma 3 。  

總之，Gemma 3 在設計上就具備函數調用能力，並且在 Ollama 和 llama.cpp 中都提供了支援。儘管 Ollama 的官方文件可能沒有明確強調工具支援，但社群的發現表明這是可以實現的。llama.cpp 已積極更新以包含 Gemma 3 的支援，這表示函數調用應該是可行的，可能需要按照 Google 的指南進行特定的提示或配置。

## 6\. Ollama 框架與函數調用支援

Ollama 是一個用於在本地運行 LLM 的框架，並提供 OpenAI 相容的 API 。這種相容性通常有助於函數調用的實現，因為許多 LLM 的設計都符合 OpenAI API 的函數調用慣例 。Ollama 支援匯入 GGUF 模型，這與使用 llama.cpp 中的模型，然後可能在 Ollama 中使用相關 。  

如第二節所述，Qwen 2.5 在 Ollama 中具有明確且有充分文檔記錄的工具調用支援。第三節提到，QwQ 在其 Ollama 函式庫條目中包含 "tools" 標籤，這暗示了某種程度的支援，儘管詳細資訊不太容易獲得。第四節強調了 Ollama 上存在社群修改版的 DeepSeek R1 模型，這些模型具有自訂的工具調用範本，因為官方模型缺乏原生支援。第五節指出，雖然 Ollama 支援 Gemma 3，但函數調用方面可能依賴於模型固有的能力以及 Google 文件中提到的潛在特定提示技術。

Ollama 以其易用性和 OpenAI API 相容性為特色，為使用各種 LLM 實現函數調用提供了一個有利的環境。支援程度可能因模型而異，有些模型（如 Qwen 2.5）具有明確的整合，而其他模型可能依賴於其原生能力或社群驅動的修改。

## 7\. llama.cpp 框架與函數調用支援

llama.cpp 是一個 C/C++ 函式庫，專注於在各種硬體上實現高效的 LLM 推論 。它支援各種量化方案和硬體加速 。`llama-cli` 工具用於與模型互動 。值得注意的是，llama.cpp 近期增加了對 OpenAI 風格函數調用的支援 。  

如第二節所述，Qwen 2.5 被列為在 llama.cpp 中具有原生工具調用格式支援的模型。第三節提到，雖然 QwQ 基於 Qwen 2.5 並且應該與 llama.cpp 相容，但所提供的資料中缺乏關於其函數調用支援的明確詳細資訊。第四節強調，DeepSeek R1 在 llama.cpp 中的函數調用支援標記為 "WIP"，可能尚未完全正常運作或易於直接使用。第五節確認 llama.cpp 支援 Gemma 3，並且 `llama-gemma3-cli` 提供了一個特定的介面，這表明 Gemma 3 支援的函數調用應該可以實現。

llama.cpp 正在發展以包含函數調用功能，並明確支援某些模型（如 Qwen 2.5 和 Gemma 3）。對於 DeepSeek R1，支援仍在開發中。QwQ 的使用者可能需要在 llama.cpp 中依賴其底層的 Qwen 2.5 功能。

## 8\. 比較分析與總結表

下表總結了本報告中分析的四種大型語言模型在 Ollama 和 llama.cpp 框架下的函數調用支援情況。

| **LLM 名稱** | **Ollama** | **llama.cpp** |
| --- |  --- |  --- |
| Qwen 2.5 | 是 (原生支援) | 是 (原生格式支援) |
| QwQ | 是 (存在 "tools" 標籤) | 可能 (基於 Qwen 2.5) |
| DeepSeek R1 | 部分 (社群修改版) | 部分 (開發中) |
| Gemma 3 | 是 (模型支援) | 是 (模型支援) |

## 9\. 結論

本報告分析了 Qwen 2.5、QwQ、DeepSeek R1 和 Gemma 3 這四種大型語言模型在 Ollama 和 llama.cpp 這兩個推論框架下的函數調用支援情況。分析顯示，Qwen 2.5 在這兩個框架下都提供了強大的原生支援，Ollama 的整合尤其順暢。QwQ 雖然基於 Qwen 2.5，並且在 Ollama 中有工具標籤，但其函數調用支援的具體程度仍有待進一步研究。DeepSeek R1 官方版本不支援函數調用，但社群在 Ollama 上進行了修改以提供部分支援，而 llama.cpp 的支援仍在開發中。Gemma 3 則官方支援函數調用，並且在 Ollama 和 llama.cpp 中都有相應的支援。

總體而言，Qwen 2.5 是目前看來在 Ollama 和 llama.cpp 中都提供最直接和完善函數調用支援的選擇。QwQ 的推理能力使其在某些應用場景下可能很有價值，但其函數調用支援可能需要更深入的探索。DeepSeek R1 雖然在推理方面表現出色，但在函數調用方面仍有不足，需要依賴社群的努力或等待官方的更新。Gemma 3 作為一個新興的模型，其官方的函數調用支援使其在兩個框架下都具有潛力。

對於開發者和研究人員而言，在選擇 LLM 和框架時，應仔細考慮其函數調用需求。如果需要開箱即用的函數調用功能，Qwen 2.5 和 Gemma 3 可能是較好的選擇。對於需要強大推理能力的使用者，QwQ 可能值得考慮，但需要注意其函數調用支援的現狀。DeepSeek R1 在函數調用方面可能需要更多的工作和客製化。隨著這些技術的不斷發展，未來可能會看到更多關於函數調用支援的增強和改進。

## 10\. 用來生成報告的資料來源

- [qwen.readthedocs\.io || llama.cpp - Qwen](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html)
- [qwen.readthedocs\.io || Ollama - Qwen](https://qwen.readthedocs.io/en/latest/run_locally/ollama.html)
- [reddit\.com || Where is qwen2.5 with tool training and 128k context? : r/LocalLLaMA - Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1hl2rmk/where_is_qwen25_with_tool_training_and_128k/)
- [github\.com || Qwen2.5 is the large language model series developed by Qwen team, Alibaba Cloud. - GitHub](https://github.com/QwenLM/Qwen2.5)
- [qwenlm.github\.io || Qwen2.5: A Party of Foundation Models! | Qwen](https://qwenlm.github.io/blog/qwen2.5/)
- [qwen.readthedocs\.io || Function Calling - Qwen](https://qwen.readthedocs.io/en/latest/framework/function_call.html)
- [github\.com || llama.cpp/docs/function-calling.md at master - ggml-org/llama.cpp - GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md)
- [python.langchain\.com || Llama.cpp - ️ LangChain](https://python.langchain.com/docs/integrations/chat/llamacpp/)
- [ollama\.com || qwen2.5 - Ollama](https://ollama.com/library/qwen2.5)
- [reddit\.com || PSA: Local LLM finally working, Qwen 2.5 + Ollama in Home Assistant Reliably Executes Function Calls and Controls My House at GPT-4o-Mini Level : r/homeassistant - Reddit](https://www.reddit.com/r/homeassistant/comments/1fkzihk/psa_local_llm_finally_working_qwen_25_ollama_in/)
- [ollama\.com || qwq - Ollama](https://ollama.com/library/qwq)
- [alibabacloud\.com || Alibaba Cloud Model Studio:Deep thinking (QwQ)](https://www.alibabacloud.com/help/en/model-studio/user-guide/qwq)
- [reddit\.com || QwQ - Best Way to Separate Thought Process from Final Output? : r/LocalLLaMA - Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1h2n4ct/qwq_best_way_to_separate_thought_process_from/)
- [github\.com || QwQ is the reasoning model series developed by Qwen team, Alibaba Cloud. - GitHub](https://github.com/QwenLM/QwQ)
- [medium\.com || Alibaba's QWQ 32B: The Compact AI Model That Rivals DeepSeek R1 | by Tahir | Mar, 2025 | Medium](https://medium.com/@tahirbalarabe2/alibabas-qwq-32b-the-compact-ai-model-that-rivals-deepseek-r-0d7b57d585e2)
- [groq\.com || A Guide to Reasoning with Qwen QwQ 32B - Groq is Fast AI Inference](https://groq.com/a-guide-to-reasoning-with-qwen-qwq-32b/)
- [qwenlm.github\.io || QwQ: Reflect Deeply on the Boundaries of the Unknown - Qwen](https://qwenlm.github.io/blog/qwq-32b-preview/)
- [alibabacloud\.com || Alibaba Cloud Unveils QwQ-32B: A Compact Reasoning Model with Cutting-Edge Performance](https://www.alibabacloud.com/blog/alibaba-cloud-unveils-qwq-32b-a-compact-reasoning-model-with-cutting-edge-performance_602039)
- [datacamp\.com || How to Set Up and Run QwQ-32B Locally With Ollama - DataCamp](https://www.datacamp.com/tutorial/qwq-32b-ollama)
- [youtube\.com || QWQ 32B on Ollama - Model That Reflects Deeply - Thorough Local Testing - YouTube](https://www.youtube.com/watch?v=G1-X4XB_HHM)
- [medium\.com || Running LLaMA Locally with Llama.cpp: A Complete Guide | by Mostafa Farrag - Medium](https://medium.com/hydroinformatics/running-llama-locally-with-llama-cpp-a-complete-guide-adb5f7a2e2ec)
- [youtube\.com || Prompt Chaining with Qwen and QwQ reasoning model (Ollama + LLM) - YouTube](https://www.youtube.com/watch?v=YoeNwp9je6E)
- [github\.com || ollama/ollama: Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 3, and other large language models. - GitHub](https://github.com/ollama/ollama)
- [github\.com || ggml-org/llama.cpp: LLM inference in C/C++ - GitHub](https://github.com/ggml-org/llama.cpp)
- [datacamp\.com || I Tested QwQ 32B Preview: Alibaba's Reasoning Model - DataCamp](https://www.datacamp.com/blog/qwq-32b-preview)
- [github\.com || deepseek r1 (with tool calling) - Issue #877 - block/goose - GitHub](https://github.com/block/goose/issues/877)
- [docs.openwebui\.com || Run DeepSeek R1 Dynamic 1.58-bit with Llama.cpp - Open WebUI](https://docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/)
- [datacamp\.com || How to Set Up and Run DeepSeek-R1 Locally With Ollama - DataCamp](https://www.datacamp.com/tutorial/deepseek-r1-ollama)
- [github\.com || Issue #9 - deepseek-ai/DeepSeek-R1 - Function calling - GitHub](https://github.com/deepseek-ai/DeepSeek-R1/issues/9)
- [qualcomm\.com || Run DeepSeek Models on Windows on Snapdragon Llama.cpp and MLC-LLM tutorial](https://www.qualcomm.com/developer/blog/2025/02/how-to-run-deepseek-windows-snapdragon-tutorial-llama-cpp-mlc-llm)
- [youtube\.com || How to do Tool Calling with DeepSeek R1 - YouTube](https://www.youtube.com/watch?v=hA_m5mOYZxA)
- [daehnhardt\.com || DeepSeek R1 With Ollama - Elena Daehnhardt](https://daehnhardt.com/blog/2025/01/28/deepseek-with-ollama/)
- [dataleadsfuture\.com || Integrating LlamaIndex and DeepSeek-R1 for reasoning\_content and Function Call Features - Data Leads Future](https://www.dataleadsfuture.com/integrating-llamaindex-and-deepseek-r1-for-reasoning_content-and-function-call-features-2/)
- [ollama\.com || MFDoom/deepseek-r1-tool-calling - Ollama](https://ollama.com/MFDoom/deepseek-r1-tool-calling)
- [adasci.org: Implementing DeepSeek-R1 Locally through Llama.cpp - Association of Data Scientists](https://adasci.org/implementing-deepseek-r1-locally-through-llama-cpp/)
- [ollama\.com || MFDoom/deepseek-r1-tool-calling/template - Ollama](https://ollama.com/MFDoom/deepseek-r1-tool-calling/blobs/e835211bc0fb)
- [modal\.com || Run large and small language models with llama.cpp (DeepSeek-R1, Phi-4) | Modal Docs](https://modal.com/docs/examples/llama_cpp)
- [ollama\.com || deepseek-r1 - Ollama](https://ollama.com/library/deepseek-r1)
- [ai.plainenglish\.io || Function Calling : The Superpower DeepSeek R1 Doesn't Have (Yet!) | by Anix Lynch, MBA, ex-VC - Artificial Intelligence in Plain English](https://ai.plainenglish.io/function-calling-the-superpower-deepseek-r1-doesnt-have-yet-c80ef6f9057d)
- [reddit\.com || DeepSeek-R1 optimizes the llama.cpp WASM runtime by leveraging SIMD instructions -x2 Speed Increase - the whole PR is 99% R1 : r/singularity - Reddit](https://www.reddit.com/r/singularity/comments/1ibew93/deepseekr1_optimizes_the_llamacpp_wasm_runtime_by/)
- [teetracker.medium\.com || Ollama Workaround: DeepSeek R1 Tool Support | by TeeTracker | Feb, 2025 - Medium](https://teetracker.medium.com/ollama-workaround-deepseek-r1-tool-support-c64dbb924da1)
- [dev.to: Setting Up Ollama & Running DeepSeek R1 Locally for a Powerful RAG System](https://dev.to/ajmal_hasan/setting-up-ollama-running-deepseek-r1-locally-for-a-powerful-rag-system-4pd4)
- [reddit\.com || Gemma 3 support? : r/Oobabooga - Reddit](https://www.reddit.com/r/Oobabooga/comments/1jalcvk/gemma_3_support/)
- [blog.google: Introducing Gemma 3: The most capable model you can run on a single GPU or TPU](https://blog.google/technology/developers/gemma-3/)
- [ai.google\.dev || Run Gemma with Ollama | Google AI for Developers - Gemini API](https://ai.google.dev/gemma/docs/integrations/ollama)
- [github\.com || Experimental playground for Gemma 3 vision - ggml-org llama.cpp - Discussion #12348 - GitHub](https://github.com/ggml-org/llama.cpp/discussions/12348)
- [dev.to: A Step-by-Step Guide to Install Gemma-3 Locally with Ollama or Transformers](https://dev.to/nodeshiftcloud/a-step-by-step-guide-to-install-gemma-3-locally-with-ollama-or-transformers-12g6)
- [ai.google\.dev || Gemma.cpp tutorial | Google AI for Developers - Gemini API](https://ai.google.dev/gemma/docs/core/gemma_cpp)
- [datacamp\.com || How to Set Up and Run Gemma 3 Locally With Ollama - DataCamp](https://www.datacamp.com/tutorial/gemma-3-ollama)
- [developers.googleblog\.com || Introducing Gemma 3: The Developer Guide](https://developers.googleblog.com/en/introducing-gemma3/)
- [apidog\.com || How to Run Gemma 3 Locally Using Ollama ? - Apidog](https://apidog.com/blog/run-gemma-3-locally-with-ollama/)
- [ai.google\.dev || Function calling with Gemma | Google AI for Developers - Gemini API](https://ai.google.dev/gemma/docs/capabilities/function-calling)
- [ollama\.com || gemma3 - Ollama](https://ollama.com/library/gemma3)
- [philschmid.de || Google Gemma 3 Function Calling Example](https://www.philschmid.de/gemma-function-calling)
- [reddit\.com || Does Gemma 3 support tool calling? : r/LocalLLM - Reddit](https://www.reddit.com/r/LocalLLM/comments/1jf5u0m/does_gemma_3_support_tool_calling/)
