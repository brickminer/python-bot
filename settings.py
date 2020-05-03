from os import environ

DATABASE = {
    'drivername': 'mysql+mysqldb',
    'host': environ.get('MYSQL_HOST'),
    'port': environ.get('MYSQL_PORT'),
    'username': environ.get('MYSQL_USER'),
    'password': environ.get('MYSQL_PASS'),
    'database': environ.get('MYSQL_DB')
}


TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN")
DEBUG_QUERIES = environ.get("DEBUG_QUERIES") == 'on'


if environ.get("BLOCKED_SETS") is not None:
    BLOCKED_SETS = environ.get("BLOCKED_SETS").split(',')
else:
    BLOCKED_SETS = []
