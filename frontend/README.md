# Frontend Setup

This frontend is built using React and provides the user interface for uploading documents and interacting with the RAG assistant.

## Prerequisites

* Node.js
* npm

## Installation

Navigate to the frontend directory:

```bash
cd frontend
```

Navigate to the Rag_system directory:

```bash
cd Rag_system
```

Install all required dependencies:

```bash
npm install
```

Before running the project, create a .env file based on the provided .env.example file. find the backend url by running the backend by default it is http://127.0.0.1:8000

## Running the Frontend

Start the development server:

```bash
npm run dev
```

The application will be available at the URL displayed in the terminal (typically):

```text
http://localhost:5173
```

## Features

* PDF Upload
* Text Upload
* Chat Interface
* Vector Database Management
* Retrieval-Augmented Question Answering

## Backend Requirement

Ensure the FastAPI backend is running before starting the frontend.
