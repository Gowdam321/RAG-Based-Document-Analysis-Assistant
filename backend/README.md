# Backend Setup

This backend is built using FastAPI and provides APIs for document indexing, retrieval, and question answering.

## Prerequisites

* Python 3.10 or higher
* pip

## Installation

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

Before running the Backend, create a .env file based on the provided .env.example file. you need to create a groq API key for this

## Running the Backend

Navigate to the application directory:

```bash
cd app
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Once the server is running, FastAPI automatically generates API documentation:

```text
Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
```

## Available Endpoints

* `GET /` - Health check
* `POST /upload-pdf` - Upload and index PDF documents
* `POST /upload-text` - Upload and index text content
* `POST /query` - Ask questions from indexed content
* `DELETE /clear-index` - Clear the vector database

```
```
