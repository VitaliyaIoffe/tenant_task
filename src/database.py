import sqlite3
import os

from src.models import Tenant

DB_PATH = 'db/tenants.db'


class DatabaseManager:
    """Manages SQLite database operations."""

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the tenants table if it doesn't exist."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tenants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT,
                email TEXT,
                phone_number TEXT,
                company TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_tenant(self, tenant: Tenant) -> None:
        """Insert tenant data into the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tenants (address, email, phone_number, company)
            VALUES (?, ?, ?, ?)
        """, tenant.to_db_tuple())

        conn.commit()
        conn.close()
