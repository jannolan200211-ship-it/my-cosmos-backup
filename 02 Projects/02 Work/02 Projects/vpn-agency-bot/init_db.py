import sqlite3
import os

DB_PATH = "/root/.openclaw/workspace/02 Work/02 Projects/vpn-agency-bot/vpn_agency.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER PRIMARY KEY,
            username TEXT,
            full_name TEXT,
            active_plan TEXT,
            expiry_date TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Keys Table (Outline Keys)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vpn_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key_id TEXT UNIQUE,
            access_url TEXT,
            region TEXT,
            data_limit INTEGER,
            is_assigned INTEGER DEFAULT 0,
            assigned_to INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assigned_to) REFERENCES users (chat_id)
        )
    ''')

    # Payments Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount INTEGER,
            region TEXT,
            screenshot_file_id TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (chat_id)
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")

if __name__ == "__main__":
    init_db()
