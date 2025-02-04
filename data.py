import sqlite3

DB_NAME = "finance_tracker.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        type TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect(DB_NAME)
