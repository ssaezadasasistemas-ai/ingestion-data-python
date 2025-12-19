import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config(database: str) -> dict:
    return {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": database,
        "port": int(os.getenv("MYSQL_PORT", 3306))
    }
