import bcrypt
from api import engine
from models import User, Project, Model, ProjectModel, Feature, Geom
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape

# create session and bind engine
Session = sessionmaker(bind=engine)
session = Session()

# create User object
password = 'toto'
byte_pwd = password.encode('utf-8')
hashed_password = bcrypt.hashpw(byte_pwd, bcrypt.gensalt())
toto = User(email='toto@gmail.com', password=hashed_password.decode('utf-8'))
# add User object to session
session.add(toto)
# commit session changes
session.commit()
# query User table and print results
query1 = session.query(User).filter_by(email='toto@gmail.com').first()
print(query1.to_dict())

# create Project object and assign user foreign key
newProject = Project(name='My beautiful park')
newProject.user_id = toto.id
# add Project object to session and commit
session.add(newProject)
session.commit()
query2 = session.query(Project)
for i in query2:
    print(i.to_dict())

# create Model object and assign user foreign key
newModel = Model(name='Park bench')
newModel.user_id = toto.id
# add Model object to session and commit
session.add(newModel)
session.commit()
query6 = session.query(Model)
for i in query6:
    print(i.to_dict())

newModelFeature = Feature(type='Feature', properties="{}")
newModelFeature.model_id = newModel.id
session.add(newModelFeature)
session.commit()
query7 = session.query(Feature)
for i in query7:
    print(i)

newGeomForFeature1 = Geom(coordinates='POINT(1 1)')
newGeomForFeature1.feature_id = newModelFeature.id
session.add(newGeomForFeature1)
session.commit()

query8 = session.query(Geom)
for i in query8:
    print(i)

# When creating a projectModel, I need to copy an existing model's featureCollection
# and linking those features to the projectModel
modelId_to_duplicate = 1
model_to_duplicate = session.query(Model).filter_by(id=modelId_to_duplicate).first()
# Set center point of copied model and a rotation if required
newProjectModel = ProjectModel(center_point='POINT(-70 45)', rotation=45.5)
newProjectModel.project_id = newProject.id
session.add(newProjectModel)
session.commit()
# Duplicate features
newFeatures = Feature(type='Feature', properties="{}")
newFeatures.projectmodel_id = newProjectModel.id
session.add(newFeatures)
session.commit()
print('REEEEEE: ', model_to_duplicate.feature_collection[0])
createdFeatures = session.query(Feature).filter_by(id=newFeatures.id).first()
for feature in model_to_duplicate.feature_collection:
    print('FEATUREEE: ', to_shape(feature.geometry.coordinates).wkt)
    newFeaturesGeom = Geom(coordinates=to_shape(feature.geometry.coordinates).wkt)
    print('BRUH: ', createdFeatures.id)
    newFeaturesGeom.feature_id = createdFeatures.id
    session.add(newFeaturesGeom)
    session.commit()
    
# session.add(newProjectModel, newFeatures, newFeaturesGeom)
# session.commit()

