from openai import OpenAI
from app.config import OPENAI_API_KEY, CHAT_MODEL
from app.retrieve import retrieve_chunks

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """You are a documentation assistant.Answer the user's question \
    using ONLY the numbered context sources provided. If the answer is not in the  \
    context, say "I dont have information about that in the documentation," \
    When you use a source, cite it inline like [1], [2]. Be concise and accurate."""
    
def build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into numbered sources for the prompt."""
    parts = []
    for i, chunk in enumerate(chunks, 1):
        parts.append(f"[{i}] (from {chunk['source_title']})\n{chunk['content']}")
    return "\n\n".join(parts)

def answer_question(question: str, top_k: int=3) -> dict:
    """Full RAG: retrieve, ground, generate ans answer with citations"""
    chunks = retrieve_chunks(question,top_k= top_k)
    
    if not chunks:
        return {"answer": "No documentation have been ingested yet.", "sources": []}
    
    context = build_context(chunks)
    user_prompt = f"Context sources:\n\n{context}\n\nQuestion: {question}"
    
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content":user_prompt},
        ],
    )
    
    answer = resp.choices[0].message.content
    
    #Return the answer plus the sources it could have cited 
    sources = [
        {"n": i, "title": c["source_title"], "path": c["source_path"]}
        for i,c in enumerate(chunks,1)
    ]
    return {"answer": answer, "sources": sources}