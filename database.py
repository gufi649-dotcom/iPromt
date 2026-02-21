import sqlite3

conn = sqlite3.connect("prompts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prompts (
id INTEGER PRIMARY KEY,
image TEXT,
prompt TEXT UNIQUE,
description TEXT,
posted INTEGER DEFAULT 0
)
""")

conn.commit()

def save_prompt(image, prompt, description):
    try:
        cursor.execute(
            "INSERT INTO prompts (image, prompt, description) VALUES (?, ?, ?)",
            (image, prompt, description)
        )
        conn.commit()
    except:
        pass

def get_unposted():
    cursor.execute("SELECT id, image, prompt, description FROM prompts WHERE posted=0 LIMIT 1")
    return cursor.fetchone()

def mark_posted(pid):
    cursor.execute("UPDATE prompts SET posted=1 WHERE id=?", (pid,))
    conn.commit()
