# db.py
import sqlite3
from typing import Optional

DB_PATH = "bot_settings.db"

class DB:
    def __init__(self, path=DB_PATH):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self._init_tables()

    def _init_tables(self):
        c = self.conn.cursor()
        c.execute("""
CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
)""")
        self.conn.commit()

    def set(self, key: str, value: str):
        c = self.conn.cursor()
        c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()

    def get(self, key: str) -> Optional[str]:
        c = self.conn.cursor()
        c.execute("SELECT value FROM settings WHERE key = ?", (key,))
        r = c.fetchone()
        return r[0] if r else None

    def delete(self, key: str):
        c = self.conn.cursor()
        c.execute("DELETE FROM settings WHERE key = ?", (key,))
        self.conn.commit()

db = DB()
