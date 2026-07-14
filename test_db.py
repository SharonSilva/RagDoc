from app.db import get_connection

conn = get_connection()
with conn.cursor() as cur:
    cur.execute("SELECT COUNT(*) FROM chunks;")
    count = cur.fetchone()[0]
    print(f"Connected! chunks table has {count} rows.")
conn.close()