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