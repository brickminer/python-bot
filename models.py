from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine.url import URL
from datetime import datetime
from formatters import format_currency, format_text
import database

DeclarativeBase = declarative_base()


class LegoSet(DeclarativeBase):
    engine = database.get_engine()

    __tablename__ = 'sets'
    id = Column('id', Integer, primary_key=True)
    number = Column('number', String(20))
    name = Column('name', String(255))
    type = Column('type', String(255), nullable=True)
    theme_group = Column('theme_group', String(255), nullable=True)
    theme = Column('theme', String(255), nullable=True)
    subtheme = Column('subtheme', String(255), nullable=True)
    tags = Column('tags', String(1000), nullable=True)
    year = Column('year', Integer, nullable=True)
    pieces = Column('pieces', Integer, nullable=True)
    minifigs = Column('minifigs', Integer, nullable=True)
    uk_price = Column('uk_price', Float(5, 2), nullable=True)
    us_price = Column('us_price', Float(5, 2), nullable=True)
    eu_price = Column('eu_price', Float(5, 2), nullable=True)
    packaging = Column('packaging', String(255), nullable=True)
    dimensions = Column('dimensions', String(255), nullable=True)
    weight = Column('weight', String(255), nullable=True)
    barcodes = Column('barcodes', String(255), nullable=True)
    item_number = Column('item_number', String(255), nullable=True)
    image = Column('image', String(255), nullable=True)
    url = Column('url', String(255), nullable=True)
    created = Column('created', DateTime, default=datetime.now())
    updated = Column('updated', DateTime, nullable=True)

    def __repr__(self):
        return '<Id {} Name {} Number {}>'.format(self.id, self.name, self.number)

    def all():
        Session = sessionmaker(bind=LegoSet.engine)
        session = Session()

        return session.query(LegoSet).all()

    def search(text):
        Session = sessionmaker(bind=LegoSet.engine)
        session = Session()

        name_filter = LegoSet.name.like('%' + text + '%')
        number_filter = LegoSet.number.like('%' + text + '%')

        return session.query(LegoSet).filter(or_(name_filter, number_filter)).limit(10).all()

    def create(self):
        Session = sessionmaker(bind=LegoSet.engine)
        session = Session()
        session.add(self)
        session.commit()
        session.close

    def set_info(self):
        template = "Set Number: {}\nName: {}\nParts: {}\nMinifigs: {}\nYear: {}\nUS Price: {}\nEU Price: {}\nUK Price: {}"

        return template.format(
            format_text(self.number),
            format_text(self.name),
            format_text(self.pieces),
            format_text(self.minifigs),
            format_text(self.year),
            format_currency(self.us_price),
            format_currency(self.eu_price),
            format_currency(self.uk_price)
        )
