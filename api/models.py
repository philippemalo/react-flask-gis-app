# from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# class GeometryType(str, Enum):
#     GEOMETRY = "GEOMETRY"
#     POINT = "POINT"
#     LINESTRING = "LINESTRING"
#     POLYGON = "POLYGON"
#     MULTIPOINT = "MULTIPOINT"
#     MULTILINESTRING = "MULTILINESTRING"
#     MULTIPOLYGON = "MULTIPOLYGON"
#     GEOMETRYCOLLECTION = "GEOMETRYCOLLECTION"
#     CURVE = "CURVE"

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    
    project = relationship("Project")
    
    email = Column(String, unique=True)
    password = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    data = relationship('Feature')

    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Feature(Base):
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    
    type = Column(String)
    geom = Column(Geography(geometry_type=None, srid=4326))

    def to_dict(self):
        print('raw geom: ', self.geom)
        return {
            "id": self.id,
            "type": self.type,
            "geom": self.geom
        }

