# chromadb

- PyPI
  - https://pypi.org/project/chromadb/
- Git Repo:
  - https://github.com/chroma-core/chroma
- Website:
  - https://www.trychroma.com/

> the AI-native open-source embedding database

## 2024-10-08

- Learned from https://github.com/gabrielchua/RAGxplorer/blob/main/ragxplorer/rag.py
- [[ 向量資料庫 ] 一個好用的開源 Embedding 應用資料庫— ChromaDB](https://medium.com/@simon3458/chromadb-introduction-27ed114d8d1d)

## 2025-04-12

- 緣起：最近在測試一些 GenAI Use Case，常撞到 context window size 的限制。所以想試試看 RAG 的作法能否舒緩 context window size 的壓力。想起先前的一些研究，常見的 vector database 包括 pinecone, chromadb, faiss, pgVector 等。有鑑於 chromadb 算是比較輕量級，合適在本地端直接運行在記憶體或存成檔案的一種實作，就挑這個來當作第一個 vector database 實作的對象。

### ChromaDB 與 ClickHouse 的黑歷史

- https://g.co/gemini/share/bc8686250b5a
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there relationship between chromadb and clickhouse?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
There's an interesting history between ChromaDB and ClickHouse.

**Historically, ChromaDB used ClickHouse as an optional document store, especially for client/server deployments.** If ClickHouse wasn't used, ChromaDB would store data in an <mark>in-process DuckDB database</mark>.

However, **ChromaDB has evolved.** As of <mark>version 0.4.0, it **no longer relies on ClickHouse or DuckDB as system dependencies.**</mark> It now uses <mark>SQLite</mark> for document storage in both local and client/server setups. This change aimed to simplify installation and running ChromaDB.

Despite this shift, the connection isn't entirely severed:

* **ClickHouse has integrated vector search capabilities as an add-on.** This means ClickHouse itself can perform vector similarity searches, which is the core functionality of ChromaDB.
* There might still be users who deployed earlier versions of ChromaDB with ClickHouse and continue to use them.
* Tools might exist that facilitate data transfer or interaction between the two systems, though they aren't core to either project. For example, there's a record of "ClickPy" providing download analytics for ChromaDB within the ClickHouse ecosystem.

**In essence, while ChromaDB initially had a dependency option for ClickHouse, it has since moved towards a more self-contained architecture. However, both are capable of handling vector data in different ways.** ChromaDB is built specifically as a vector database, while ClickHouse is a more general-purpose columnar database with added vector search functionality.
</td></tr></table>

### ChromeDB 與其他向量資料庫的比較表

- https://g.co/gemini/share/206632776e8d

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Could you create a comparison table of Faiss, ChromaDB, LanceDB, Pinecone, Milvus and Qdrant using markdown syntax?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Alright, let's get this updated comparison table whipped up for you, keeping in mind the current date and location (though those don't directly impact the technical features!).

| Feature             | Faiss                                      | ChromaDB                                 | LanceDB                                    | Pinecone                                    | Milvus                                      | Qdrant                                       |
|----------------------|--------------------------------------------|------------------------------------------|------------------------------------------|---------------------------------------------|---------------------------------------------|----------------------------------------------|
| **Primary Focus** | Efficient similarity search library        | Developer-friendly embedding database      | Persistent vector database for ML workloads | Managed vector database service             | Open-source vector database, scalable       | Open-source vector database, developer experience |
| **Deployment** | Library (Python, C++)                        | Local (in-memory, persistent SQLite), Client/Server (SQLite) | Local (file-based), Cloud (in progress) | Cloud-hosted (fully managed)              | Self-hosted (Docker, Kubernetes), Cloud offerings | Self-hosted (Docker, Kubernetes), Cloud offerings |
| **Scalability** | Scales with available RAM and CPU/GPU, can handle large datasets | Limited by local resources in default setup, client/server offers better scalability | Designed for efficient out-of-core processing | Highly scalable (horizontal scaling managed by Pinecone) | Highly scalable (distributed architecture)   | Highly scalable (horizontal scaling)         |
| **Ease of Use** | Relatively straightforward for core functionality, more involved for advanced features | Very easy to get started, Python-centric API | Easy to use Python and Javascript APIs     | Relatively easy to use, REST and Python API | More complex setup and management           | Relatively easy to use, Python, Go, Rust, Java clients |
| **Data Storage** | In-memory primarily, can save/load indices to disk | In-memory (default), Persistent (SQLite)   | Persistent (Lance columnar format)        | Cloud storage managed by Pinecone           | Various backends supported (e.g., RocksDB, S3) | In-memory with persistence options           |
| **Vector Search** | Primarily Approximate Nearest Neighbors (ANN) | Exact and Approximate Nearest Neighbors (ANN) | Approximate Nearest Neighbors (ANN) with filtering | Approximate Nearest Neighbors (ANN)         | Exact and Approximate Nearest Neighbors (ANN) | Exact and Approximate Nearest Neighbors (ANN) |
| **Filtering** | Basic filtering capabilities after search     | Rich filtering capabilities based on metadata | Rich filtering based on vector and metadata | Filtering based on metadata                | Rich filtering capabilities based on attributes | Rich filtering capabilities based on payload |
| **Metadata Handling**| Limited direct metadata management         | First-class support for metadata          | Integrated metadata handling within the columnar format | Supports metadata associated with vectors    | Supports attributes associated with vectors | First-class support for payload (arbitrary JSON) |
| **Ecosystem & Integrations** | Widely used in the research community      | Growing Python ecosystem, Langchain integration | Growing Python and Javascript ecosystem, integrates with data processing tools | Strong ecosystem, integrations with various MLOps tools | Wide range of integrations, active open-source community | Growing ecosystem, Langchain, LlamaIndex integrations |
| **Cost** | Open-source (free)                           | Open-source (free for local use), costs for client/server deployments | Open-source (free for local use), potential costs for future cloud offerings | Usage-based pricing for managed service   | Open-source (free to self-host), costs for cloud offerings | Open-source (free to self-host), costs for cloud offerings |
| **Real-time Updates**| Requires rebuilding the index for updates    | Supports adding, updating, and deleting vectors and metadata | Supports adding and deleting records       | Supports real-time upserts and deletes      | Supports real-time data insertion and updates | Supports real-time upserts and deletes      |
| **Key Advantage** | High performance for similarity search, especially with large datasets | Developer-friendly, easy to integrate into Python workflows | Efficient storage and querying for ML data, strong data versioning potential | Fully managed service, handles scaling automatically | Highly scalable and flexible, supports hybrid architectures | Focus on developer experience, strong filtering and payload capabilities |

**In a nutshell:**

* **Faiss:** Think of it as a powerful engine under the hood for similarity search. It's a library you build upon.
* **ChromaDB:** Great for getting started quickly in Python, especially for LLM applications, with both in-memory and persistent options.
* **LanceDB:** Positions itself as a database optimized for ML data, offering efficient storage and querying with a focus on persistent data.
* **Pinecone:** The go-to if you want a fully managed, scalable vector database without worrying about infrastructure.
* **Milvus:** Offers high scalability and flexibility as an open-source vector database, suitable for complex deployments.
* **Qdrant:** Balances ease of use and scalability with excellent filtering and the ability to store arbitrary JSON payloads alongside your vectors.

Choosing the best one depends heavily on your project's specific requirements, scale, deployment needs, and your team's expertise.
</td></tr></table>

### ChromaDB 與 LlamaIndex 的整合範例

- https://g.co/gemini/share/c5b5a67f4b2f

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Are there integration between llama-index and ChromaDB?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there is a strong and direct integration between LlamaIndex and ChromaDB.

LlamaIndex is a framework for building applications powered by large language models (LLMs). It helps you ingest, structure, and access your private or domain-specific data. Vector databases play a crucial role in this process by providing efficient storage and retrieval of vector embeddings, which are numerical representations of your data's meaning.

**ChromaDB is explicitly supported as a vector store within LlamaIndex.** This means you can seamlessly use ChromaDB to store and query the embeddings generated by LlamaIndex.

Here's how the integration works:

* **Storing Embeddings:** When you use LlamaIndex to process your documents, it can generate embeddings for the text chunks. You can configure LlamaIndex to use ChromaDB as the `vector_store` in your `StorageContext`. LlamaIndex will then automatically store these embeddings, along with the corresponding text and metadata, in a ChromaDB collection.
* **Querying:** When you query your LlamaIndex index, the query is also converted into an embedding. LlamaIndex then uses the ChromaDB vector store to perform a similarity search, finding the most relevant embeddings (and thus the original text chunks) to your query.
* **Abstraction:** LlamaIndex provides an abstraction layer over ChromaDB, making it easy to interact with ChromaDB without needing to write raw ChromaDB client code. You interact with LlamaIndex's indexing and querying interfaces, and it handles the underlying communication with ChromaDB.

**Key aspects of the integration:**

* **`ChromaVectorStore`:** LlamaIndex provides a `ChromaVectorStore` class within its `vector_stores` module. This class acts as the connector between LlamaIndex and ChromaDB. You initialize it with a ChromaDB collection object.
* **`StorageContext`:** You use LlamaIndex's `StorageContext` to specify how your data is stored. When using ChromaDB, you'll instantiate a `ChromaVectorStore` and pass it to the `StorageContext`.
* **`VectorStoreIndex`:** This is a primary LlamaIndex class for building vector-based indexes. You can create a `VectorStoreIndex` directly from documents, and by providing a `StorageContext` configured with `ChromaVectorStore`, the index will be stored in ChromaDB. You can also load an existing index from ChromaDB using `VectorStoreIndex.from_vector_store()`.
* **Metadata Filtering:** Both LlamaIndex and ChromaDB support metadata. When storing data, LlamaIndex can store metadata in ChromaDB, and during querying, you can use metadata filters within LlamaIndex queries to narrow down your search within ChromaDB.
* **Different ChromaDB Modes:** LlamaIndex supports various ChromaDB deployment modes, including in-memory, persistent local storage, and connecting to a remote ChromaDB server.

**In short, ChromaDB is a first-class citizen in the LlamaIndex ecosystem, offering a robust and easy-to-use vector storage solution for your LLM-powered applications.** The integration simplifies the process of building retrieval-augmented generation (RAG) pipelines and other applications that rely on semantic search over your data.
</td></tr></table>

- https://g.co/gemini/share/5708e3d5ae8e

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step example in Python, to create a git repository RAG using LlamaIndex, ChromaDB and LangChain?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Alright, let's craft a step-by-step Python example to build a Git repository RAG (Retrieval-Augmented Generation) application using LlamaIndex, ChromaDB, and LangChain. This will guide you through the process of cloning a Git repository, indexing its content using LlamaIndex and ChromaDB, and then querying it using LangChain for the language model.

**Prerequisites:**

* **Python 3.8+**
* **Git installed**
* **Install the necessary libraries:**

    ```bash
    pip install llama-index chromadb langchain sentence-transformers
    ```

**Step 1: Import Necessary Libraries**

```python
import os
import shutil
from pathlib import Path

from git import Repo
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.embeddings import HuggingFaceEmbedding
from langchain_openai import ChatOpenAI  # Or any other LangChain LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
```

**Step 2: Define Repository Details and Paths**

```python
repo_url = "https://github.com/hwchase17/langchain"  # Example LangChain repository
repo_name = "langchain_repo"
repo_path = Path("./" + repo_name)
documents_path = Path("./" + repo_name)  # LlamaIndex will read files from here
persist_dir = Path("./chroma_db")
```

**Step 3: Clone the Git Repository**

```python
if repo_path.exists():
    shutil.rmtree(repo_path)  # Remove if it exists to ensure a fresh clone

print(f"Cloning repository from {repo_url} to {repo_path}...")
Repo.clone_from(repo_url, repo_path)
print("Repository cloned successfully.")
```

**Step 4: Load Documents from the Repository using LlamaIndex**

LlamaIndex's `SimpleDirectoryReader` can recursively read files from a directory.

```python
print(f"Loading documents from {documents_path}...")
reader = SimpleDirectoryReader(input_dir=documents_path, recursive=True, file_extractor={
    ".md": "markdown",
    ".py": "python",
    ".txt": "text",
    # Add other relevant file extensions and their parsers if needed
})
documents = reader.load_data()
print(f"Loaded {len(documents)} documents.")
```

**Step 5: Initialize ChromaDB and LlamaIndex Embedding Model**

We'll use `HuggingFaceEmbedding` for generating embeddings. You can choose other embedding models as well.

```python
# Initialize ChromaDB in a persistent directory
chroma_client = chromadb.PersistentClient(path=str(persist_dir))
chroma_collection = chroma_client.get_or_create_collection(name="langchain_docs")

# Initialize LlamaIndex's ChromaVectorStore
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Initialize the embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2")

# Configure LlamaIndex's StorageContext
storage_context = StorageContext.from_defaults(vector_store=vector_store, embed_model=embed_model)
```

**Step 6: Create the Vector Store Index using LlamaIndex**

This step processes the loaded documents, generates embeddings, and stores them in ChromaDB via the `vector_store`.

```python
print("Creating LlamaIndex Vector Store Index...")
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)
print("Vector Store Index created and persisted to ChromaDB.")
```

**Step 7: Set up LangChain LLM and Prompt**

Here, we'll initialize a LangChain LLM (replace with your preferred model and API key if needed) and define a prompt for querying.

```python
# Initialize LangChain LLM (replace with your actual API key or model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)  # Requires OpenAI API key

# Define a prompt for querying the Git repository content
prompt_template = """You are a helpful assistant that answers questions about the content of a Git repository.
Use the following context to answer the user's question.
If you don't know the answer, just say "I don't know".
Context: {context}
Question: {question}
Answer:"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)
```

**Step 8: Create a Query Function**

This function takes a query, retrieves relevant documents from ChromaDB using LlamaIndex, and then uses LangChain to generate an answer based on the retrieved context.

```python
def query_git_repo(query):
    # Perform similarity search using LlamaIndex's VectorStoreIndex
    retriever = index.as_retriever()
    nodes = retriever.retrieve(query)
    context_text = "\n\n".join([node.get_content() for node in nodes])

    # Use LangChain to generate the answer
    response = llm_chain.run(context=context_text, question=query)
    return response
```

**Step 9: Example Query**

Now you can ask questions about the LangChain repository.

```python
query = "What are the main features of LangChain?"
answer = query_git_repo(query)
print(f"\nQuestion: {query}")
print(f"Answer: {answer}")

query = "How can I contribute to LangChain?"
answer = query_git_repo(query)
print(f"\nQuestion: {query}")
print(f"Answer: {answer}")
```

**Step 10: Clean Up (Optional)**

You can remove the cloned repository and ChromaDB directory if you want to start fresh next time.

```python
# if repo_path.exists():
#     shutil.rmtree(repo_path)
# if persist_dir.exists():
#     shutil.rmtree(persist_dir)
```

**Complete Code:**

```python
import os
import shutil
from pathlib import Path

from git import Repo
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.embeddings import HuggingFaceEmbedding
from langchain_openai import ChatOpenAI  # Or any other LangChain LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import chromadb

# Define repository details and paths
repo_url = "https://github.com/hwchase17/langchain"  # Example LangChain repository
repo_name = "langchain_repo"
repo_path = Path("./" + repo_name)
documents_path = Path("./" + repo_name)  # LlamaIndex will read files from here
persist_dir = Path("./chroma_db")

# Clone the Git Repository
if repo_path.exists():
    shutil.rmtree(repo_path)  # Remove if it exists to ensure a fresh clone

print(f"Cloning repository from {repo_url} to {repo_path}...")
Repo.clone_from(repo_url, repo_path)
print("Repository cloned successfully.")

# Load Documents from the Repository using LlamaIndex
print(f"Loading documents from {documents_path}...")
reader = SimpleDirectoryReader(input_dir=documents_path, recursive=True, file_extractor={
    ".md": "markdown",
    ".py": "python",
    ".txt": "text",
    # Add other relevant file extensions and their parsers if needed
})
documents = reader.load_data()
print(f"Loaded {len(documents)} documents.")

# Initialize ChromaDB and LlamaIndex Embedding Model
# Initialize ChromaDB in a persistent directory
chroma_client = chromadb.PersistentClient(path=str(persist_dir))
chroma_collection = chroma_client.get_or_create_collection(name="langchain_docs")

# Initialize LlamaIndex's ChromaVectorStore
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Initialize the embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2")

# Configure LlamaIndex's StorageContext
storage_context = StorageContext.from_defaults(vector_store=vector_store, embed_model=embed_model)

# Create the Vector Store Index using LlamaIndex
print("Creating LlamaIndex Vector Store Index...")
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)
print("Vector Store Index created and persisted to ChromaDB.")

# Set up LangChain LLM and Prompt
# Initialize LangChain LLM (replace with your actual API key or model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)  # Requires OpenAI API key

# Define a prompt for querying the Git repository content
prompt_template = """You are a helpful assistant that answers questions about the content of a Git repository.
Use the following context to answer the user's question.
If you don't know the answer, just say "I don't know".
Context: {context}
Question: {question}
Answer:"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Create a Query Function
def query_git_repo(query):
    # Perform similarity search using LlamaIndex's VectorStoreIndex
    retriever = index.as_retriever()
    nodes = retriever.retrieve(query)
    context_text = "\n\n".join([node.get_content() for node in nodes])

    # Use LangChain to generate the answer
    response = llm_chain.run(context=context_text, question=query)
    return response

# Example Query
query = "What are the main features of LangChain?"
answer = query_git_repo(query)
print(f"\nQuestion: {query}")
print(f"Answer: {answer}")

query = "How can I contribute to LangChain?"
answer = query_git_repo(query)
print(f"\nQuestion: {query}")
print(f"Answer: {answer}")

# Clean Up (Optional)
# if repo_path.exists():
#     shutil.rmtree(repo_path)
# if persist_dir.exists():
#     shutil.rmtree(persist_dir)
```

**Explanation:**

1.  **Import Libraries:** Imports the necessary modules from `git`, `llama_index`, `chromadb`, and `langchain`.
2.  **Define Paths:** Sets up variables for the repository URL, local path, and the ChromaDB persistence directory.
3.  **Clone Repository:** Uses the `git` library to clone the specified Git repository to your local machine.
4.  **Load Documents:** Employs LlamaIndex's `SimpleDirectoryReader` to recursively load all files (with specified extensions) from the cloned repository directory into LlamaIndex `Document` objects.
5.  **Initialize ChromaDB and Embeddings:**
    * Initializes a ChromaDB client, creating or getting a collection to store the embeddings.
    * Creates a `ChromaVectorStore` object, connecting LlamaIndex to the ChromaDB collection.
    * Initializes a `HuggingFaceEmbedding` model to generate embeddings for the text content.
    * Sets up a `StorageContext` in LlamaIndex, linking the `vector_store` and the `embed_model`.
6.  **Create Vector Store Index:** Uses `VectorStoreIndex.from_documents` to process the loaded documents, generate embeddings using the specified `embed_model`, and store them in ChromaDB via the configured `storage_context`. The index is persisted to the `persist_dir`.
7.  **Set up LangChain LLM and Prompt:**
    * Initializes a LangChain LLM (in this case, `ChatOpenAI`). **Remember to replace this with your desired LLM and provide any necessary API keys.**
    * Defines a prompt template that instructs the LLM to answer questions based on the provided context.
    * Creates an `LLMChain` to link the prompt and the LLM.
8.  **Query Function:**
    * Takes a `query` as input.
    * Uses the LlamaIndex `index` (which is backed by ChromaDB) to perform a similarity search (`index.as_retriever().retrieve(query)`), retrieving the most relevant `Node` objects (containing text and metadata).
    * Extracts the text content from the retrieved nodes to form the `context`.
    * Passes the `context` and the original `query` to the LangChain `llm_chain` to generate an `answer`.
    * Returns the generated `answer`.
9.  **Example Query:** Demonstrates how to use the `query_git_repo` function with example questions.
10. **Clean Up (Optional):** Includes commented-out code to remove the cloned repository and ChromaDB directory if needed.

**To Run This Code:**

1.  Make sure you have all the prerequisites installed.
2.  Save the code as a Python file (e.g., `git_rag.py`).
3.  **If you are using `ChatOpenAI` (or any other LangChain LLM that requires an API key), ensure you have set up your API key as an environment variable (e.g., `OPENAI_API_KEY="your_key_here"`).**
4.  Run the script from your terminal: `python git_rag.py`

This will clone the LangChain repository, index its content in ChromaDB, and then answer the example questions based on the retrieved information. You can adapt the `repo_url`, file extensions, embedding model, and LLM according to your specific needs.
</td></tr></table>

### ChromaDB Local Storage

- https://g.co/gemini/share/e7c4d92255df

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Does chromadb store as local file?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, ChromaDB can store its data as local files. It offers a **PersistentClient** that allows you to specify a directory on your local machine where the database will be saved.

Here's how it works:

* **PersistentClient:** When you initialize ChromaDB with the `PersistentClient` and provide a `path` to a directory, ChromaDB will store its database files in that location.
* **Automatic Persistence:** Data is automatically persisted to this directory as you add collections and embeddings.
* **Loading on Startup:** When you re-initialize the `PersistentClient` with the same path, ChromaDB will automatically load the existing database from those files.

**Example:**

```python
import chromadb

# Initialize ChromaDB to store data in the './chroma_db' directory
client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = client.get_or_create_collection("my_documents")

# Add data to the collection
collection.add(
    documents=["This is document 1", "This is document 2"],
    ids=["doc1", "doc2"]
)

# When you close your script and run it again:
client_reloaded = chromadb.PersistentClient(path="./chroma_db")
collection_reloaded = client_reloaded.get_collection("my_documents")
print(f"Number of documents in reloaded collection: {collection_reloaded.count()}")
```

In the example above, the data added to `my_documents` collection will be saved in the `./chroma_db` directory and will be loaded automatically when you re-run the script and connect to the same path.

**Where are the files stored?**

Within the `persist_directory` you specify, ChromaDB will create a structure containing:

* A `chroma.sqlite3` file: This is the main SQLite database that stores the metadata about your collections, segments, and other system information.
* Subdirectories for each collection (named with UUIDs): These directories contain the actual vector data (often in binary files like `header.bin`, `link_lists.bin`, `data_level0.bin` for the HNSW index) and metadata related to the vectors in that collection.

So, to answer your question directly: **Yes, when configured with the `PersistentClient`, ChromaDB stores its data as local files within the directory you specify.** This makes it easy to have a local, persistent vector database for your applications.
</td></tr></table>

## 2025-04-15

- https://docs.trychroma.com/docs/overview/getting-started

### Get Started

- Install 安裝
```bash
jazzw@JazzBook:~/git/snippet/py/chromadb$ pip install chromadb
... skip ...
Building wheels for collected packages: chroma-hnswlib
  Building wheel for chroma-hnswlib (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for chroma-hnswlib (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [5 lines of output]
      running bdist_wheel
      running build
      running build_ext
      building 'hnswlib' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for chroma-hnswlib
Failed to build chroma-hnswlib
ERROR: Failed to build installable wheels for some pyproject.toml based projects (chroma-hnswlib)
```
- 看起來 Windows 環境需要安裝 Visual C++
- 改用 WSL 試試看
```bash
jazzw@JazzBook:~/git/snippet/py/chromadb$ wsl
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 5.15.167.4-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Apr 15 22:19:43 CST 2025

  System load:  0.24                Processes:             54
  Usage of /:   0.3% of 1006.85GB   Users logged in:       0
  Memory usage: 3%                  IPv4 address for eth0: 172.29.78.252
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

This message is shown once a day. To disable it please create the
/home/jazz/.hushlogin file.
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ cd
jazz@JazzBook:~$ pip3 install chromadb
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```
- WSL 有點囉唆，我還是直接在 Github Codespace 的容器裡測試好了。
```bash
jazzw@JazzBook:~$ blank ssh
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1021-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Tue Apr 15 06:49:17 2025 from ::1
@jazzwang ➜ /workspaces/codespaces-blank (main) $ pip install chromadb
@jazzwang ➜ /workspaces/codespaces-blank (main) $
```
- 跑個範例程式：
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ vi chromadb-lab1.py
```
```python
import chromadb
chroma_client = chromadb.Client()

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about florida"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ python3 chromadb-lab1.py
Traceback (most recent call last):
  File "/workspaces/codespaces-blank/chromadb-lab1.py", line 1, in <module>
    import chromadb
  File "/home/codespace/.python/current/lib/python3.12/site-packages/chromadb/__init__.py", line 94, in <module>
    raise RuntimeError(
RuntimeError: Your system has an unsupported version of sqlite3. Chroma                     requires sqlite3 >= 3.35.0.
Please visit                     https://docs.trychroma.com/troubleshooting#sqlite to learn how                     to upgrade
```
- 根據文件，Linux 環境要裝 `pysqlite3-binary`，而 Windows 環境更麻煩要額外裝 SQLite 的 DLL
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ pip install pysqlite3-binary
Collecting pysqlite3-binary
  Downloading pysqlite3_binary-0.5.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (766 bytes)
Downloading pysqlite3_binary-0.5.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 49.5 MB/s eta 0:00:00
Installing collected packages: pysqlite3-binary
Successfully installed pysqlite3-binary-0.5.4
```
- 測試還是不行。發現 Codespace 裡面還有 condas 環境。乾脆弄一個 `venv` 隔離一下好了。
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ python3 -m venv venv
@jazzwang ➜ /workspaces/codespaces-blank (main) $ source venv/bin/activate
(venv) @jazzwang ➜ /workspaces/codespaces-blank (main) $ pip install chromadb
```
- 所以講的是 SQLite 版本太舊
```bash
(venv) @jazzwang ➜ /workspaces/codespaces-blank (main) $ dpkg -l sqlite3
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version           Architecture Description
+++-==============-=================-============-===================================
ii  sqlite3        3.31.1-4ubuntu0.6 amd64        Command line interface for SQLite 3
```
## 2025-04-16

- 換一台 Github Codespace 一樣的版本。
```bash
@jazzwang ➜ /workspaces/snippet (master) $ dpkg -l sqlite3
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version           Architecture Description
+++-==============-=================-============-===================================
ii  sqlite3        3.31.1-4ubuntu0.6 amd64        Command line interface for SQLite 3
@jazzwang ➜ /workspaces/snippet (master) $ uname -a
Linux codespaces-dad4c5 6.8.0-1021-azure #25~22.04.1-Ubuntu SMP Thu Jan 16 21:37:09 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```
- 那就開一台新的 Debian docker instance 來跑吧！！
```bash
@jazzwang ➜ /workspaces/snippet/py/chromadb (master) $ docker run --name chromadb -it -v $(pwd):/data debian /bin/bash
root@0bebe826fa2e:/# cd data/
root@0bebe826fa2e:/data# apt-get update
root@0bebe826fa2e:/data# apt-get -y install python3-pip sqlite3
root@0bebe826fa2e:/data# pip3 install chromadb
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.11/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```
- 直接加 `--break-system-packages` 強迫安裝
```
root@0bebe826fa2e:/data# pip3 install chromadb --break-system-packages
```
- 試跑
```
root@0bebe826fa2e:/data# python3 chromadb-lab1.py
/root/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx.tar.gz: 100%|███████████████████████████████████████████████████| 79.3M/79.3M [00:18<00:00, 4.41MiB/s]
{'ids': [['id2', 'id1']], 'embeddings': None, 'documents': [['This is a document about oranges', 'This is a document about pineapple']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[None, None]], 'distances': [[1.1462137699127197, 1.3015384674072266]]}
```
- 結論：在 Windows 上使用 WSL 應該也可以依法炮製。
- ( 2025-04-16 18:28:32 )
- 備註：在 Google Cloud Shell 測試，就沒有遇到特定的 blocker。

### ChromaDB Local Storage - Test Drive

- Install ChromaDB on Windows WSL (Ubuntu)
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet$ pip install chromadb --break-system-packages
```
- 執行上面 Gemini 的範例：
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet$ python3 chromadb-lab2.py
Number of documents in reloaded collection: 2
```
- 觀察產生的 local storage 結構：
```bash
$ tree chroma_db/
chroma_db/
├── chroma.sqlite3
└── f0911c04-b80c-4e21-9fdd-11b74123bc08
    ├── data_level0.bin
    ├── header.bin
    ├── length.bin
    └── link_lists.bin

2 directories, 5 files
```

### LlamaIndex and ChromaDB - Test Drive

- Install LlamaIndex, LangChain, Sentence Transformers, ChromaDB on Windows WSL (Ubuntu)
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet$ pip install llama-index chromadb langchain sentence-transformers GitPython --break-system-packages
```
- 設定 OPENAI_API_KEY 環境變數：
```bash
export OPENAI_API_KEY=sk-000000000000000000000000000 ## paid OpenAI
```
- 試著運行上面 Gemini 給的範例：
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ python3 chromadb-git-repo-analysis.py
Traceback (most recent call last):
  File "/mnt/c/Users/jazzw/git/snippet/py/chromadb/chromadb-git-repo-analysis.py", line 7, in <module>
    from llama_index.vector_stores import ChromaVectorStore
ModuleNotFoundError: No module named 'llama_index.vector_stores'
```

## 2025-04-17

- 參考：https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/
- 加裝 `llama-index-vector-stores-chroma`
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ pip install llama-index-vector-stores-chroma --break-system-packages
```
- 改掉出錯的第 7 行
```diff
- from llama_index.vector_stores import ChromaVectorStore
+ from llama_index.vector_stores.chroma import ChromaVectorStore
```
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ python3 chromadb-git-repo-analysis.py
Traceback (most recent call last):
  File "/mnt/c/Users/jazzw/git/snippet/py/chromadb/chromadb-git-repo-analysis.py", line 8, in <module>
    from llama_index.embeddings import HuggingFaceEmbedding
ImportError: cannot import name 'HuggingFaceEmbedding' from 'llama_index.embeddings' (unknown location)
```
- ( 2025-04-17 00:26:04 )
- 加裝 `llama-index-embeddings-huggingface`
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ pip install llama-index-embeddings-huggingface --break-system-packages
```
- 改掉出錯的第八行
```diff
- from llama_index.embeddings import HuggingFaceEmbedding
+ from llama_index.embeddings.huggingface import HuggingFaceEmbedding
```
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ python3 chromadb-git-repo-analysis.py
Traceback (most recent call last):
  File "/mnt/c/Users/jazzw/git/snippet/py/chromadb/chromadb-git-repo-analysis.py", line 9, in <module>
    from langchain_openai import ChatOpenAI  # Or any other LangChain LLM
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'langchain_openai
```

## 2025-04-18

- ( 2025-04-18 20:01:57 )
- 改掉出錯的第九行
```diff
- from langchain_openai import ChatOpenAI  # Or any other LangChain LLM
+ from langchain_openai import ChatOpenAI
```
```bash
jazz@JazzBook:/mnt/c/Users/jazzw/git/snippet/py/chromadb$ python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/hwchase17/langchain to langchain_repo...
```
- 看到跳出 WSL 遇到一些 IO 效能問題的警告。然後查了一下，雖然有產生 `langchain_repo` 的目錄，卻似乎一直都沒有抓到檔案。
- 改用 Google Cloud Shell 跑跑看。一來網路比較快，二來不用切到 WSL 這樣好幾層。

## 2025-04-19

- ( 2025-04-19 00:11:56 )
```bash
cloudshell:~$ pip install chromadb GitPython llama-index-vector-stores-chroma llama-index-embeddings-huggingface
```
- 結果：光裝套件就把 Cloud Shell 的硬碟吃光了 :( 有點扯
```
ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device
@cloudshell:~$ df -h .
Filesystem                         Size  Used Avail Use% Mounted on
/dev/disk/by-id/google-home-part1  4.8G  4.6G     0 100% /home
```

## 2025-04-20

- ( 2025-04-20 11:42:40 )
- 改用 Github Codespace + Debian Docker Image 測試
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ docker run -it --name chromadb --hostname chromadb -v $(pwd):/data debian /bin/bash
root@chromadb:/# cd /data
root@chromadb:/data# apt-get update; apt-get -y install python3-pip wget git
root@chromadb:/data# pip install chromadb GitPython llama-index-vector-stores-chroma llama-index-embeddings-huggingface langchain langchain-openai --break-system-packages
root@chromadb:/data# wget https://raw.githubusercontent.com/jazzwang/snippet/refs/heads/master/py/chromadb/chromadb-git-repo-analysis.py
root@chromadb:/data# python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/hwchase17/langchain to langchain_repo...
```
- 看到一些錯誤訊息，加上 langchain repo 其實蠻複雜的，改用一個簡單一點的 git repo 來做這個實驗。
```
root@chromadb:/data# python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/jazzwang/confluence-insight to git_repo...
Repository cloned successfully.
Loading documents from git_repo...
Failed to load file /data/git_repo/MEMO.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/README.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/gen-pageGraph.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageHistories.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageIds.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageLinks.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pages.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/profile-stats.py with error: 'str' object has no attribute 'load_data'. Skipping...
Loaded 7 documents.
modules.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 349/349 [00:00<00:00, 2.73MB/s]
config_sentence_transformers.json: 100%|████████████████████████████████████████████████████████████████████████████████████| 116/116 [00:00<00:00, 772kB/s]
README.md: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 10.4k/10.4k [00:00<00:00, 47.8MB/s]
sentence_bert_config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 53.0/53.0 [00:00<00:00, 449kB/s]
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 571/571 [00:00<00:00, 5.58MB/s]
Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
model.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 438M/438M [00:01<00:00, 314MB/s]
tokenizer_config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 363/363 [00:00<00:00, 1.84MB/s]
vocab.txt: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 1.80MB/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 3.58MB/s]
special_tokens_map.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 239/239 [00:00<00:00, 2.24MB/s]
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 190/190 [00:00<00:00, 2.11MB/s]
Traceback (most recent call last):
  File "/data/chromadb-git-repo-analysis.py", line 52, in <module>
    storage_context = StorageContext.from_defaults(vector_store=vector_store, embed_model=embed_model)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: StorageContext.from_defaults() got an unexpected keyword argument 'embed_model'
```
- 補安裝 `hf_xet`
```
root@chromadb:/data# pip install huggingface_hub[hf_xet] --break-system-packages
root@chromadb:/data# pip install hf_xet --break-system-packages
```
- 看起來要繼續解
```
root@chromadb:/data# python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/jazzwang/confluence-insight to git_repo...
Repository cloned successfully.
Loading documents from git_repo...
Failed to load file /data/git_repo/MEMO.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/README.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/gen-pageGraph.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageHistories.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageIds.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageLinks.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pages.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/profile-stats.py with error: 'str' object has no attribute 'load_data'. Skipping...
Loaded 7 documents.
Traceback (most recent call last):
  File "/data/chromadb-git-repo-analysis.py", line 52, in <module>
    storage_context = StorageContext.from_defaults(vector_store=vector_store, embed_model=embed_model)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: StorageContext.from_defaults() got an unexpected keyword argument 'embed_model'
```
- 參考：https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/
- 改掉第 52 行
```diff
- storage_context = StorageContext.from_defaults(vector_store=vector_store, embed_model=embed_model)
+ storage_context = StorageContext.from_defaults(vector_store=vector_store)
```
- 新的錯誤訊息是關於該用什麼 `embedding`
```
root@chromadb:/data# python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/jazzwang/confluence-insight to git_repo...
Repository cloned successfully.
Loading documents from git_repo...
Failed to load file /data/git_repo/MEMO.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/README.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/gen-pageGraph.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageHistories.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageIds.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageLinks.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pages.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/profile-stats.py with error: 'str' object has no attribute 'load_data'. Skipping...
Loaded 7 documents.
Creating LlamaIndex Vector Store Index...
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/dist-packages/llama_index/core/embeddings/utils.py", line 50, in resolve_embed_model
    from llama_index.embeddings.openai import (
ModuleNotFoundError: No module named 'llama_index.embeddings.openai'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/chromadb-git-repo-analysis.py", line 56, in <module>
    index = VectorStoreIndex.from_documents(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/dist-packages/llama_index/core/indices/base.py", line 119, in from_documents
    return cls(
           ^^^^
  File "/usr/local/lib/python3.11/dist-packages/llama_index/core/indices/vector_store/base.py", line 72, in __init__
    else Settings.embed_model
         ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/dist-packages/llama_index/core/settings.py", line 64, in embed_model
    self._embed_model = resolve_embed_model("default")
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/dist-packages/llama_index/core/embeddings/utils.py", line 61, in resolve_embed_model
    raise ImportError(
ImportError: `llama-index-embeddings-openai` package not found, please run `pip install llama-index-embeddings-openai`
```
- 補裝 `llama-index-embeddings-openai`
```bash
root@chromadb:/data# pip install llama-index-embeddings-openai --break-system-packages
```
```bash
root@chromadb:/data# export OPENAI_API_KEY=sk-0000000000000000000000000000000000000000
root@chromadb:/data# python3 chromadb-git-repo-analysis.py
Cloning repository from https://github.com/jazzwang/confluence-insight to git_repo...
Repository cloned successfully.
Loading documents from git_repo...
Failed to load file /data/git_repo/MEMO.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/README.md with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/gen-pageGraph.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageHistories.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageIds.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pageLinks.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/get-pages.py with error: 'str' object has no attribute 'load_data'. Skipping...
Failed to load file /data/git_repo/profile-stats.py with error: 'str' object has no attribute 'load_data'. Skipping...
Loaded 7 documents.
Creating LlamaIndex Vector Store Index...
Vector Store Index created and persisted to ChromaDB.
/data/chromadb-git-repo-analysis.py:74: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.
  llm_chain = LLMChain(prompt=prompt, llm=llm)
/data/chromadb-git-repo-analysis.py:84: LangChainDeprecationWarning: The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  response = llm_chain.run(context=context_text, question=query)

Question: What are the main features of this git repo?
Answer: I don't know.

Question: How can I contribute to this git repo?
Answer: To contribute to this Git repository, you can follow the guidelines outlined in the "Submission of Contributions" section of the Apache License Version 2.0. This section states that any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of the License, without any additional terms or conditions. Make sure to adhere to the requirements specified in the license, such as providing attribution notices and following the redistribution conditions.
```
- 初步看起來是正常可以跑了。算是一個整合了 ChromaDB, LlamaIndex, LangChain, OpenAI embedding/GPT-3.5-Turbo 的 RAG 應用。
- 想法：
  - 畢竟是 Gemini 生成的範例程式，所以語法上會有很多舊的語法。像第 74 行跟第 84 行。
```bash
/data/chromadb-git-repo-analysis.py:74: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.
  llm_chain = LLMChain(prompt=prompt, llm=llm)
/data/chromadb-git-repo-analysis.py:84: LangChainDeprecationWarning: The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  response = llm_chain.run(context=context_text, question=query)
```
  - 還有上面遇到的套件 import 語法錯誤，應該是因為 LangChain, LlamaIndex, ChromaDB 都一直在快速演化中，所以 Python package 的物件導向封裝方式也一定隨著時間不斷地修改。各大 LLM 模型目前雖然可以做到 Vibe Coding，透過持續迭代，與使用 TOOL 呼叫外部搜尋 API (或者支援 Grounding 的模型)，開發者的手動介入與修改還是不可或缺的。