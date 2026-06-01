import fitz
import re


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = []

    for page in doc:

        blocks = page.get_text("blocks")

        blocks.sort(key=lambda b: (b[1], b[0]))

        page_text = []

        for block in blocks:

            text = block[4].strip()

            if not text:
                continue

            page_text.append(text)

        full_text.append("\n".join(page_text))

    return "\n\n".join(full_text)


def clean_text(text):

    text = re.sub(r'\r', '\n', text)

    text = re.sub(r'\n\s*\n+', '\n\n', text)

    return text.strip()


def split_into_paragraphs(text):

    return [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]


def count_words(text):

    return len(text.split())


def create_chunks(text, min_words=70, max_words=170):

    text = clean_text(text)

    paragraphs = split_into_paragraphs(text)

    chunks = []

    current_chunk = []

    current_words = 0

    for para in paragraphs:

        para_words = count_words(para)

        if para_words > max_words:

            if current_chunk:
                chunks.append("\n\n".join(current_chunk))

            sentences = re.split(
                r'(?<=[.!?])\s+',
                para
            )

            temp = []

            temp_words = 0

            for sentence in sentences:

                sentence_words = count_words(sentence)

                if temp_words + sentence_words > max_words:

                    chunks.append(" ".join(temp))

                    temp = [sentence]

                    temp_words = sentence_words

                else:

                    temp.append(sentence)

                    temp_words += sentence_words

            if temp:
                chunks.append(" ".join(temp))

            current_chunk = []

            current_words = 0

            continue

        if current_words + para_words > max_words:

            if current_words >= min_words:

                chunks.append("\n\n".join(current_chunk))

                current_chunk = [para]

                current_words = para_words

            else:

                current_chunk.append(para)

                chunks.append("\n\n".join(current_chunk))

                current_chunk = []

                current_words = 0

        else:

            current_chunk.append(para)

            current_words += para_words

    if current_chunk:

        if chunks and current_words < min_words:

            chunks[-1] += (
                "\n\n" +
                "\n\n".join(current_chunk)
            )

        else:

            chunks.append(
                "\n\n".join(current_chunk)
            )

    return chunks