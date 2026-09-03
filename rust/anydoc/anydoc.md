# anydoc

- Git Repo
  - https://github.com/firecrawl/anydoc
- Website
  - https://firecrawl.github.io/anydoc/

> [!NOTE]
> Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown. Built in Rust, with Node.js and Python bindings.

## 2026-08-17

- Read from: https://www.linkedin.com/feed/update/urn:li:activity:7493676437913395200

> [!NOTE]
> 快速把任何辦公文件轉成乾淨的 Markdown？！
>
> Firecrawl 開源 anydoc，支援將 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF 統一轉換成 GitHub-Flavored Markdown，連 .doc、.ppt、.xls 這類舊格式都在支援範圍內。
>
> anydoc 會將所有格式都先解析進同一套文件模型，再由單一 Markdown 序列化器輸出，所以不論輸入是二十年前的 .doc 還是昨天做的 .pptx，表格、註腳、清單編號的處理都一致。另外格式判斷是讀檔案內容本身的標記，副檔名標錯的檔案照樣轉得出來。
>
> 效能是它的主打。純 Rust、不載入任何 ML 模型、不呼叫外部服務，中位轉換時間低於 5 毫秒。官方 benchmark 拿 100 份真實文件、橫跨十四種格式，與另外六套轉換器對比，由 LLM 評審盲測比對 LibreOffice 渲染的原始頁面，結果 anydoc 是唯一覆蓋全部十四種格式的工具，每一種格式的品質分數都最高，速度也比次快的工具快一個量級。