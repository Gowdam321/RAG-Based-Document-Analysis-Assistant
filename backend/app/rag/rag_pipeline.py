from rag.pdf_loader import (
    extract_text,
    create_chunks
)

from rag.vector_store import (
    save_index,
    search,
    clear_index
)

from rag.llm import (
    generate_answer
)


def process_pdf(pdf_path):

    text = extract_text(pdf_path)

    chunks = create_chunks(text)

    save_index(chunks)

    return len(chunks)

def process_text(text):
    chunks = create_chunks(text)
    save_index(chunks)
    return len(chunks)


def ask_question(query):

    retrieved_chunks = search(query)

    context = "\n\n".join(retrieved_chunks)

    answer = generate_answer(
        context,
        query
    )

    return {
        "query": query,
        "answer": answer,
        "context": retrieved_chunks
    }


def clear_vector_database():

    clear_index()

    return {
        "message": "Vector database cleared"
    }