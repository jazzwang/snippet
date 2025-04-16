import os
import shutil
from pathlib import Path

from git import Repo
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
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