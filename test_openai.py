from openai import OpenAI
from app.config import OPENAI_API_KEY, EMBEDDING_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

resp = client.embeddings.create(
    model=EMBEDDING_MODEL,
    input="hello world",
)

vector = resp.data[0].embedding
print(f"Got an embedding with {len(vector)} dimensions")
print(f"First 5 numbers: {vector[:5]}")
