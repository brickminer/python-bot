from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from ..settings import DB_CONNECTION, DEBUG_QUERIES


engine = create_engine(DB_CONNECTION,
                       echo=bool(DEBUG_QUERIES))
