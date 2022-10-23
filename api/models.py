from enum import Enum
from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String, Float
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from shapely import wkb
from shapely.geometry import mapping
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
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    feature_collection = relationship('Feature')

    name = Column(String)

    def to_dict(self):
        features = []

        for i in self.feature_collection:
            features.append(i.to_dict())
        
        # print('FEATURES: ', features)

        return {
            "id": self.id,
            "name": self.name,
            "featureCollection": features
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
    
    # There is probably a better check constraint to make sure that atleast one foreign key is set
    __table_args__ = (
        CheckConstraint('project_id + model_id + projectmodel_id > 0'),
    )

    properties = Column(String)
    type = Column(String)

    geometry = relationship('Geom', back_populates='feature', uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "geometry": self.geometry.to_dict(),
            "properties": self.properties,
            "type": self.type
        }

class Geom(Base):
    __tablename__ = 'geom'
    id = Column(Integer, primary_key=True)

    feature_id = Column(Integer, ForeignKey("feature.id"), nullable=False)

    coordinates = Column(Geography(geometry_type='GEOMETRY', srid=4326))

    feature = relationship('Feature', back_populates='geometry')

    def wkb_to_geojson(self):
        return mapping(wkb.loads(str(self.coordinates), True))

    def to_dict(self):
        geom = self.wkb_to_geojson()

        if geom["type"] == 'Point':
            geom["coordinates"] = [list(geom["coordinates"])]
        else:
            geom["coordinates"] = list(geom["coordinates"])

        return {
            "id": self.id,
            "type": geom["type"].upper(),
            "coordinates": geom["coordinates"]
        }
