from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from bot.settings import Settings

settings = Settings()
engine = create_engine(settings.db_connection(), echo=settings.debug_queries())
