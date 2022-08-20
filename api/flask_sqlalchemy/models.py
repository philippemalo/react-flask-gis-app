from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

DATABASE_URL = 'postgresql://user:pass@localhost:5432/db'

engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Shape(Base):
    __tablename__ = 'shape'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geometry('POLYGON'))