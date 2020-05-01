from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

import settings

def get_engine():
    return create_engine(URL(**settings.DATABASE), echo=bool(settings.DEBUG_QUERIES))        