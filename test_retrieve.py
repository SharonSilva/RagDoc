from app.retrieve import retrieve_chunks

question = "What tool runs a FastAPI app?"
results = retrieve_chunks(question)

print(f"Question: {question}\n")
for i, r in enumerate(results, 1):
    print(f"[{i}] distance={r['distance']:.4f}  source={r['source_title']}")
    print(f"    {r['content'][:80]}...\n")