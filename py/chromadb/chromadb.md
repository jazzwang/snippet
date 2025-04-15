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
Collecting chromadb
  Downloading chromadb-1.0.4-cp39-abi3-win_amd64.whl.metadata (7.0 kB)
Collecting build>=1.0.3 (from chromadb)
  Downloading build-1.2.2.post1-py3-none-any.whl.metadata (6.5 kB)
Collecting pydantic>=1.9 (from chromadb)
  Downloading pydantic-2.11.3-py3-none-any.whl.metadata (65 kB)
Collecting chroma-hnswlib==0.7.6 (from chromadb)
  Downloading chroma_hnswlib-0.7.6.tar.gz (32 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting fastapi==0.115.9 (from chromadb)
  Downloading fastapi-0.115.9-py3-none-any.whl.metadata (27 kB)
Collecting uvicorn>=0.18.3 (from uvicorn[standard]>=0.18.3->chromadb)
  Downloading uvicorn-0.34.1-py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: numpy>=1.22.5 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (2.2.4)
Collecting posthog>=2.4.0 (from chromadb)
  Downloading posthog-3.24.1-py2.py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: typing-extensions>=4.5.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (4.12.2)
Collecting onnxruntime>=1.14.1 (from chromadb)
  Downloading onnxruntime-1.21.0-cp312-cp312-win_amd64.whl.metadata (4.9 kB)
Collecting opentelemetry-api>=1.2.0 (from chromadb)
  Downloading opentelemetry_api-1.32.0-py3-none-any.whl.metadata (1.6 kB)
Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb)
  Downloading opentelemetry_exporter_otlp_proto_grpc-1.32.0-py3-none-any.whl.metadata (2.5 kB)
Collecting opentelemetry-instrumentation-fastapi>=0.41b0 (from chromadb)
  Downloading opentelemetry_instrumentation_fastapi-0.53b0-py3-none-any.whl.metadata (2.2 kB)
Collecting opentelemetry-sdk>=1.2.0 (from chromadb)
  Downloading opentelemetry_sdk-1.32.0-py3-none-any.whl.metadata (1.6 kB)
Collecting tokenizers>=0.13.2 (from chromadb)
  Downloading tokenizers-0.21.1-cp39-abi3-win_amd64.whl.metadata (6.9 kB)
Collecting pypika>=0.48.9 (from chromadb)
  Using cached pypika-0.48.9-py2.py3-none-any.whl
Collecting tqdm>=4.65.0 (from chromadb)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: overrides>=7.3.1 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (7.7.0)
Collecting importlib-resources (from chromadb)
  Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
Collecting grpcio>=1.58.0 (from chromadb)
  Downloading grpcio-1.71.0-cp312-cp312-win_amd64.whl.metadata (4.0 kB)
Collecting bcrypt>=4.0.1 (from chromadb)
  Downloading bcrypt-4.3.0-cp39-abi3-win_amd64.whl.metadata (10 kB)
Collecting typer>=0.9.0 (from chromadb)
  Downloading typer-0.15.2-py3-none-any.whl.metadata (15 kB)
Collecting kubernetes>=28.1.0 (from chromadb)
  Downloading kubernetes-32.0.1-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tenacity>=8.2.3 (from chromadb)
  Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Requirement already satisfied: pyyaml>=6.0.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (6.0.2)
Requirement already satisfied: mmh3>=4.0.1 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (5.1.0)
Collecting orjson>=3.9.12 (from chromadb)
  Downloading orjson-3.10.16-cp312-cp312-win_amd64.whl.metadata (42 kB)
Requirement already satisfied: httpx>=0.27.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (0.28.1)
Collecting rich>=10.11.0 (from chromadb)
  Downloading rich-14.0.0-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: jsonschema>=4.19.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from chromadb) (4.23.0)
Collecting starlette<0.46.0,>=0.40.0 (from fastapi==0.115.9->chromadb)
  Downloading starlette-0.45.3-py3-none-any.whl.metadata (6.3 kB)
Requirement already satisfied: packaging>=19.1 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from build>=1.0.3->chromadb) (24.2)
Collecting pyproject_hooks (from build>=1.0.3->chromadb)
  Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: colorama in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from build>=1.0.3->chromadb) (0.4.6)
Requirement already satisfied: anyio in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from httpx>=0.27.0->chromadb) (4.9.0)
Requirement already satisfied: certifi in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from httpx>=0.27.0->chromadb) (2025.1.31)
Requirement already satisfied: httpcore==1.* in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from httpx>=0.27.0->chromadb) (1.0.7)
Requirement already satisfied: idna in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from httpx>=0.27.0->chromadb) (3.10)
Requirement already satisfied: h11<0.15,>=0.13 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from httpcore==1.*->httpx>=0.27.0->chromadb) (0.14.0)
Requirement already satisfied: attrs>=22.2.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from jsonschema>=4.19.0->chromadb) (25.3.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from jsonschema>=4.19.0->chromadb) (2024.10.1)
Requirement already satisfied: referencing>=0.28.4 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from jsonschema>=4.19.0->chromadb) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from jsonschema>=4.19.0->chromadb) (0.24.0)
Requirement already satisfied: six>=1.9.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from kubernetes>=28.1.0->chromadb) (1.17.0)
Requirement already satisfied: python-dateutil>=2.5.3 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from kubernetes>=28.1.0->chromadb) (2.9.0.post0)
Collecting google-auth>=1.0.1 (from kubernetes>=28.1.0->chromadb)
  Downloading google_auth-2.39.0-py2.py3-none-any.whl.metadata (6.2 kB)
Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from kubernetes>=28.1.0->chromadb) (1.8.0)
Requirement already satisfied: requests in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from kubernetes>=28.1.0->chromadb) (2.32.3)
Collecting requests-oauthlib (from kubernetes>=28.1.0->chromadb)
  Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Collecting oauthlib>=3.2.2 (from kubernetes>=28.1.0->chromadb)
  Using cached oauthlib-3.2.2-py3-none-any.whl.metadata (7.5 kB)
Requirement already satisfied: urllib3>=1.24.2 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from kubernetes>=28.1.0->chromadb) (2.3.0)
Collecting durationpy>=0.7 (from kubernetes>=28.1.0->chromadb)
  Downloading durationpy-0.9-py3-none-any.whl.metadata (338 bytes)
Collecting coloredlogs (from onnxruntime>=1.14.1->chromadb)
  Using cached coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)
Collecting flatbuffers (from onnxruntime>=1.14.1->chromadb)
  Downloading flatbuffers-25.2.10-py2.py3-none-any.whl.metadata (875 bytes)
Collecting protobuf (from onnxruntime>=1.14.1->chromadb)
  Downloading protobuf-6.30.2-cp310-abi3-win_amd64.whl.metadata (593 bytes)
Collecting sympy (from onnxruntime>=1.14.1->chromadb)
  Downloading sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
Collecting deprecated>=1.2.6 (from opentelemetry-api>=1.2.0->chromadb)
  Downloading Deprecated-1.2.18-py2.py3-none-any.whl.metadata (5.7 kB)
Collecting importlib-metadata<8.7.0,>=6.0 (from opentelemetry-api>=1.2.0->chromadb)
  Downloading importlib_metadata-8.6.1-py3-none-any.whl.metadata (4.7 kB)
Collecting googleapis-common-protos~=1.52 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb)
  Downloading googleapis_common_protos-1.70.0-py3-none-any.whl.metadata (9.3 kB)
Collecting opentelemetry-exporter-otlp-proto-common==1.32.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb)
  Downloading opentelemetry_exporter_otlp_proto_common-1.32.0-py3-none-any.whl.metadata (1.9 kB)
Collecting opentelemetry-proto==1.32.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb)
  Downloading opentelemetry_proto-1.32.0-py3-none-any.whl.metadata (2.4 kB)
Collecting protobuf (from onnxruntime>=1.14.1->chromadb)
  Downloading protobuf-5.29.4-cp310-abi3-win_amd64.whl.metadata (592 bytes)
Collecting opentelemetry-instrumentation-asgi==0.53b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading opentelemetry_instrumentation_asgi-0.53b0-py3-none-any.whl.metadata (2.1 kB)
Collecting opentelemetry-instrumentation==0.53b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading opentelemetry_instrumentation-0.53b0-py3-none-any.whl.metadata (6.8 kB)
Collecting opentelemetry-semantic-conventions==0.53b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading opentelemetry_semantic_conventions-0.53b0-py3-none-any.whl.metadata (2.5 kB)
Collecting opentelemetry-util-http==0.53b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading opentelemetry_util_http-0.53b0-py3-none-any.whl.metadata (2.6 kB)
Collecting wrapt<2.0.0,>=1.0.0 (from opentelemetry-instrumentation==0.53b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading wrapt-1.17.2-cp312-cp312-win_amd64.whl.metadata (6.5 kB)
Collecting asgiref~=3.0 (from opentelemetry-instrumentation-asgi==0.53b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)
  Downloading asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting monotonic>=1.5 (from posthog>=2.4.0->chromadb)
  Using cached monotonic-1.6-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting backoff>=1.10.0 (from posthog>=2.4.0->chromadb)
  Using cached backoff-2.2.1-py3-none-any.whl.metadata (14 kB)
Collecting distro>=1.5.0 (from posthog>=2.4.0->chromadb)
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=1.9->chromadb)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.33.1 (from pydantic>=1.9->chromadb)
  Downloading pydantic_core-2.33.1-cp312-cp312-win_amd64.whl.metadata (6.9 kB)
Collecting typing-inspection>=0.4.0 (from pydantic>=1.9->chromadb)
  Downloading typing_inspection-0.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->chromadb)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from rich>=10.11.0->chromadb) (2.19.1)
Collecting huggingface-hub<1.0,>=0.16.4 (from tokenizers>=0.13.2->chromadb)
  Downloading huggingface_hub-0.30.2-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: click>=8.0.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from typer>=0.9.0->chromadb) (8.1.8)
Collecting shellingham>=1.3.0 (from typer>=0.9.0->chromadb)
  Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting httptools>=0.6.3 (from uvicorn[standard]>=0.18.3->chromadb)
  Downloading httptools-0.6.4-cp312-cp312-win_amd64.whl.metadata (3.7 kB)
Collecting python-dotenv>=0.13 (from uvicorn[standard]>=0.18.3->chromadb)
  Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)
Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.18.3->chromadb)
  Downloading watchfiles-1.0.5-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
Collecting websockets>=10.4 (from uvicorn[standard]>=0.18.3->chromadb)
  Downloading websockets-15.0.1-cp312-cp312-win_amd64.whl.metadata (7.0 kB)
Collecting cachetools<6.0,>=2.0.0 (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb)
  Downloading cachetools-5.5.2-py3-none-any.whl.metadata (5.4 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb)
  Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting rsa<5,>=3.1.4 (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb)
  Using cached rsa-4.9-py3-none-any.whl.metadata (4.2 kB)
Collecting filelock (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb)
  Downloading filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
Collecting fsspec>=2023.5.0 (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb)
  Downloading fsspec-2025.3.2-py3-none-any.whl.metadata (11 kB)
Collecting zipp>=3.20 (from importlib-metadata<8.7.0,>=6.0->opentelemetry-api>=1.2.0->chromadb)
  Downloading zipp-3.21.0-py3-none-any.whl.metadata (3.7 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from requests->kubernetes>=28.1.0->chromadb) (3.4.1)
Requirement already satisfied: sniffio>=1.1 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from anyio->httpx>=0.27.0->chromadb) (1.3.1)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>=1.14.1->chromadb)
  Using cached humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy->onnxruntime>=1.14.1->chromadb)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting pyreadline3 (from humanfriendly>=9.1->coloredlogs->onnxruntime>=1.14.1->chromadb)
  Downloading pyreadline3-3.5.4-py3-none-any.whl.metadata (4.7 kB)
Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb)
  Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
Downloading chromadb-1.0.4-cp39-abi3-win_amd64.whl (18.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 1.3 MB/s eta 0:00:00
Downloading fastapi-0.115.9-py3-none-any.whl (94 kB)
Downloading bcrypt-4.3.0-cp39-abi3-win_amd64.whl (152 kB)
Downloading build-1.2.2.post1-py3-none-any.whl (22 kB)
Downloading grpcio-1.71.0-cp312-cp312-win_amd64.whl (4.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 1.9 MB/s eta 0:00:00
Downloading kubernetes-32.0.1-py2.py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 1.8 MB/s eta 0:00:00
Downloading onnxruntime-1.21.0-cp312-cp312-win_amd64.whl (11.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.8/11.8 MB 2.0 MB/s eta 0:00:00
Downloading opentelemetry_api-1.32.0-py3-none-any.whl (65 kB)
Downloading opentelemetry_exporter_otlp_proto_grpc-1.32.0-py3-none-any.whl (18 kB)
Downloading opentelemetry_exporter_otlp_proto_common-1.32.0-py3-none-any.whl (18 kB)
Downloading opentelemetry_proto-1.32.0-py3-none-any.whl (55 kB)
Downloading opentelemetry_instrumentation_fastapi-0.53b0-py3-none-any.whl (12 kB)
Downloading opentelemetry_instrumentation-0.53b0-py3-none-any.whl (30 kB)
Downloading opentelemetry_instrumentation_asgi-0.53b0-py3-none-any.whl (16 kB)
Downloading opentelemetry_semantic_conventions-0.53b0-py3-none-any.whl (188 kB)
Downloading opentelemetry_util_http-0.53b0-py3-none-any.whl (7.3 kB)
Downloading opentelemetry_sdk-1.32.0-py3-none-any.whl (118 kB)
Downloading orjson-3.10.16-cp312-cp312-win_amd64.whl (133 kB)
Downloading posthog-3.24.1-py2.py3-none-any.whl (85 kB)
Downloading pydantic-2.11.3-py3-none-any.whl (443 kB)
Downloading pydantic_core-2.33.1-cp312-cp312-win_amd64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 1.9 MB/s eta 0:00:00
Downloading rich-14.0.0-py3-none-any.whl (243 kB)
Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
Downloading tokenizers-0.21.1-cp39-abi3-win_amd64.whl (2.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 1.9 MB/s eta 0:00:00
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Downloading typer-0.15.2-py3-none-any.whl (45 kB)
Downloading uvicorn-0.34.1-py3-none-any.whl (62 kB)
Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached backoff-2.2.1-py3-none-any.whl (15 kB)
Downloading Deprecated-1.2.18-py2.py3-none-any.whl (10.0 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Downloading durationpy-0.9-py3-none-any.whl (3.5 kB)
Downloading google_auth-2.39.0-py2.py3-none-any.whl (212 kB)
Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
Downloading httptools-0.6.4-cp312-cp312-win_amd64.whl (88 kB)
Downloading huggingface_hub-0.30.2-py3-none-any.whl (481 kB)
Downloading importlib_metadata-8.6.1-py3-none-any.whl (26 kB)
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached monotonic-1.6-py2.py3-none-any.whl (8.2 kB)
Using cached oauthlib-3.2.2-py3-none-any.whl (151 kB)
Downloading protobuf-5.29.4-cp310-abi3-win_amd64.whl (434 kB)
Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)
Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Downloading starlette-0.45.3-py3-none-any.whl (71 kB)
Downloading typing_inspection-0.4.0-py3-none-any.whl (14 kB)
Downloading watchfiles-1.0.5-cp312-cp312-win_amd64.whl (291 kB)
Downloading websockets-15.0.1-cp312-cp312-win_amd64.whl (176 kB)
Using cached coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Downloading flatbuffers-25.2.10-py2.py3-none-any.whl (30 kB)
Downloading pyproject_hooks-1.2.0-py3-none-any.whl (10 kB)
Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Downloading sympy-1.13.3-py3-none-any.whl (6.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 1.9 MB/s eta 0:00:00
Downloading asgiref-3.8.1-py3-none-any.whl (23 kB)
Downloading cachetools-5.5.2-py3-none-any.whl (10 kB)
Downloading fsspec-2025.3.2-py3-none-any.whl (194 kB)
Using cached humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Using cached rsa-4.9-py3-none-any.whl (34 kB)
Downloading wrapt-1.17.2-cp312-cp312-win_amd64.whl (38 kB)
Downloading zipp-3.21.0-py3-none-any.whl (9.6 kB)
Downloading filelock-3.18.0-py3-none-any.whl (16 kB)
Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
Downloading pyreadline3-3.5.4-py3-none-any.whl (83 kB)
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
- 
```bash
jazzw@JazzBook:~$ blank ssh
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1021-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Tue Apr 15 06:49:17 2025 from ::1
@jazzwang ➜ /workspaces/codespaces-blank (main) $ pip install chromadb
... skip ...
Successfully installed annotated-types-0.7.0 asgiref-3.8.1 backoff-2.2.1 bcrypt-4.3.0 build-1.2.2.post1 cachetools-5.5.2 chroma-hnswlib-0.7.6 chromadb-1.0.4 click-8.1.8 coloredlogs-15.0.1 deprecated-1.2.18 distro-1.9.0 durationpy-0.9 fastapi-0.115.9 flatbuffers-25.2.10 google-auth-2.39.0 googleapis-common-protos-1.70.0 grpcio-1.71.0 httptools-0.6.4 huggingface-hub-0.30.2 humanfriendly-10.0 importlib-metadata-8.6.1 importlib-resources-6.5.2 kubernetes-32.0.1 markdown-it-py-3.0.0 mdurl-0.1.2 mmh3-5.1.0 monotonic-1.6 oauthlib-3.2.2 onnxruntime-1.21.0 opentelemetry-api-1.32.0 opentelemetry-exporter-otlp-proto-common-1.32.0 opentelemetry-exporter-otlp-proto-grpc-1.32.0 opentelemetry-instrumentation-0.53b0 opentelemetry-instrumentation-asgi-0.53b0 opentelemetry-instrumentation-fastapi-0.53b0 opentelemetry-proto-1.32.0 opentelemetry-sdk-1.32.0 opentelemetry-semantic-conventions-0.53b0 opentelemetry-util-http-0.53b0 orjson-3.10.16 posthog-3.24.1 protobuf-5.29.4 pyasn1-0.6.1 pyasn1-modules-0.4.2 pydantic-2.11.3 pydantic-core-2.33.1 pypika-0.48.9 pyproject_hooks-1.2.0 python-dotenv-1.1.0 requests-oauthlib-2.0.0 rich-14.0.0 rsa-4.9 shellingham-1.5.4 starlette-0.45.3 tenacity-9.1.2 tokenizers-0.21.1 tqdm-4.67.1 typer-0.15.2 typing-inspection-0.4.0 uvicorn-0.34.1 uvloop-0.21.0 watchfiles-1.0.5 websockets-15.0.1 wrapt-1.17.2 zipp-3.21.0
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
