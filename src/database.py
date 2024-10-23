import logging
import sqlite3
import os

from src.models import Tenant

DB_PATH = 'db/tenants.db'

logger = logging.getLogger(__file__)
logger.setLevel(level=logging.INFO)


class DatabaseManager:
    """Manages SQLite database operations."""

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the tenants table if it doesn't exist."""
        logger.info("Initializing database")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS Tenants 
                (address, email, phone_number, company)""")
                logging.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing the database: {e}")

    def insert_tenant(self, tenant: Tenant) -> None:
        """Insert tenant data into the database."""
        logging.info("Inserting tenant")

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                elements = tenant.to_db_tuple()  # Ensure this method returns the correct tuple
                logger.info(f"Inserting tenant data: {elements}")  # Log the data being inserted
                cursor.execute("""INSERT INTO tenants (address, email, phone_number, company)
                VALUES (?, ?, ?, ?);""", elements)

                logger.info("Tenant inserted successfully")
        except Exception as e:
            logger.error(f"Error inserting tenant: {e}")