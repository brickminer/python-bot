from dotenv import load_dotenv
from os import environ

load_dotenv()

DB_CONNECTION = environ.get('DB_CONNECTION')
TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN")
DEBUG_QUERIES = environ.get("DEBUG_QUERIES") == 'on'

if environ.get("BLOCKED_SETS") != '':
    BLOCKED_SETS = environ.get("BLOCKED_SETS").split(',')
else:
    BLOCKED_SETS = []
