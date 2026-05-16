import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    DB_PATH    = os.getenv("DB_PATH", "maBase.db")
    DB_TIMEOUT = int(os.getenv("DB_TIMEOUT", 30))
