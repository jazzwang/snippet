# QMD

- Git Repo
  - https://github.com/tobi/qmd

> mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local

## 2026-06-06

- 緣起：
  - 印象先前有看到，跟 LLM Wiki 有關
  - https://rar.design/posts/obsidian-ai-second-brain-2026 提到
  > Karpathy 上個月在 X 丟了一句話，1600 萬人看，5000 人在 GitHub Gist 收藏。內容只有一個概念：「把你的筆記丟進一個資料夾，叫 LLM 幫你整理。」
  > 一個禮拜後，半個矽谷工程師圈在做同一件事——把 Notion 裡的東西搬回 Obsidian。Reddit、Threads、設計師圈都在傳這個工作流，<mark>連 Shopify 的 Tobi Lutke 都跳下來寫了一個叫 QMD 的本地搜尋引擎來支援這個流派</mark>。
  - https://ohya.co/blog/qmd-local-search-for-openclaw
    - 看起來合適跟 Agent 整合在一起。
    - 本地模型 - 需要 2 GB 硬碟空間
- 研究：
  - 比較 QMD 與 Obsidian 

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
QMD (https://github.com/tobi/qmd) 與 Obsidian (https://obsidian.md/) 的優缺點 side-by-side 比較表
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr><td>A:</td><td>

QMD (Query Markup Documents) 與 Obsidian 是兩款定位完全不同的工具：QMD 是一個專為 AI 與終端機設計的本地「智慧搜尋引擎」，而 Obsidian 則是一套面向人類用戶的「視覺化知識管理與筆記軟體」。 [1, 2, 3, 4, 5] 

以下為兩者的優缺點 Side-by-Side 橫向對比表：

## QMD 與 Obsidian 優缺點對比

| 比較維度 [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] | QMD (tobi/qmd) | Obsidian |
|---|---|---|
| 主要定位 | 本地端 AI 混合搜尋側車 (Sidecar) 與檢索工具 | 個人知識管理 (PKM) 與 Markdown 筆記軟體 |
| 主要優點 | 強大 AI 檢索：結合 BM25、向量語意搜尋與本地 LLM 重排（Reranking）。AI 工作流最佳化：原生支援 MCP 協定，完美整合 Claude Code 等 AI 代理。節省 Token：智慧分塊（Chunking）只讀取相關片段，大幅節省 AI 脈絡視窗消耗。無介面輕量：全本地運行，無 UI 負擔，速度極快。 | 極佳視覺體驗：擁有完整的圖形化介面（GUI）與即時雙向連結（Backlinks）。生態系龐大：上千款社群外掛（如 Dataview、看板、日誌）與主題可供高度客製化。多端同步與行動版：支援 Windows、Mac、Linux、iOS 及 Android，有多種同步選擇。雙向連結網路：強大的知識圖譜（Graph View），方便人類大腦進行網狀思考。 |
| 主要缺點 | 無圖形介面：全靠 CLI 終端機指令或 AI 呼叫，不適合日常打字做筆記。硬體門檻較高：本地跑嵌入（Embedding）與 LLM 重排需要消耗一定的 CPU/GPU 資源。無編輯/組織功能：它只是個「搜尋引擎」，無法幫你建立標籤、分類或雙向連結。 | 傳統搜尋較弱：內建搜尋主要依賴精準關鍵字字面匹配，缺乏概念性的模糊語意理解。AI 整合需外掛：原生不帶本地向量資料庫，需依靠 Smart Connections 等第三方外掛才能實現 AI 檢索。上手難度高：進階功能（如 Dataview 語法、外掛配置）需要一定的學習曲線。 |
| 使用者介面 | 無 GUI（純命令列 CLI 或 MCP API 接口） | 富文字 Markdown 圖形介面、關聯圖譜 |
| 互動對象 | AI 代理（Agents）、開發者、終端機重度使用者 | 人類筆記記者、研究人員、知識工作者 |

## 兩者如何做出選擇？

* 選擇 QMD 的場景：如果您是一名開發者，或者正在構建基於 AI Agents 的本地工作流（例如 [Claude Code](https://github.com/tobi/qmd)），且擁有數千個 Markdown 檔案或技術文件，希望 AI 能在不翻遍整個資料夾的情況下精準撈出最相關的段落，QMD 是極佳的後端檢索側車。 [6, 7, 8] 
* 選擇 Obsidian 的場景：如果您需要一個日常記錄想法、寫日記、管理專案進度、構建第二大腦的工具，且需要舒適的閱讀與動手編輯體驗，那麼擁有強大外掛生態與跨平台介面的 Obsidian 絕對是首選。 [5, 16] 

> 💡 最佳實踐（強強聯手）：
> 實際上這兩者完全不衝突。社群上許多科技愛好者的作法是：<mark>使用 Obsidian 作為前端</mark>來撰寫、儲存與視覺化管理所有的 Markdown 筆記（Vault），同時在後端<mark>利用 QMD 去索引 Obsidian 的資料夾</mark>。這樣一來，人類可以在 Obsidian 享受精美的圖形介面，而 AI 夥伴也可以透過 QMD 獲得極高效率的本地語意檢索能力！ [3, 5, 8, 13] 

如果您想嘗試這種組合，您可以告訴我您的操作系統（Mac/Windows）與日常使用的 AI 工具（如 Claude Code），我可以為您說明如何將 QMD 配置到您的 Obsidian 筆記庫中。

[1] [https://github.com](https://github.com/tobi/qmd)
[2] [https://www.linkedin.com](https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-activity-7425244479009239040-6TIF)
[3] [https://hellogithub.com](https://hellogithub.com/en/repository/tobi/qmd)
[4] [https://medium.com](https://medium.com/coding-nexus/qmd-local-hybrid-search-engine-for-markdown-that-cuts-token-usage-by-95-e0f9d21f89af)
[5] [https://vocus.cc](https://vocus.cc/article/653fc240fd8978000108baed)
[6] [https://docs.openclaw.ai](https://docs.openclaw.ai/concepts/memory-qmd)
[7] [https://www.facebook.com](https://www.facebook.com/philipzh/posts/qmd-obsidian-claude-code%E6%90%9C%E5%B0%8B%E7%B5%90%E6%9E%9C%E8%B7%9Fobsidian-cli%E6%9C%89%E5%B7%AE%E7%95%B0httpsgithubcomtobiqmd/10166625080108765/)
[8] [https://mcpmarket.com](https://mcpmarket.com/tools/skills/quick-markdown-search-qmd)
[9] [https://github.com](https://github.com/tobi/qmd/blob/main/README.md)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=123cqKLy6lc)
[11] [https://alexanderzeitler.com](https://alexanderzeitler.com/articles/introducing-lazyqmd-a-tui-for-qmd/)
[12] [https://github.com](https://github.com/tobi/qmd/activity?ref=main)
[13] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=46689289)
[14] [https://github.com](https://github.com/tobi/qmd?ref=aitoolnet.com)
[15] [https://github.com](https://github.com/tobi/qmd?ref=jarsen.engineer)
[16] [https://www.reddit.com](https://www.reddit.com/r/ObsidianMD/comments/z6hkzy/obsidian_vs_everything_else/?tl=zh-hant)

</td></tr>
</table>

- 根據比較結果，混合兩個工具反而是最好的作法：
  - Obsidian 給人寫筆記用
  - QMD 給 AI Agent 索引用