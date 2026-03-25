# RAG App Architecture

## Overview
This simple RAG (Retrieval-Augmented Generation) application consists of several key components that work together to provide question-answering capabilities based on a knowledge base.

## Components

### 1. Document Loader
- **Purpose**: Loads and preprocesses text documents from files.
- **Functionality**: Reads text files, splits content into manageable chunks (sentences in this simple implementation).
- **Output**: List of document chunks.

### 2. Embedding Model
- **Purpose**: Converts text into vector representations.
- **Library**: SentenceTransformers (all-MiniLM-L6-v2 model).
- **Functionality**: Encodes documents and queries into dense vectors.
- **Output**: High-dimensional vectors representing semantic meaning.

### 3. Vector Database
- **Purpose**: Stores and searches document embeddings efficiently.
- **Library**: FAISS (Facebook AI Similarity Search).
- **Functionality**: Indexes embeddings for fast similarity search.
- **Output**: Indices of most similar documents for a given query.

### 4. Retriever
- **Purpose**: Finds relevant documents for a user query.
- **Functionality**: Encodes query, searches vector database, returns top-k similar documents.
- **Output**: List of relevant document chunks.

### 5. Generator
- **Purpose**: Produces natural language responses.
- **Library**: Hugging Face Transformers (GPT-2 model).
- **Functionality**: Takes query and retrieved documents as context to generate answers.
- **Output**: Coherent text response.

## Data Flow

1. **Indexing Phase**:
   - Documents → Document Loader → Embedding Model → Vector Database

2. **Query Phase**:
   - User Query → Embedding Model → Retriever → Retrieved Documents → Generator → Answer

## Dependencies
- sentence-transformers: For text embeddings
- faiss-cpu: For vector similarity search
- transformers: For text generation
- torch: Backend for ML models

## Limitations
- Simple sentence-based chunking (may not preserve context)
- In-memory FAISS index (not persistent)
- Basic text generation without fine-tuning
- No advanced retrieval techniques (e.g., re-ranking)