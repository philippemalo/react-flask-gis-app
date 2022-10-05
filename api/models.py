# from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float
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
    
    projects = relationship("Project")
    models = relationship("Model")

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
    
    points = relationship('Point')
    linestrings = relationship('Linestring')
    polygon = relationship('Polygon')

    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    points = relationship('ModelPoint')
    linestrings = relationship('ModelLinestring')
    polygons = relationship('ModelPolygon')

    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Point(Base):
    __tablename__ = 'point'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))

    geom = Column(Geography(geometry_type='POINT', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }

class Linestring(Base):
    __tablename__ = 'linestring'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))

    geom = Column(Geography(geometry_type='LINESTRING', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }

class Polygon(Base):
    __tablename__ = 'polygon'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))

    geom = Column(Geography(geometry_type='POLYGON', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }


class ModelPoint(Base):
    __tablename__ = 'modelpoint'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"))

    geom = Column(Geography(geometry_type='POINT', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }

class ModelLinestring(Base):
    __tablename__ = 'modellinestring'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"))

    geom = Column(Geography(geometry_type='LINESTRING', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }

class ModelPolygon(Base):
    __tablename__ = 'modelpolygon'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"))

    geom = Column(Geography(geometry_type='POLYGON', srid=4326))

    def to_dict(self):
        return {
            "id": self.id,
            "geom": self.geom
        }

class ProjectModel(Base):
    __tablename__ = 'projectmodel'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    model_id = Column(Integer, ForeignKey("model.id"))

    lat = Column(Float)
    lng = Column(Float)
    rotation = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "model_id": self.model_id,
            "project_id": self.project_id,
            "lat": self.lat,
            "lng": self.lng,
            "rotation": self.rotation
        }

    