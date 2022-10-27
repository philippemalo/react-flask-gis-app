from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String, Float
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from shapely import wkb
from shapely.geometry import mapping, shape

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
        models = []
        for i in self.models:
            models.append(i.to_dict())

        features = []
        for i in self.feature_collection:
            features.append(i.to_dict())

        return {
            "id": self.id,
            "name": self.name,
            "models": models,
            "featureCollection": features
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

        return {
            "id": self.id,
            "name": self.name,
            "featureCollection": features
        }

class ProjectModel(Base):
    __tablename__ = 'projectmodel'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)

    feature_collection = relationship('Feature')

    center_point = Column(Geography(geometry_type='POINT', srid=4326))
    rotation = Column(Float)

    def wkb_to_geojson(self):
        dataShape = shape(wkb.loads(str(self.center_point), True))
        geojson = mapping(dataShape)
        return geojson

    def to_dict(self):
        geom = self.wkb_to_geojson()
        features = []

        for i in self.feature_collection:
            features.append(i.to_dict())
            
        return {
            "id": self.id,
            "featureCollection": features,
            "centerPoint": geom["coordinates"],
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
        if not self.geometry:
            raise Exception('The feature with id: '+str(self.id)+' is not tied to a geom... it should be deleted')
        geometry = self.geometry.to_dict()
        return {
            "id": self.id,
            "geometry": geometry,
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
        dataShape = shape(wkb.loads(str(self.coordinates), True))
        geojson = mapping(dataShape)
        return geojson

    def to_dict(self):
        geom = self.wkb_to_geojson()
        geomType = geom["type"]
        return {
            "id": self.id,
            "type": geomType,
            "coordinates": geom["coordinates"]
        }
