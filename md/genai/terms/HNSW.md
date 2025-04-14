# Hierarchical Navigable Small World (HNSW)

## 2024-06-30

### pgvector + pgvectorscale vs pinecone

- 本來想說來比較一下 pgvector 跟 pinecone 兩個效能會差多少呢？
- 2024-04-17 : [Pinecone vs. Postgres pgvector: For vector search, easy isn’t so easy](https://www.pinecone.io/blog/pinecone-vs-pgvector/)
  - 本文提到了一些 pgvector 的缺點，像是用 HNSW index 太耗費記憶體（所以成本太高）

## 2025-04-12

### ChromaDB Local Storage

- https://g.co/gemini/share/e7c4d92255df

```
**Where are the files stored?**

Within the `persist_directory` you specify, ChromaDB will create a structure containing:

* A `chroma.sqlite3` file: This is the main SQLite database that stores the metadata about your collections, segments, and other system information.
* Subdirectories for each collection (named with UUIDs): These directories contain the actual vector data (often in binary files like `header.bin`, `link_lists.bin`, `data_level0.bin` for the HNSW index) and metadata related to the vectors in that collection.
```

## 2025-04-14

- https://www.perplexity.ai/search/what-is-hnsw-index-bBIG04AqTY2ESCCy6HzYyw#0
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
What is HNSW index?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
The Hierarchical Navigable Small World (HNSW) index is a sophisticated data structure designed for efficient **Approximate Nearest Neighbor (ANN)** searches in high-dimensional vector spaces. It is widely used in vector databases and applications like recommendation systems, image retrieval, and generative AI.

### **Key Features of HNSW**
1. **Multi-layered Graph Structure**:
   - HNSW organizes data into a graph with multiple layers, where higher layers contain fewer nodes and sparser connections. This hierarchy enables fast traversal and efficient narrowing down of search areas.
   - The search begins at the top layer for global traversal and progresses to lower layers for local refinement, mimicking a "zoom out, then zoom in" approach[1][2].

2. **Probabilistic Construction**:
   - When inserting vectors, they are added to the bottom layer and probabilistically assigned to higher layers with decreasing likelihood. This creates long-range connections in upper layers and dense connectivity in lower layers[1][4].

3. **Search Efficiency**:
   - HNSW achieves logarithmic time complexity $$O(\log n)$$ for searches by reducing the number of distance computations compared to brute-force methods. It balances speed and accuracy using tunable parameters like `m` (maximum connections per node) and `efSearch` (search depth)[1][3].

4. **Scalability**:
   - The index is highly scalable, making it suitable for large datasets. However, it requires significant memory resources, as the size of the index grows with the number of vectors and connections[2][5].

5. **Trade-offs**:
   - HNSW is an approximate method, meaning it sacrifices exactness for speed.
   - Building the index can be computationally expensive, especially for large datasets, requiring substantial RAM and CPU usage[4].

### **Applications**
- **Vector Search**: HNSW is commonly used in vector databases (e.g., FAISS, Milvus) to retrieve semantically similar embeddings efficiently.
- **Generative AI**: It supports fast similarity searches for text or image embeddings in applications like recommendation systems or LLM-based tools[3][5].
- **Postgres Integration**: Extensions like pgvector enable HNSW indexing directly within relational databases for optimized ANN queries[3][4].

Overall, HNSW's combination of speed, scalability, and tunability makes it a popular choice for high-dimensional vector search tasks where exact methods are impractical.

Citations:
[1] https://zilliz.com/ai-faq/what-is-a-hierarchical-navigable-small-world-hnsw-graph-index-and-how-does-it-organize-vectors-to-enable-efficient-approximate-nearest-neighbor-search
[2] https://weaviate.io/developers/academy/py/vector_index/hnsw
[3] https://neon.tech/blog/understanding-vector-search-and-hnsw-index-with-pgvector
[4] https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector
[5] https://www.educative.io/courses/vector-database/hnsw-indexing-in-vector-databases-for-performance-optimization
[6] https://towardsdatascience.com/not-all-hnsw-indices-are-made-equaly-6bc0d7efd8c7/
[7] https://www.pinecone.io/learn/series/faiss/hnsw/
[8] https://docs.vespa.ai/en/approximate-nn-hnsw.html

---
Answer from Perplexity: pplx.ai/share
</td></tr></table>

- https://g.co/gemini/share/54529c88d0d0
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
What is HNSW index?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

The Hierarchical Navigable Small World (HNSW) index is a graph-based algorithm that excels at performing approximate nearest neighbor (ANN) searches, particularly in high-dimensional vector spaces. Think of it as creating a smart map for your data points, allowing for quick and efficient searches for similar items.

Here's a breakdown of the key ideas behind HNSW:

**1. Navigable Small World (NSW) Graphs:**

* At its core, HNSW builds upon the concept of Navigable Small World (NSW) graphs. Imagine each data point as a node in a network. NSW graphs connect these nodes based on their proximity (similarity), with closer points having more connections.
* A crucial property of NSW graphs is the "small world" phenomenon – most nodes can be reached from any other node in a small number of steps. This is achieved by having both short-range connections (to very similar items) and a few longer-range connections (to less similar but potentially important "bridge" nodes).
* During a search, the algorithm starts at a random entry point and greedily navigates the graph by always moving to the neighbor closest to the query point. The mix of short and long links allows for efficient traversal to the general vicinity of the target.

**2. Hierarchy:**

* HNSW enhances the NSW concept by introducing a hierarchical structure, similar to a multi-layered skip list. It creates multiple layers of these NSW graphs.
* The top layers are sparser, containing fewer nodes and longer links, designed for quick, coarse-grained exploration of the data. These layers help to rapidly narrow down the search to a relevant area.
* As you move down the layers, the graphs become denser, with more nodes and shorter links, allowing for fine-grained searching and more accurate identification of the nearest neighbors.
* The search process starts at the top layer and navigates down to progressively lower layers, refining the search at each step. This hierarchical approach significantly speeds up the search compared to a single-layer NSW graph.

**In essence, HNSW combines the "small world" property for efficient navigation with a hierarchical structure for progressively finer searches.**

**Key Properties and Benefits:**

* **High Search Accuracy and Recall:** HNSW achieves a good balance between speed and accuracy in finding nearest neighbors.
* **Low Latency:** The hierarchical structure enables fast query times, crucial for real-time applications.
* **Scalability:** HNSW performs well even with large, high-dimensional datasets.
* **Dynamic Data Handling:** It can efficiently handle insertions and deletions of data points without requiring a complete rebuild of the index (unlike some other indexing methods).
* **Tunable Performance:** Parameters like the number of connections per node and the search list size can be adjusted to trade off between search speed, accuracy, and memory usage.

**Applications:**

HNSW indexes are widely used in various applications that rely on efficient similarity search, including:

* **Vector Databases:** As a primary indexing method for fast retrieval of similar vector embeddings.
* **Recommendation Systems:** Finding similar users or items based on their vector representations.
* **Image and Video Retrieval:** Searching for visually similar content.
* **Natural Language Processing (NLP):** Semantic search, finding documents or text snippets with similar meanings.
* **Anomaly Detection:** Identifying unusual data points that are far from their nearest neighbors.
* **Multi-modal Data Retrieval:** Searching across different data types (text, images, audio) based on their embeddings.

In short, the HNSW index is a powerful and versatile tool for efficiently finding similar data points in large, complex datasets, making it a cornerstone of many modern AI applications.
</td></tr></table>