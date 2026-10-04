from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from pydantic import BaseModel

import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from rag.rag_pipeline import (
    process_pdf,
    process_text,
    ask_question,
    clear_vector_database
)


app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):

    query: str

class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():

    return {
        "message": "RAG API Running"
    }


@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
    UPLOAD_DIR,
    file.filename
)

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    total_chunks = process_pdf(file_path)

    return {
        "message": "PDF indexed successfully",
        "chunks_created": total_chunks
    }


@app.post("/upload-text")
async def upload_text(request: TextRequest):

    total_chunks = process_text(request.text)
    return {
        "message": "Text indexed successfully",
        "chunks_created": total_chunks
    }

@app.post("/query")
async def query_rag(
    request: QueryRequest
):

    result = ask_question(
        request.query
    )

    return result

@app.delete("/clear-index")
async def clear_index_endpoint():

    result = clear_vector_database()

    return result