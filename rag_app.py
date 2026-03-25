#!/usr/bin/env python3

import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

class SimpleRAG:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2', generator_model='gpt2'):
        self.embedder = SentenceTransformer(model_name)
        self.generator = pipeline('text-generation', model=generator_model)
        self.index = None
        self.documents = []

    def load_documents(self, file_path):
        with open(file_path, 'r') as f:
            text = f.read()
        # Split into chunks (simple sentence split)
        self.documents = text.split('. ')
        self.documents = [doc.strip() for doc in self.documents if doc.strip()]

    def build_index(self):
        embeddings = self.embedder.encode(self.documents)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype('float32'))

    def retrieve(self, query, k=3):
        query_embedding = self.embedder.encode([query])
        distances, indices = self.index.search(query_embedding.astype('float32'), k)
        retrieved_docs = [self.documents[i] for i in indices[0]]
        return retrieved_docs

    def generate_answer(self, query, retrieved_docs):
        context = ' '.join(retrieved_docs)
        prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
        result = self.generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text'].split('Answer:')[1].strip()

    def answer_query(self, query):
        retrieved = self.retrieve(query)
        answer = self.generate_answer(query, retrieved)
        return answer

if __name__ == "__main__":
    rag = SimpleRAG()
    # Assume a sample.txt exists
    if os.path.exists('sample.txt'):
        rag.load_documents('sample.txt')
        rag.build_index()
        query = input("Enter your question: ")
        answer = rag.answer_query(query)
        print(f"Answer: {answer}")
    else:
        print("Please create a sample.txt file with some text.")