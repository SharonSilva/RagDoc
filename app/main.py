from fastapi import FastAPI

app = FastAPI(title="RagDoc API")

@app.get("/health")
def health():
    return {"status": "ok"}



