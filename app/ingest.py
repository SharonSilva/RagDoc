from openai import OpenAI
from app.config import OPENAI_API_KEY, EMBEDDING_MODEL
from app.db import get_connection

client = OpenAI(api_key=OPENAI_API_KEY)


def chunk_text(text: str, chunk_size: int = 500, overlap: int= 50) -> list[str]:
    """ Split text into overlapping word-based chunks. """
    words= text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap # step forward, leaving an overlap
    return chunks

def embed_text(text: str) -> list[float]:
    """Turn one piece of text into a 1536-dim embedding"""
    resp = client.embeddings.create(model=EMBEDDING_MODEL, input=text)
    return resp.data[0].embedding

def ingest_document(
    text: str,
    document_id: int,
    source_title: str,
    source_path: str,
) -> int:
    """Chunk a document, embed each chunk and store them.Returns chunk count."""
    chunks = chunk_text(text)
    conn = get_connection()
    with conn.cursor() as cur:
        for index, chunk in enumerate(chunks):
            embedding = embed_text(chunk)
            cur.execute(
                """
                INSERT INTO chunks
                    (document_id, content, source_title, source_path, chunk_index, embedding)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (document_id, chunk, source_title, source_path, index, embedding)
            )
        conn.commit()
    conn.close()
    return len(chunks)
        
        
        
