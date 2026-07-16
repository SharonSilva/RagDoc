from app.ingest import ingest_document

sample= """
FastAPI is a modern Python web framework for building APIs.
It is based on standard Python type hints and is very fast.
FastAPI automatically generates interactive API documentation.
Uvicorn is the server that runs FastAPI applications.
Pydantic handles data validation in FastAPI using type annotations.
"""

count = ingest_document(
    text=sample,
    document_id=1,
    source_title="FastAPI Intro",
    source_path="docs/fastapi-intro",
)
print(f"Ingested {count} chunk(s)")