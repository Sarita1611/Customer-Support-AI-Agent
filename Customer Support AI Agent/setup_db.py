import sqlite3

conn = sqlite3.connect("support.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    issue TEXT,
    status TEXT
)
""")

cur.executemany("""
INSERT INTO customers (name, email, issue, status) VALUES (?, ?, ?, ?)
""", [
    ('Alice', 'alice@example.com', 'Payment failed', 'open'),
    ('Bob', 'bob@example.com', 'Login issue', 'resolved'),
    ('Charlie', 'charlie@example.com', 'Cannot reset password', 'open')
])

conn.commit()
conn.close()
print("✅ Database setup complete.")
