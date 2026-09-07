# Tantivy 全文索引技術摘要

- Git Repo
  - https://github.com/quickwit-oss/tantivy
- Website
  - https://docs.rs/tantivy/latest/tantivy/

> [!NOTE]
> Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust

## 2026-09-07

- 緣起：
  - 在研究 [rust/utopia](../utopia/utopia.md) 時，看到的 Tantivy 全文搜尋引擎
- 技術摘要：

> [!QUESTION]
> 請透過 web search 搜尋並整理關於 Tantivy 全文索引的技術摘要，並儲存到 rust/tantivy/tantivy.md

> Tantivy 是以 Rust 撰寫、受 Apache Lucene 設計啟發的全文搜尋函式庫，不是像 Elasticsearch 或 Solr 那樣的獨立搜尋伺服器。

## 1. 定位與核心特性

Tantivy 是 Rust 生態中的 Lucene 類型搜尋引擎核心，可嵌入應用程式，建立本地或服務內的全文索引。

- 倒排索引（inverted index）
- BM25 相關性評分
- 布林、詞組、範圍、模糊、Regex 等查詢
- 增量索引與多執行緒索引
- 分段索引（segment-based index）
- 背景合併 segments
- mmap 目錄存取
- 壓縮文件儲存
- Fast fields，概念類似 Lucene 的 DocValues
- Faceted search 與部分聚合功能
- 可自訂 tokenizer 與 token filter
- 支援文字、數值、日期、IP、布林、Facet、JSON 等欄位類型

Tantivy 本身不負責分散式搜尋；需要叢集、分片或分散式儲存時，可使用建立在 Tantivy 之上的 Quickwit。

## 2. 索引的基本資料結構

Tantivy 的索引由多個 **segment** 組成：

```text
Index
├── Segment A
├── Segment B
└── Segment C
```

每個 segment 都是可獨立搜尋的索引單位，包含以下資料：

1. **Term dictionary**
   - 儲存排序後的 term。
   - 將 term 對應至該 term 的索引資訊，例如 postings 的位置與統計資料。

2. **Postings / inverted lists**
   - 記錄某個 term 出現在哪些文件。
   - 可包含 document ID、term frequency 與 term position。
   - Tantivy 的 postings 模組實作倒排索引；`SegmentPostings` 代表某個 term 在單一 segment 中的 postings list。

3. **Field norms**
   - 記錄文件欄位長度等資訊。
   - BM25 評分會利用欄位長度進行正規化。

4. **Document store**
   - 儲存原始文件欄位，供搜尋命中後取回。
   - 它是 row-oriented、可壓縮的儲存區。
   - 只有設為 `STORED` 的欄位，才會在搜尋結果中透過 `Searcher::doc()` 取回。

5. **Fast fields**
   - 以 column-oriented 方式儲存欄位值。
   - 適合依 document ID 快速讀取欄位，例如排序、聚合、評分或篩選。
   - 概念上相當於 Lucene 的 DocValues。

## 3. `INDEXED`、`STORED` 與 `FAST` 的差異

欄位旗標決定該欄位能否搜尋、取回、排序或聚合。

| 設定 | 作用 | 常見用途 |
|---|---|---|
| `INDEXED` | 建立可搜尋的索引 | term query、範圍查詢 |
| `STORED` | 保存原始欄位值 | 搜尋結果顯示標題、內容 |
| `FAST` | 建立可依 doc ID 快速讀取的欄式資料 | 排序、聚合、評分、快速篩選 |
| `TEXT` | Tokenize 後建立文字索引 | 一般全文搜尋 |
| `STRING` | 不切詞，整個值視為一個 term | ID、URL、標籤 |

例如：

```rust
schema_builder.add_text_field("title", TEXT | STORED);
schema_builder.add_text_field("body", TEXT);
schema_builder.add_u64_field("views", INDEXED | FAST | STORED);
```

這段設定表示：

- `title` 可全文搜尋，也可在結果中取回。
- `body` 可全文搜尋，但不保存原文。
- `views` 可做數值查詢、排序或聚合，也可取回原始值。

`INDEXED` 與 `STORED` 是兩個獨立概念。欄位能被搜尋，不代表可以取回原始內容；欄位被儲存，也不代表可以用來搜尋。

## 4. Tokenizer 與文字分析流程

全文索引會先把文字轉換成 token：

```text
原始文字
  ↓
Tokenizer
  ↓
Token filter
  ↓
Term / position
  ↓
倒排索引
```

Tantivy 內建的 tokenizer 包括：

### `default`

預設 tokenizer 通常會：

- 依空白與標點切分
- 將文字轉成小寫
- 移除超過長度限制的 token

### `raw`

不進行實際切詞，整個欄位值視為一個 token，適合 UUID、URL、程式碼識別字與精確比對欄位。

### `en_stem`

在基本切詞與小寫化之後，再進行英文 stemming，以改善召回率。不同字形可能被歸納為相近的詞根。

Tantivy 也支援自訂 tokenizer 與 token filter，例如：

- lowercase
- stop-word removal
- stemming
- ASCII folding
- n-gram
- regex tokenizer
- whitespace tokenizer

每個文字欄位都應在 schema 中指定 tokenizer。中文、日文與韓文通常需要整合語言專用的斷詞器，不能直接依賴預設 tokenizer。

### 中文使用上的注意事項

Tantivy 預設 tokenizer 不適合中文語意切詞。中文通常需要使用第三方 tokenizer，例如：

- `tantivy-jieba`
- `cang-jie`
- Lindera
- 其他自訂 `Tokenizer`

直接使用預設 tokenizer 可能無法正確切分中文詞語，降低搜尋的召回率與精確度。

## 5. `IndexRecordOption` 與索引資訊量

文字欄位可以選擇保存多少索引資訊。常見概念包括：

- 僅保存 term 是否出現
- 保存詞頻（term frequency）
- 保存詞頻與位置（positions）

保存詞頻與位置會增加索引大小，但可支援 BM25 評分與詞組查詢。

| 索引資訊 | 可支援的能力 |
|---|---|
| Basic | 基本 term 搜尋 |
| WithFreqs | 利用詞頻進行評分 |
| WithFreqsAndPositions | BM25、詞組查詢、位置相關功能 |

例如詞組查詢：

```text
"distributed search engine"
```

詞組查詢需要讀取詞項位置，因此欄位必須保存 positions。只使用基本索引資訊的欄位，無法支援依賴詞頻或位置的功能。

## 6. 寫入流程與 segment 生命週期

Tantivy 的索引寫入由 `IndexWriter` 負責：

```text
add_document()
      ↓
記憶體中的 indexing pipeline
      ↓
建立新的 segment
      ↓
commit()
      ↓
新 segment 對搜尋可見
      ↓
背景 merge
```

### 寫入流程

1. 建立 schema。
2. 建立 `Index`。
3. 取得 `IndexWriter`。
4. 加入文件。
5. `commit()`。
6. 由 `IndexReader` 重新載入索引。
7. 取得新的 `Searcher` 執行查詢。

`IndexWriter` 會管理索引執行緒與共享佇列；每個索引執行緒都能透過 `SegmentWriter` 建立獨立的 segment。

### `commit()` 的語意

`commit()` 會：

- 等待待處理的文件完成索引
- 將目前結果 flush 到磁碟
- 發布新的索引版本
- 使修改具備持久性

文件必須在 `commit()` 後才會對搜尋可見。既有的 `Searcher` 不會自動反映新資料；重新載入 `IndexReader` 後，必須取得新的 `Searcher`。

### Merge

持續寫入會產生許多小 segment。Tantivy 會在背景執行 segment merge，將多個 segment 合併成較大的 segment，以減少：

- 搜尋時需要掃描的 segment 數量
- 檔案與 metadata 數量
- 重複 term dictionary 的成本

Merge 會消耗 CPU、磁碟 I/O 與暫存空間；部署時應設定合適的 merge policy，並為這些工作保留資源。

## 7. 文件更新與刪除模型

Tantivy 的索引資料具有 immutable 特性：

- 文件不是直接原地更新。
- 更新通常等同於刪除舊文件，再重新索引新文件。
- 刪除操作也會在 commit 後才對讀取端可見。
- 已被刪除的文件可能要等到 segment merge 後，才真正從底層索引資料中清除。

這種 immutable 設計簡化了讀取端的索引管理，但大量更新時要留意：

- delete tombstones 的累積
- merge 的 I/O 成本
- index size 暫時增加
- commit 頻率與延遲之間的取捨

## 8. 查詢模型與評分

Tantivy 使用 `Query` trait 抽象查詢，常見查詢類型包括：

- `TermQuery`
- `BooleanQuery`
- `PhraseQuery`
- `RangeQuery`
- `FuzzyTermQuery`
- `RegexQuery`
- `ExistsQuery`
- `MoreLikeThisQuery`
- `FastFieldRangeQuery`
- `InvertedIndexRangeQuery`

### Query Parser

查詢語法例如：

```text
rust AND search
"title of book"
views:10
views:[10 TO 100]
(title:rust OR body:lucene)
```

可用的查詢語法取決於 schema 中的欄位名稱、欄位型別與索引選項。

### BM25

Tantivy 使用 BM25 作為主要文字相關性評分方法，與 Lucene 的評分方式相近。BM25 通常會考慮：

- query term 是否出現
- 詞頻（term frequency）
- 文件頻率
- 文件欄位長度
- 詞項的稀有程度

## 9. 搜尋執行模型

搜尋流程如下：

```text
Query
  ↓
Query Parser / Query object
  ↓
對每個 segment 建立 scorer
  ↓
讀取 term dictionary 與 postings
  ↓
合併各 segment 的結果
  ↓
Collector 排序、取 Top-N 或聚合
  ↓
依 DocAddress 取回 stored fields
```

Tantivy 的 `Searcher` 會對目前可見的 segments 建立 `SegmentReader`，每個 segment 個別執行查詢，再將結果合併。

常見的 collector 包括：

- Top documents
- Count
- 聚合（Aggregation）
- Facet
- 統計與分組

搜尋會先透過索引與評分找出文件 ID，再依需求讀取少量儲存欄位，不必一開始載入所有原始文件。

## 10. 儲存與效能設計

### mmap

Tantivy 支援 mmap directory，以 memory mapping 存取索引檔案，可：

- 減少額外的使用者空間 buffer 複製
- 利用作業系統 page cache
- 加快重複查詢的資料存取
- 降低啟動時完整載入索引的需求

### 壓縮

Stored documents 可使用壓縮儲存，例如：

- LZ4
- Zstd
- 不壓縮

LZ4、Zstd 與不壓縮會在 CPU 使用量、磁碟空間和讀取延遲之間呈現不同取捨，應依工作負載選擇。

### SIMD 與壓縮 postings

Tantivy 使用整數壓縮與部分 SIMD 優化，以降低 postings 的儲存空間與讀取成本。實際效能會受到以下因素影響：

- 查詢類型
- term 的 document frequency
- segment 數量
- index size
- CPU 與記憶體
- 頁面快取（page cache）狀態
- Top-N 大小
- 是否需要計算評分

因此，評估實際效能時應使用目標資料集與查詢負載自行測試。

## 11. Tantivy 的優點與限制

### 優點

- Rust 原生實作，適合嵌入式搜尋場景。
- 與 Lucene 類似的 segment、倒排索引與 BM25 架構。
- 不需要額外啟動搜尋伺服器。
- 啟動時間短，適合 CLI、桌面應用及單機服務。
- schema、tokenizer 與 query API 可程式化控制。
- 同時支援全文搜尋、結構化欄位與聚合。
- 可透過第三方 tokenizer 支援非英文語言。
- 支援多執行緒索引與背景 segment merge。

### 限制

- 本身不是分散式搜尋服務。
- 不提供 Elasticsearch 等級的完整叢集管理、複寫與分片功能。
- schema 屬於較嚴格的預先定義模型。
- 文件更新採刪除加重新索引，非原地修改。
- 中文、日文、韓文需自行選擇並整合斷詞器。
- commit 與 merge 的資源消耗需要應用程式自行規劃。
- 使用者必須自行處理服務 API、權限、備份、監控與高可用性。

## 12. 適合的使用情境

適用情境包括：

- Rust 應用程式內嵌全文搜尋
- 本機文件搜尋
- CLI 搜尋工具
- 郵件、訊息、日誌與知識庫索引
- 中小型單機搜尋服務
- 需要低延遲與低部署複雜度的產品
- 作為更高階分散式搜尋系統的底層索引引擎

需要以下能力時，應搭配 Quickwit 或其他搜尋平台：

- 多節點分散式搜尋
- 自動 shard 與 replica 管理
- 大規模叢集
- 雲端物件儲存整合
- 跨節點容錯與彈性擴展

## 13. 簡化版架構總結

```text
文件
  ↓
Schema 決定欄位型別與索引選項
  ↓
Tokenizer / Token Filter
  ↓
Term、頻率、位置
  ↓
倒排索引 + term dictionary
  ↓
多個 immutable segments
  ↓
背景 merge
  ↓
Searcher
  ↓
Query / BM25 / Collector
  ↓
DocAddress
  ↓
Stored fields / Fast fields
```

## 參考資料

- [Tantivy GitHub repository](https://github.com/quickwit-oss/tantivy)
- [Tantivy API documentation](https://docs.rs/tantivy/latest/tantivy/)
- [Postings module](https://docs.rs/tantivy/latest/tantivy/postings/index.html)
- [Schema module](https://docs.rs/tantivy/latest/tantivy/schema/index.html)
- [Tokenizer module](https://docs.rs/tantivy/latest/tantivy/tokenizer/index.html)
- [Query module](https://docs.rs/tantivy/latest/tantivy/query/index.html)
- [IndexWriter API](https://docs.rs/tantivy/latest/tantivy/indexer/struct.IndexWriter.html)
- [Tantivy on crates.io](https://crates.io/crates/tantivy)
