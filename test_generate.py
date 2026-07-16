from app.generate import answer_question

question= "What runs a FastAPI application?"
result = answer_question(question)

print(f"Q: {question}\n")
print(f"A: {result['answer']}\n")
print("Sources:")
for s in result["sources"]:
    print(f"    [{s['n']}] {s['title']}")