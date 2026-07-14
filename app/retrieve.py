from app.ingest import embed_text
from app.db import get_connection

def retrieve_chunks(question:str, top_k:int = 3) -> list[dict]:
    """ Embed the question and return the top_k most similar chunks."""
    query_embedding = embed_text(question)
    
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            """ 
            SELECT 
                id,
                content,
                source_title,
                source_path,
                embedding <=> %s::vector as distance
            FROM chunks
            ORDER BY distance
            LIMIT %s
            """,
            (query_embedding, top_k),
        )
        rows = cur.fetchall()
    conn.close()
    
    return [
        {
            "id": row[0],
            "content": row[1],
            "source_title": row[2],
            "source_path": row[3],
            "distance": row[4],
        }
        for row in rows
    ]