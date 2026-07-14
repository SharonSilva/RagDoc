import psycopg
from pgvector.psycopg import register_vector
from app.config import DATABASE_URL

def get_connection():
    """Open a DB connection with pgvector support enabled."""
    conn = psycopg.connect(DATABASE_URL)
    register_vector(conn) #teaches pyscopg how to send/recieve vector types
    return conn
