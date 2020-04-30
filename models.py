from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine.url import URL
from datetime import datetime

import settings

engine = create_engine(URL(**settings.DATABASE), echo=bool(settings.DEBUG_QUERIES))

Base = declarative_base()

class LegoSet(Base):
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
    uk_price = Column('uk_price', Float(5,2), nullable=True)	
    us_price = Column('us_price', Float(5,2), nullable=True)	
    eu_price = Column('eu_price', Float(5,2), nullable=True)
    packaging = Column('packaging', String(255), nullable=True)	
    dimensions = Column('dimensions', String(255), nullable=True)	
    weight = Column('weight', String(255), nullable=True)	
    barcodes = Column('barcodes', String(255), nullable=True)	
    item_number = Column('item_number', String(255), nullable=True)	
    image = Column('image', String(255), nullable=True)	
    url = Column('url', String(255), nullable=True)	
    created = Column('created', DateTime, default=datetime.now())	
    updated	= Column('updated', DateTime, nullable=True)

    def __repr__(self):
        return '<Id {} Name {} Number {}>'.format(self.id, self.name, self.number)        


def create_tables():
    Base.metadata.create_all(bind=engine)   


def save(item):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(item)
    session.commit()
    session.close

def fetch_all(class_name):
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(class_name).all() 


def search_lego_set(search):
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(LegoSet).filter(or_(LegoSet.name.like('%' + search + '%'), LegoSet.number.like('%' + search + '%'))).limit(10)