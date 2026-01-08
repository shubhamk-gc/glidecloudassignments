**Day 03-> 08-Jan

A vector-based document search system using SentenceTransformer embeddings and ChromaDB, without using any Large Language Model (LLM) for answering queries.

The system focuses on indexing, embeddings, and similarity search algorithms, which is a core foundation for Retrieval-Augmented Generation (RAG) systems.

🚀 What This Project Does

Loads documents from a text file

Splits documents into chunks

Converts each chunk into vector embeddings

Stores embeddings in ChromaDB (vector database)

Converts user queries into embeddings

Retrieves the most relevant document chunks using vector similarity search

Exposes the search functionality via a FastAPI endpoint

 No LLM is used for answering
 Only indexing + searching algorithms

Key Concepts Learned->

Embeddings: Numerical vector representations of text

Vector Databases: Efficient storage and retrieval of embeddings

Cosine Distance: Used to measure semantic similarity

Approximate Nearest Neighbor (ANN) search

Chunking strategy for large documents

FastAPI for building ML-backed APIs

Testing with Pytest