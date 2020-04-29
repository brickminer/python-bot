from os import environ

DATABASE = {
    'drivername': 'mysql+mysqldb',
    'host': environ.get('MYSQL_HOST'),
    'port': environ.get('MYSQL_PORT'),
    'username': environ.get('MYSQL_USER'),
    'password': environ.get('MYSQL_PASS'),
    'database': environ.get('MYSQL_DB')
}

DEBUG = {
    'queries': environ.get("DEBUG_QUERIES") == 1
} 