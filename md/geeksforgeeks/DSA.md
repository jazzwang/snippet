# Data Structure and Algorithm

- https://www.geeksforgeeks.org/explore - 刷題大全

## 2024-09-11

以前沒學過資料結構與演算法，所以先了解一下 High Level Overview

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230807133054/Data-structure-algorithm.png)
Source: https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/

- DP 是指 [Dynamic Programing](https://en.wikipedia.org/wiki/Dynamic_programming) 也就是中文的「動態規劃」

### Overview of Data Structures and Algorithms (1)

- From https://www.perplexity.ai
- Prompt:
> could you give me a high-level overview of data structure and algorithm?

Data structures and algorithms are fundamental concepts in computer science that work hand-in-hand to efficiently organize and manipulate data. Here's a high-level overview:

- **Data Structures**: These are specialized formats for storing and organizing data to support efficient access and modifications. Common data structures include:
    - Arrays
    - Linked Lists
    - Stacks
    - Queues
    - Trees (Binary Search Trees, AVL Trees, Red-Black Trees, etc.)
    - Graphs
    - Hash Tables
* **Algorithms**: These are well-defined procedures for solving problems, often using one or more data structures. Some popular algorithm categories are:
    - Searching (Linear Search, Binary Search, etc.)
    - Sorting (Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, etc.)
    - Graph Algorithms (Depth-First Search, Breadth-First Search, Dijkstra's Algorithm, etc.)
    - Dynamic Programming
    - Divide and Conquer
    - Greedy Algorithms
    - Backtracking

### Overview of Data Structures and Algorithms (2)

- from chat.openai.com = https://chatgpt.com/
- prompt:
> could you give me a high-level overview of data structure and algorithm?

Data structures and algorithms are fundamental concepts in computer science that help us efficiently store, organize, and process data. Here's a high-level overview:

#### Data Structures

1. **Arrays**: 
   - **Description**: Fixed-size collections of elements, all of the same type, stored in contiguous memory locations.
   - **Usage**: Access elements by index, useful for simple lists and tables.

2. **Linked Lists**:
   - **Description**: Collections of nodes, where each node contains data and a reference (or link) to the next node.
   - **Types**: Singly linked list, doubly linked list, circular linked list.
   - **Usage**: Useful for dynamic data where the size may change.

3. **Stacks**:
   - **Description**: Collections of elements with Last-In-First-Out (LIFO) access.
   - **Operations**: Push (add), Pop (remove), Peek (view top element).
   - **Usage**: Useful for managing function calls, undo mechanisms, etc.

4. **Queues**:
   - **Description**: Collections of elements with First-In-First-Out (FIFO) access.
   - **Operations**: Enqueue (add), Dequeue (remove).
   - **Usage**: Useful for task scheduling, buffering.

5. **Hash Tables**:
   - **Description**: Data structures that map keys to values using a hash function to compute an index.
   - **Usage**: Efficient for lookups, insertions, and deletions.

6. **Trees**:
   - **Description**: Hierarchical structures with nodes connected by edges. Each node has zero or more child nodes.
   - **Types**: Binary trees, binary search trees, AVL trees, B-trees.
   - **Usage**: Useful for hierarchical data representation, fast searches, and sorted data.

7. **Graphs**:
   - **Description**: Collections of nodes (vertices) and edges connecting pairs of nodes.
   - **Types**: Directed, undirected, weighted, unweighted.
   - **Usage**: Useful for network representation, shortest path problems, etc.

#### Algorithms

1. **Sorting Algorithms**:
   - **Examples**: Bubble sort, Merge sort, Quick sort, Heap sort.
   - **Usage**: Arrange data in a specific order. Efficiency varies (e.g., O(n^2) for Bubble sort, O(n log n) for Quick sort).

2. **Searching Algorithms**:
   - **Examples**: Linear search, Binary search.
   - **Usage**: Find an element in a collection. Binary search is efficient for sorted data (O(log n)).

3. **Graph Algorithms**:
   - **Examples**: Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra’s algorithm, Kruskal’s algorithm.
   - **Usage**: Solve problems related to paths and connectivity in graphs.

4. **Dynamic Programming**:
   - **Description**: Technique to solve problems by breaking them into simpler subproblems and storing the results to avoid redundant computations.
   - **Examples**: Fibonacci sequence, Knapsack problem.

5. **Greedy Algorithms**:
   - **Description**: Build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
   - **Examples**: Prim’s algorithm for minimum spanning tree, Huffman coding.

6. **Divide and Conquer**:
   - **Description**: Break a problem into smaller subproblems, solve each subproblem independently, and combine their solutions.
   - **Examples**: Merge sort, Quick sort.

Understanding these concepts helps in designing efficient software and solving complex computational problems. Data structures provide the means to manage and access data effectively, while algorithms give us the methods to perform computations and solve problems efficiently.