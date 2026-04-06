import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'paddles.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seen_paddles (
            key TEXT PRIMARY KEY,
            brand TEXT,
            model TEXT,
            date_added TEXT,
            source TEXT
        )
    ''')
    conn.commit()
    conn.close()

def is_new_paddle(key):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM seen_paddles WHERE key = ?', (key,))
    exists = cursor.fetchone()
    conn.close()
    return exists is None

def save_paddle(paddle):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO seen_paddles (key, brand, model, date_added, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (paddle['key'], paddle['brand'], paddle['model'], paddle['date_added'], paddle['source']))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
