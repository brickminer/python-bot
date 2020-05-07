from dotenv import load_dotenv
from os import environ

load_dotenv()


class Settings():
    def db_connection(self) -> str:
        return environ.get('DB_CONNECTION') or ""

    def telegram_token(self) -> str:
        return environ.get("TELEGRAM_TOKEN") or ""

    def debug_queries(self) -> bool:
        return environ.get("DEBUG_QUERIES") == 'on'

    def blocked_sets(self) -> list:
        if environ.get("BLOCKED_SETS") != '':
            return environ.get("BLOCKED_SETS").split(',')

        return []
