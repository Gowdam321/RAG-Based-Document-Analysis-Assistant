# RAG-Based Document Analysis Assistant

An AI-powered Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents or text content and ask questions based on the provided knowledge source. The system uses semantic search and vector embeddings to retrieve relevant context and generate accurate responses.

---

## Features

* Upload and index PDF documents
* Upload and index plain text content
* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG)
* Interactive chat interface
* FastAPI backend
* React frontend
* FAISS vector database
* Clear and rebuild vector index

---

## Architecture

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Document Processing
 │
 ├── Text Chunking
 │
 ├── Embedding Generation
 │
 ▼
FAISS Vector Database
 │
 ▼
Context Retrieval
 │
 ▼
LLM Response Generation
 │
 ▼
Answer Returned to User
```

---

## Tech Stack

### Frontend

* React
* Vite
* Axios
* CSS

### Backend

* FastAPI
* Uvicorn
* FAISS
* Sentence Transformers
* NumPy
* PyMuPDF / PDF Processing
* Pydantic

### AI Components

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Similarity Search

---


## Setup Instructions

### Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Before running the Backend, create a .env file based on the provided .env.example file. you need to create a groq API key for this

Run the backend:

```bash
cd app
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### Frontend

Navigate to the frontend directory:

```bash
cd frontend
```

Navigate to the Rag_system directory:

```bash
cd Rag_system
```

Install dependencies:

```bash
npm install
```

Before running the project, create a .env file based on the provided .env.example file. find the backend url by running the backend by default it is http://127.0.0.1:8000

Run the development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Documentation

FastAPI automatically generates API documentation:

```text
Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
```

---

## Workflow

1. Upload a PDF document or text content.
2. The document is split into chunks.
3. Embeddings are generated for each chunk.
4. Chunks are stored in a FAISS vector database.
5. User submits a question.
6. Relevant chunks are retrieved using semantic search.
7. Retrieved context is passed to the language model.
8. An accurate answer is returned to the user.

---

## Future Improvements

* Multi-document support
* Chat history persistence
* Hybrid search (Keyword + Semantic)
* Reranking models
* Authentication and user accounts
* Cloud deployment
* Source citation for responses

---

## Author

Gowdam M

Electronics and Communication Engineering Student | AI & Software Development Enthusiast
