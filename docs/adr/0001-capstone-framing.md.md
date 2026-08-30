ADR-0001: Capstone Framing — Document Knowledge Assistant
Status: Draft v1
Date: 2026-08-30
Author: Ashish

Context

Users often need to find specific information across a collection of documents without manually reading every file. This capstone aims to build a Knowledge Assistant that allows users to ask questions in natural language and receive relevant, grounded answers from their uploaded documents.

Inputs	: The user sends natural-language questions along with documents such as PDFs, Word files, or text files containing the knowledge base.
Outputs : The system produces a concise, context-aware answer supported by relevant document references or citations.
Tools	: The system uses an LLM such as OpenAI, a document parser, an embedding model, a vector retriever/vector database, and a backend API such as FastAPI.
Memory	: No As of now
Autonomy level : The system operates as a retrieval-augmented assistant that autonomously retrieves relevant information and generates an answer while remaining user-driven rather than independently executing actions.
Decision boundaries	: The assistant may decide which document chunks are relevant and how to formulate the answer, but it must not invent information or make decisions beyond what is supported by the provided knowledge base.
Success metrics : output is generated, grounded response from documents, hallucination rate