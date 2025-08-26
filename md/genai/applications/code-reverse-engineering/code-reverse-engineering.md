# Source Code Reverse Engineering

- Gemini 2.5 Flash
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
what are the common steps to build a source code reverse engineering chatbot using LLM? how to build source code index?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Building a source code reverse engineering chatbot using a large language model (LLM) involves a multi-step process that combines natural language processing with code analysis. The core idea is to leverage an LLM's ability to understand and generate human-like text to explain complex codebases, with the help of a specialized code index. This approach, often referred to as Retrieval-Augmented Generation (RAG), prevents the LLM from hallucinating or providing incorrect information by grounding its responses in the actual source code.

***

### Common Steps to Build the Chatbot 🤖

1.  **Data Collection and Pre-processing**:
    * First, you need to collect the source code you want the chatbot to understand. This can be a repository, a folder of files, or a single codebase.
    * The raw code needs to be cleaned. This can include removing non-essential files, stripping out comments, or normalizing the code format to ensure consistency.
    * The cleaned code is then broken down into smaller, manageable chunks. This is a critical step because LLMs have a limited context window. A single file or function might be too large to fit, so you split the code into smaller segments, such as individual functions, classes, or code blocks.

2.  **Building the Code Index**:
    * This is the most crucial part of the RAG pipeline. The code chunks from the previous step are converted into a format that the LLM can quickly search and retrieve from.
    * Each code chunk is passed through an **embedding model** (e.g., a sentence-transformer model or a dedicated code embedding model like CodeBERT). This model converts the code's semantic and syntactic meaning into a numerical vector (an embedding). Code embeddings capture the "essence" of the code—what it does, its dependencies, and its relationships with other code.
    * These embeddings are then stored in a **vector database** (e.g., Pinecone, ChromaDB, or FAISS). A vector database is optimized for similarity searches, meaning it can quickly find the code chunks whose embeddings are most similar to a given query's embedding.

3.  **Chatbot Logic and Integration**:
    * A user submits a query to the chatbot, such as "How does the `login_user` function work?"
    * The chatbot's system takes this natural language query and also converts it into an embedding using the same model used for the code index.
    * The chatbot then performs a **similarity search** in the vector database using the query's embedding. It retrieves the top K most relevant code chunks.
    * These retrieved code chunks are then included in the prompt that is sent to the LLM. The prompt typically follows a template: "Given the following code snippets from the codebase, answer the user's question. Code snippets: [retrieved code]. User question: [original user query]."
    * The LLM processes this enriched prompt, using the provided context to generate a detailed and accurate response about the code. This is where the magic of RAG happens: the LLM's generative power is grounded by the specific, relevant information retrieved from the codebase, which significantly reduces the risk of incorrect or generic answers.

4.  **User Interface and Iteration**:
    * The final step is building a user-friendly interface that allows users to interact with the chatbot.
    * The system should also be designed for continuous improvement. As the codebase changes, the index needs to be updated. You can set up a pipeline to automatically re-index the code when new commits are pushed or when significant changes are made.

***

### How to Build a Source Code Index

Building a source code index for an LLM chatbot is essentially an exercise in **Retrieval-Augmented Generation (RAG)**. It's a pipeline that transforms a codebase into a searchable, machine-readable format. 

Here's a more detailed breakdown:

1.  **Code Parsing and Chunking**:
    * The first step is to parse the source code to understand its structure. Instead of treating code as plain text, you use tools that recognize code syntax, like abstract syntax trees (ASTs). This allows you to identify logical units like functions, classes, and methods.
    * Once parsed, the code is broken into **chunks**. A naive approach is to split by line count, but a better method is to split by logical units (e.g., a full function or class definition). This ensures that each chunk is a coherent, self-contained piece of code that provides meaningful context.

2.  **Embedding Generation**:
    * Each chunk is then converted into a high-dimensional vector, or **embedding**. This is the most resource-intensive part of the process.
    * You need to select an appropriate embedding model. While general-purpose models work, models specifically trained on code (like `text-embedding-3-small` or `codebert-base-embedding`) often produce better results as they have a deeper understanding of code semantics.
    * This is where you'd use a Python library like `sentence-transformers` or a service API from OpenAI or Google to generate the embeddings.

3.  **Vector Database Storage**:
    * After the embeddings are created, they are stored in a **vector database**. This type of database is different from a traditional relational or NoSQL database. Instead of rows and columns, it stores vectors and their associated metadata (e.g., the original code chunk, the file name, and line numbers).
    * The vector database's primary function is to perform **similarity searches** efficiently. When a user query's embedding is submitted, the database uses algorithms like Approximate Nearest Neighbor (ANN) to quickly find the vectors that are closest to the query's vector. The "closest" vectors represent the most semantically relevant code chunks.

4.  **Metadata and Context Enrichment**:
    * To make the chatbot more powerful, you should store additional **metadata** alongside the code embeddings. This could include:
        * **File path and name**: To let the chatbot refer to specific files.
        * **Function/class name**: To provide a high-level overview.
        * **Dependencies**: Information about which functions call which other functions.
        * **Git information**: The commit history, author, and date of the last change.
    * This metadata can be used to create more sophisticated queries and to provide a more comprehensive answer. For example, if a user asks about a function, the chatbot could also retrieve the functions that call it or are called by it, providing a more complete picture of its role in the codebase.
</td></tr></table>

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how can DSPy help in reverse engineering chatbot?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
DSPy is an excellent framework for building a reverse engineering chatbot because it shifts the focus from **manual prompt engineering** to **declarative programming**. Instead of painstakingly crafting and tweaking long prompts, you define the high-level logic of your chatbot using DSPy's modules, signatures, and optimizers. This makes the development process more robust, efficient, and easier to manage, especially for complex tasks like reverse engineering source code.

***

### Core DSPy Concepts for a Code Chatbot

1.  **Signatures**: This is where you declare the input and output types for a specific task. For a reverse engineering chatbot, a signature could be `question, context -> answer`. This tells DSPy that the task is to take a question and some relevant code context, and produce an answer. DSPy then automatically generates the best possible prompt for this signature behind the scenes.

2.  **Modules**: Modules are the building blocks of your program. They are reusable components that implement a specific task defined by a signature. DSPy provides several built-in modules that are perfect for a code analysis chatbot:
    * `dspy.Retrieve`: This module handles the retrieval-augmented generation (RAG) part of the pipeline. You can use it to fetch the most relevant code snippets from your vector database based on the user's question.
    * `dspy.ChainOfThought`: This module instructs the LLM to think step-by-step. For code, this is incredibly valuable. It can be used to generate an explanation of how a function works before summarizing the final answer.
    * `dspy.ProgramOfThought`: This advanced module can be used to make the LLM generate and execute code. For a reverse engineering chatbot, this could mean it writes and runs a small script to test a function and report the result.

3.  **Optimizers**: This is DSPy's most powerful feature. Optimizers are algorithms that automatically improve your program's performance by tuning the prompts and other parameters.
    * You define a **metric** to evaluate your chatbot's performance (e.g., is the generated explanation accurate? Does it refer to the correct code snippets?).
    * You then provide the optimizer with a small set of training examples.
    * The optimizer, using techniques like `BootstrapFewShot`, will iteratively test different prompt variations and find the most effective ones. This automates the trial-and-error process of prompt engineering and makes your chatbot more reliable.

***

### A Reverse Engineering Chatbot Pipeline with DSPy



1.  **Define the RAG Program**: You'd create a DSPy program that connects the modules. For a simple chatbot, this could look like: `dspy.Retrieve` (to get the code) -> `dspy.ChainOfThought` (to analyze the code and explain it) -> a final module to format the answer.

2.  **Set Up the Index**: You still need to build a code index as described in the previous answer, using a vector database. DSPy integrates with popular vector stores like ChromaDB and FAISS, making it easy to connect your `dspy.Retrieve` module to your code index.

3.  **Compile and Optimize**: This is where you leverage DSPy's optimizers. You'd feed the program a few example questions and ideal answers. DSPy's compiler will then automatically generate and refine the prompts for each step of your pipeline, ensuring that the model is performing at its best for the reverse engineering task. This process makes your chatbot more robust against prompt-based failures and reduces the likelihood of hallucinations.

In essence, DSPy allows you to treat your chatbot's logic like a software program, with well-defined components that can be debugged, evaluated, and optimized. This is a significant improvement over manually managing brittle and hard-to-maintain prompts.
</td></tr></table>

- Gemini 2.5 Pro

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
what are the common steps to build a source code reverse engineering chatbot using LLM? how to build source code index?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
## Navigating the Labyrinth of Code: A Guide to Building a Source Code Reverse Engineering Chatbot with LLMs

Revolutionizing the intricate process of source code reverse engineering, Large Language Models (LLMs) can now power intelligent chatbots capable of dissecting and explaining complex codebases. This guide outlines the essential steps to construct such a chatbot and delves into the critical process of building a comprehensive source code index, the backbone of this powerful tool.

---

### Building the Brain: Key Steps to Creating a Reverse Engineering Chatbot

The construction of a source code reverse engineering chatbot involves a systematic process that leverages the power of LLMs to understand and articulate the nuances of software.

#### 1. Defining the Scope and Gathering the Code

The initial and most crucial step is to clearly define the chatbot's objectives. Determine the specific programming languages it will support, the types of questions it should answer (e.g., "What does this function do?", "Trace the data flow of this variable"), and the level of detail expected in its responses. Once the scope is defined, the target source code needs to be collected and organized. This may involve cloning repositories, accessing internal codebases, or integrating with version control systems.

#### 2. Building a Robust Source Code Index

This is the cornerstone of the chatbot's ability to "understand" the code. A well-structured index allows the LLM to quickly and efficiently retrieve relevant code snippets and their associated metadata to answer user queries. The process of building this index is detailed in the following section.

#### 3. Selecting and Fine-Tuning the Large Language Model

Choosing the right LLM is paramount. Consider models with strong code comprehension and generation capabilities. For specialized or proprietary codebases, fine-tuning a pre-trained model on the specific codebase can significantly improve its accuracy and understanding of domain-specific jargon and coding patterns. This process involves preparing a dataset of code-question-answer pairs and using it to further train the model.

#### 4. Designing the Retrieval-Augmented Generation (RAG) Architecture

A Retrieval-Augmented Generation (RAG) architecture is highly effective for this type of chatbot. This approach combines the generative power of an LLM with a retrieval system that fetches relevant information from the source code index. When a user asks a question, the system first retrieves pertinent code snippets and documentation from the index. This retrieved context is then fed to the LLM along with the user's query, enabling the model to generate a more accurate and contextually aware response.

#### 5. Developing the User Interface and Interaction Logic

The user interface (UI) should be intuitive, allowing developers to easily ask questions and view the chatbot's responses, which may include code snippets, explanations, and visualizations. The interaction logic will handle the flow of information from the user to the RAG system and back. This includes parsing user queries, interacting with the retrieval and generation components, and formatting the final output.

#### 6. Testing, Evaluation, and Iterative Improvement

Thorough testing is essential to ensure the chatbot's accuracy and usefulness. Develop a comprehensive test suite with a variety of questions covering different aspects of the codebase. Evaluate the responses for correctness, completeness, and clarity. Based on the evaluation, iteratively refine the indexing process, the LLM fine-tuning, and the overall system architecture.

---

### The Blueprint of Understanding: How to Build a Source Code Index

The source code index is more than just a searchable database; it's a structured representation of the codebase that captures its syntax, semantics, and relationships. Here’s how to build one effectively:

#### 1. Code Parsing and Abstract Syntax Tree (AST) Generation

The first step is to parse the source code into an **Abstract Syntax Tree (AST)** for each file. An AST is a tree representation of the abstract syntactic structure of the code. This provides a structured way to navigate and understand the code's components, such as functions, classes, variables, and their relationships. Tools like `tree-sitter` can be used to generate ASTs for various programming languages.

#### 2. Semantic Chunking of Code

Instead of treating entire files as single documents, it's more effective to break them down into smaller, semantically meaningful chunks. This can be done by traversing the AST and extracting logical units like functions, classes, or even smaller blocks of code. This "semantic chunking" ensures that the retrieved context for the LLM is focused and relevant.

#### 3. Extracting Metadata and Symbol Information

For each code chunk, extract valuable metadata. This includes:
* **Symbol Information:** Identify and index all symbols (variables, functions, classes, etc.) and their scopes.
* **Function Signatures:** Document the parameters and return types of functions.
* **Dependencies and Calls:** Map out the relationships between different parts of the code, such as function calls and class inheritances. This can be achieved through static analysis of the code.

#### 4. Generating Code Embeddings

To enable semantic search, generate **vector embeddings** for each code chunk. Embeddings are numerical representations of the code that capture its semantic meaning. Pre-trained models specifically designed for code, such as those from the `sentence-transformers` library, can be used to convert code snippets into these dense vector representations.

#### 5. Storing in a Vector Database

The code chunks, their metadata, and their corresponding vector embeddings are then stored in a specialized **vector database**. This type of database is optimized for efficient similarity searches. When a user asks a question, their query is also converted into a vector embedding, and the database is searched for the code chunks with the most similar embeddings. Popular vector databases include Pinecone, Weaviate, and Chroma.

By following these steps, you can create a powerful and insightful source code reverse engineering chatbot that can significantly accelerate the process of understanding and navigating complex software systems. This tool can serve as an invaluable assistant for developers, security researchers, and anyone tasked with delving into the intricacies of existing codebases.
</td></tr></table>

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
given a git repo with Perl, Bash scripts and Makefile, how can I build source code index especially leveraging tree-sitter-language-pack using Python and store the index into SQLite as vectore database?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

\<think\>
**Beginning the Answer**

I've initiated the direct response, focusing on the core aspects of building a source code index. I'm aiming for clarity and brevity to address the user's initial query effectively. Next step, building the document!

**Constructing the Outline**

I'm now in the process of building the document. I've formulated a complete Python script that will clone a user-specified Git repo, parse files with relevant extensions using `tree-sitter`, and then split the code into semantic chunks. These chunks will be embedded using `sentence-transformers`. Further steps involve setting up an SQLite database with `sqlite-vss` for vector search, creating a table, and inserting the data. I'll make sure to include detailed comments for clarity.

**Formulating the Script**

I'm now putting together the Python script, focusing on the core steps of cloning the repo, parsing specific file types (.pl, .pm, .sh, .bash, Makefile), and chunking the code. I'm leveraging `tree-sitter` and `tree-sitter-language-pack` for this. The next step will be to handle the fall-back chunking and vector embedding generation with `sentence-transformers`.
\</think\>

Of course. You can build a source code index from a Git repository containing Perl, Bash, and Makefiles by using Python with the `tree-sitter` library for parsing, `sentence-transformers` for creating vector embeddings, and `sqlite-vss` to store and search those vectors within an SQLite database. The process involves cloning the repo, walking through the files, parsing each file's content into manageable chunks based on its language, generating a vector embedding for each chunk, and finally, storing the file path, the code chunk itself, and its vector embedding in an SQLite table equipped for vector search.

Here is a complete, self-contained Python script that accomplishes this.

> Source Code Indexer for Perl, Bash, and Makefiles
> Aug 26, 12:34 PM

> Try again without Canvas

I've created a comprehensive Python script that handles the entire process for you.

This script clones a specified Git repository, identifies Perl, Bash, and Makefile files, and then uses `tree-sitter` to parse them into logical chunks like functions or rules. Each chunk is converted into a numerical vector embedding, which captures its semantic meaning. Finally, it stores these chunks and their vectors in an SQLite database enhanced with vector search capabilities via `sqlite-vss`.

After the indexing is complete, an example query demonstrates how you can search the codebase using natural language to find the most relevant code snippets.

To get started, you'll need to install the dependencies listed in the `requirements.txt` file and ensure you have a C compiler (like GCC, Clang, or MSVC) available for `tree-sitter` to build its language parsers.
</td></tr></table>

```python
# main_indexer.py
import os
import subprocess
import sqlite3
import json
from sentence_transformers import SentenceTransformer
from tree_sitter import Language, Parser

# --- Configuration ---
# URL of the Git repository to index
GIT_REPO_URL = "https://github.com/git-lfs/git-lfs.git" # Example repo with Perl and Bash scripts
# Directory to clone the repository into
REPO_DIR = "temp_repo"
# Path for the SQLite database
DB_FILE = "code_index.db"
# Name of the SentenceTransformer model for embeddings
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
# File extensions to look for
SUPPORTED_EXTENSIONS = {
    ".pl": "perl",
    ".pm": "perl",
    ".sh": "bash",
    ".bash": "bash",
    "Makefile": "make",
}

# --- Tree-sitter Language Setup ---
# Build the shared library for the languages if it doesn't exist
# This requires a C compiler (like GCC or Clang) to be installed.
def setup_tree_sitter_languages():
    """
    Clones tree-sitter grammars and builds a shared library for them.
    This allows the Parser to understand Perl, Bash, and Makefiles.
    """
    print("Setting up tree-sitter languages...")
    if not os.path.exists('build/my-languages.so'):
        if not os.path.exists('vendor/tree-sitter-perl'):
            subprocess.run(["git", "clone", "https://github.com/tree-sitter/tree-sitter-perl", "vendor/tree-sitter-perl"], check=True)
        if not os.path.exists('vendor/tree-sitter-bash'):
            subprocess.run(["git", "clone", "https://github.com/tree-sitter/tree-sitter-bash", "vendor/tree-sitter-bash"], check=True)
        if not os.path.exists('vendor/tree-sitter-make'):
            subprocess.run(["git", "clone", "https://github.com/tree-sitter/tree-sitter-make", "vendor/tree-sitter-make"], check=True)
        
        Language.build_library(
            'build/my-languages.so',
            [
                'vendor/tree-sitter-perl',
                'vendor/tree-sitter-bash',
                'vendor/tree-sitter-make',
            ]
        )
    print("Tree-sitter languages setup complete.")

# Load the built languages
PERL_LANGUAGE = Language('build/my-languages.so', 'perl')
BASH_LANGUAGE = Language('build/my-languages.so', 'bash')
MAKE_LANGUAGE = Language('build/my-languages.so', 'make')

# Map language names to tree-sitter Language objects
LANGUAGE_MAP = {
    "perl": PERL_LANGUAGE,
    "bash": BASH_LANGUAGE,
    "make": MAKE_LANGUAGE,
}

# --- Database Setup ---
def setup_database():
    """
    Initializes the SQLite database, loads the sqlite-vss extension,
    and creates the necessary tables for storing code chunks and their vectors.
    """
    print(f"Setting up database at {DB_FILE}...")
    conn = sqlite3.connect(DB_FILE)
    conn.enable_load_extension(True)
    
    try:
        # Try loading the pre-compiled extension
        import sqlite_vss
        sqlite_vss.load(conn)
        print("sqlite-vss loaded successfully.")
    except ImportError:
        print("Could not import sqlite_vss. Ensure it's installed: pip install sqlite-vss")
        return None
    except Exception as e:
        print(f"Error loading sqlite-vss extension: {e}")
        print("Please ensure the extension is compiled and available.")
        return None

    cursor = conn.cursor()

    # Create the main table for code chunks
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS code_chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL,
        language TEXT NOT NULL,
        chunk_text TEXT NOT NULL,
        start_line INTEGER,
        end_line INTEGER
    )
    ''')

    # Create the virtual table for vector search
    # The vector dimension for 'all-MiniLM-L6-v2' is 384
    cursor.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS vss_chunks USING vss0(
        chunk_embedding(384)
    )
    ''')
    
    conn.commit()
    print("Database setup complete.")
    return conn

# --- Code Parsing and Chunking ---
def get_chunks(file_path, language_name, code_content):
    """
    Parses the code content using tree-sitter and splits it into
    semantic chunks (e.g., functions, subroutines).
    Falls back to line-based chunking if parsing fails.
    """
    parser = Parser()
    language = LANGUAGE_MAP.get(language_name)
    if not language:
        return [] # Skip unsupported languages

    parser.set_language(language)
    tree = parser.parse(bytes(code_content, "utf8"))
    root_node = tree.root_node
    
    chunks = []
    # Query to find top-level functions/subroutines/rules
    # These queries might need adjustment for different grammar versions
    query_map = {
        "perl": "(subroutine_declaration) @sub",
        "bash": "(function_definition) @func",
        "make": "(rule) @rule"
    }
    
    capture_query = language.query(query_map.get(language_name, ""))
    captures = capture_query.captures(root_node)

    if captures:
        for node, _ in captures:
            start_line = node.start_point[0] + 1
            end_line = node.end_point[0] + 1
            chunk_text = node.text.decode('utf8')
            chunks.append({
                "text": chunk_text,
                "start_line": start_line,
                "end_line": end_line
            })
    else:
        # Fallback for files without functions or if query fails
        # Simple chunking by lines
        lines = code_content.splitlines()
        for i in range(0, len(lines), 20): # Chunk every 20 lines
            chunk_lines = lines[i:i+20]
            chunk_text = "\n".join(chunk_lines)
            chunks.append({
                "text": chunk_text,
                "start_line": i + 1,
                "end_line": i + len(chunk_lines)
            })
            
    return chunks

# --- Main Indexing Logic ---
def main():
    """
    Main function to orchestrate the cloning, parsing, embedding, and storing process.
    """
    # 1. Setup dependencies
    setup_tree_sitter_languages()
    conn = setup_database()
    if not conn:
        return
        
    model = SentenceTransformer(EMBEDDING_MODEL)

    # 2. Clone the repository if it doesn't exist
    if not os.path.exists(REPO_DIR):
        print(f"Cloning repository: {GIT_REPO_URL}...")
        subprocess.run(["git", "clone", GIT_REPO_URL, REPO_DIR], check=True)
    else:
        print(f"Repository already exists at {REPO_DIR}.")

    # 3. Walk through the repository and process files
    print("Starting to index files...")
    cursor = conn.cursor()
    total_files = 0
    indexed_files = 0

    for root, _, files in os.walk(REPO_DIR):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            
            # Determine language from extension or filename
            language = None
            if file in SUPPORTED_EXTENSIONS:
                 language = SUPPORTED_EXTENSIONS[file]
            else:
                _, ext = os.path.splitext(file)
                if ext in SUPPORTED_EXTENSIONS:
                    language = SUPPORTED_EXTENSIONS[ext]

            if language:
                indexed_files += 1
                print(f"Processing ({indexed_files}/{total_files}): {file_path}")
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Get code chunks
                    chunks = get_chunks(file_path, language, content)
                    if not chunks:
                        continue

                    # Generate embeddings for all chunks in the file
                    chunk_texts = [chunk['text'] for chunk in chunks]
                    embeddings = model.encode(chunk_texts)

                    # Insert into database
                    for i, chunk in enumerate(chunks):
                        cursor.execute(
                            "INSERT INTO code_chunks (file_path, language, chunk_text, start_line, end_line) VALUES (?, ?, ?, ?, ?)",
                            (file_path, language, chunk['text'], chunk['start_line'], chunk['end_line'])
                        )
                        chunk_id = cursor.lastrowid
                        
                        # Vector embedding needs to be a JSON string for sqlite-vss
                        embedding_json = json.dumps(embeddings[i].tolist())
                        cursor.execute(
                            "INSERT INTO vss_chunks (rowid, chunk_embedding) VALUES (?, ?)",
                            (chunk_id, embedding_json)
                        )

                except Exception as e:
                    print(f"  - Error processing file {file_path}: {e}")
    
    conn.commit()
    conn.close()
    print("\nIndexing complete!")
    print(f"Database saved to {DB_FILE}")

# --- Example Query ---
def run_example_query():
    """
    Demonstrates how to perform a vector similarity search on the indexed data.
    """
    print("\n--- Running Example Query ---")
    conn = sqlite3.connect(DB_FILE)
    conn.enable_load_extension(True)
    import sqlite_vss
    sqlite_vss.load(conn)
    cursor = conn.cursor()

    query_text = "how to handle http requests"
    print(f"Query: '{query_text}'")

    # Generate embedding for the query
    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode(query_text).tolist()
    query_embedding_json = json.dumps(query_embedding)

    # Find the 5 most similar chunks
    results = cursor.execute("""
        SELECT
            c.file_path,
            c.chunk_text,
            c.start_line,
            v.distance
        FROM vss_chunks v
        JOIN code_chunks c ON v.rowid = c.id
        WHERE vss_search(v.chunk_embedding, ?)
        ORDER BY v.distance
        LIMIT 5
    """, (query_embedding_json,)).fetchall()

    print("\nTop 5 similar code chunks found:")
    for i, (path, text, line, distance) in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(f"File: {path} (Line: {line})")
        print(f"Similarity Score (distance): {distance:.4f}")
        print("--- Code ---")
        print(text.strip())
        print("------------")

    conn.close()


if __name__ == "__main__":
    main()
    run_example_query()

```
<hr>

### `requirements.txt`

To run the script, you'll need to install the following Python libraries.

```text
# requirements.txt
# Core libraries
sentence-transformers
tree-sitter
sqlite-vss

# For building tree-sitter languages (optional, but recommended)
gitpython
```