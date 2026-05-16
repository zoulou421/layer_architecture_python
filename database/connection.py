import sqlite3
from config import DatabaseConfig


class Database:
    def __init__(self):
        self.db_path  = DatabaseConfig.DB_PATH
        self.timeout  = DatabaseConfig.DB_TIMEOUT
        self._initialize()

    def _initialize(self):
        """Crée les tables si elles n'existent pas"""
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT    NOT NULL,
                    last_name  TEXT    NOT NULL,
                    email      TEXT
                )
            """)
            conn.commit()

    def get_connection(self):
        """Retourne une connexion SQLite"""
        return sqlite3.connect(self.db_path, timeout=self.timeout)
