from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class GeometryType(str, Enum):
    POINT = "POINT"
    MULTIPOINT = "MULTIPOINT"
    LINESTRING = "LINESTRING"
    MULTILINESTRING = "MULTILINESTRING"
    POLYGON = "POLYGON"
    MULTIPOLYGON = "MULTIPOLYGON"

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
            "email": self.email
        }

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    models = relationship('ProjectModel')
    feature_collection = relationship('Feature')

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

    feature_collection = relationship('Feature')

    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class ProjectModel(Base):
    __tablename__ = 'projectmodel'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    model_id = Column(Integer, ForeignKey("model.id"))

    feature_collection = relationship('Feature')

    center_point = Column(Geography(geometry_type='POINT', srid=4326))
    rotation = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "model_id": self.model_id,
            "project_id": self.project_id,
            "centerPoint": self.center_point,
            "rotation": self.rotation
        }

class Feature(Base):
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey("project.id"))
    model_id = Column(Integer, ForeignKey("model.id"))
    projectmodel_id = Column(Integer, ForeignKey("projectmodel.id"))

    properties = Column(String)
    type = Column(String)

    geometries = relationship('Geom')

class Geom(Base):
    __tablename__ = 'geom'
    id = Column(Integer, primary_key=True)

    feature_id = Column(Integer, ForeignKey("feature.id"))

    coordinates = Column(Geography(geometry_type='GEOMETRY', srid=4326))
