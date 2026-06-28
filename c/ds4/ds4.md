# ds4

- Git Repo
  - https://github.com/antirez/ds4

> DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm

## 2026-06-28

- Read from AlphaSignal
  - 2026-05-12
  - Local 284B parameter model runs on MacBook Pro at 26 tokens/sec
  - 這是 Redis 作者的作品

> [!NOTE]
> Antirez, the person who built Redis, just shipped **ds4**: a custom engine that runs DeepSeek V4 Flash, a massive **284B parameter AI model**, fully on your MacBook. No cloud. No API costs.
>
> How is that even possible? Two tricks. First, the model gets compressed to 2-bit weights (think of it as shrinking a huge file without losing much quality), which squeezes it down to fit in **128GB of RAM**. Second, instead of keeping everything in memory, the conversation history gets saved to your SSD, so long sessions stay fast without eating your RAM.
>
> Here is what this unlocks for you:
>
> -   A **1 million token context window**, meaning you can feed it entire codebases at once
> -   Works as a local backend for Claude Code, opencode, and Pi via a drop-in OpenAI/Anthropic-compatible API
> -   Generates at 26 tokens per second on an M3 Max MacBook Pro
> 
> You start it with git clone, run **./download\_model.sh q2**, then make, and point your coding agent at localhost:8000.
>
> Redis 的創辦人 Antirez 剛剛發布了 **ds4**：一個客製化引擎，可在你的 MacBook 上完全運行 DeepSeek V4 Flash，這是一個擁有 **284 億參數的龐大 AI 模型**。無需雲端，也無需支付 API 費用。
>
> 這怎麼可能？有兩個技巧。首先，模型被壓縮成 2 位元權重（可以理解為在不損失太多品質的情況下縮小一個大檔案），這樣就能將其壓縮到 **128GB 的​​記憶體**中。其次，對話歷史記錄不會全部保存在記憶體中，而是保存到固態硬碟 (SSD) 上，因此即使長時間會話也能保持流暢，不會佔用太多記憶體。
> 
> 這將為你解鎖以下內容：
> 
> -   一個 **可容納 100 萬個令牌的上下文窗口**，這意味著您可以一次性向其提供整個程式碼庫。
> -   可透過即插即用的 OpenAI/Anthropic 相容 API，作為 Claude Code、opencode 和 Pi 的本機後端運作。
> -   在 M3 Max MacBook Pro 上每秒產生 26 個令牌
> 
> 先使用 git clone 指令，執行 **./download\_model.sh q2 指令**，然後執行 make 指令，並將你的編碼代理指向 localhost:8000。