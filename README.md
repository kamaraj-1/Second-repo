# Second-repo

This repository contains two simple applications: an add numbers script and a Retrieval-Augmented Generation (RAG) app.

## Add Numbers Script

A simple Python script to add two numbers.

### Usage

Run the script with two numbers as arguments:

```bash
python add_numbers.py 5 3
```

This will output: `The sum is: 8.0`

### Options

- `a`: First number (required)
- `b`: Second number (required)

Both arguments must be valid numbers (integers or floats).

## RAG Application

A simple Retrieval-Augmented Generation application that answers questions based on a knowledge base.

### Setup

1. Install dependencies:
```bash
pip install sentence-transformers faiss-cpu transformers torch
```

2. Create or modify `sample.txt` with your knowledge base text.

### Usage

Run the application:

```bash
python rag_app.py
```

Enter your question when prompted, and the app will retrieve relevant information and generate an answer.

### Files

- `rag_app.py`: The main RAG application
- `sample.txt`: Sample knowledge base (you can replace with your own content)
- `architecture.md`: Detailed architecture of the RAG system
- `intuition.md`: Intuitive explanation of how RAG works
- `explanation.md`: In-depth technical explanation of RAG concepts

## Documentation

For a comprehensive understanding of the RAG implementation and concepts:

- **[Architecture](architecture.md)**: System components and data flow
- **[Intuition](intuition.md)**: Conceptual understanding of RAG
- **[Deep Explanation](explanation.md)**: Technical details and theoretical foundations