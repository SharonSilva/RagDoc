-- Enable pgvector (safe to run repeatedly)
CREATE EXTENSION IF NOT EXISTS vector;

-- Each row is one chunk of a document, with its embedding
CREATE TABLE IF NOT EXISTS chunks (
    id            SERIAL PRIMARY KEY,
    document_id   INTEGER NOT NULL,
    content       TEXT NOT NULL,
    source_title  TEXT,
    source_path   TEXT,
    chunk_index   INTEGER,
    embedding     VECTOR(1536),
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);