# markitdown

> Python tool for converting files and office documents to Markdown.

> [!TIP]
> MarkItDown now offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop. See [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) for more information.

- Git Repo
  - https://github.com/microsoft/mardocxkitdown

## 2025-10-13

- 這個主要是從 Github MCP Registry 看到的
  - https://github.com/mcp

### Install

- 實驗用 `uv` 安裝
- 環境：
  ```bash
  OS: Windows 11 Home x86_64
  Host: ASUSTeK COMPUTER INC. ASUS TUF Gaming A15 FA507NV_FA507NV
  ```
- 步驟：
  ```bash
  ~/git/snippet$ uv tool install markitdown[all]
  ```
- 驗證：
  ```bash
  ~/git/snippet$ which markitdown
  /c/Users/jazzw/.local/bin/markitdown
  ```
- 測試：
  - Test Case #1 -- convert Slides PDF into Markdown
```bash
~/Downloads$ markitdown Crew\ AI.pdf -o Crew_AI.md
Cannot set gray stroke color because /'P7' is an invalid float value
Cannot set gray non-stroke color because /'P7' is an invalid float value
Cannot set gray stroke color because /'P8' is an invalid float value
Cannot set gray non-stroke color because /'P8' is an invalid float value
Cannot set gray stroke color because /'P4' is an invalid float value
Cannot set gray non-stroke color because /'P4' is an invalid float value
Cannot set gray stroke color because /'P5' is an invalid float value
Cannot set gray non-stroke color because /'P5' is an invalid float value
Cannot set gray stroke color because /'P7' is an invalid float value
Cannot set gray non-stroke color because /'P7' is an invalid float value
Cannot set gray stroke color because /'P10' is an invalid float value
Cannot set gray non-stroke color because /'P10' is an invalid float value
Cannot set gray stroke color because /'P11' is an invalid float value
Cannot set gray non-stroke color because /'P11' is an invalid float value
Cannot set gray stroke color because /'P4' is an invalid float value
Cannot set gray non-stroke color because /'P4' is an invalid float value
Cannot set gray stroke color because /'P5' is an invalid float value
Cannot set gray non-stroke color because /'P5' is an invalid float value
Cannot set gray stroke color because /'P6' is an invalid float value
Cannot set gray non-stroke color because /'P6' is an invalid float value
Cannot set gray stroke color because /'P4' is an invalid float value
Cannot set gray non-stroke color because /'P4' is an invalid float value
Cannot set gray stroke color because /'P5' is an invalid float value
Cannot set gray non-stroke color because /'P5' is an invalid float value
Cannot set gray stroke color because /'P4' is an invalid float value
Cannot set gray non-stroke color because /'P4' is an invalid float value
Cannot set gray stroke color because /'P5' is an invalid float value
Cannot set gray non-stroke color because /'P5' is an invalid float value
```
  - Test Case #2 -- convert Word PDF to Markdown
```bash
~/Downloads$ markitdown 台灣資料結構專家分析.pdf -o 台灣資料結構專家分析.md
```
  - Test Case #3 -- convert DOCX to Markdown
```bash
~/Downloads$ markitdown "Job Description_AI ML Engineer.docx" -o "Job Description_AI ML Engineer.md"
```
- 結論：
  - 感覺 PDF 轉 Markdown 很多原有格式會跑掉，像是 Table 表格。實測兩種不同原始檔案（投影片跟 Google Docs 匯出的 PDF）都只能產生類似 plain text 的輸出。
  - `.docx` 轉 Makrdown，表現比 PDF 好很多。