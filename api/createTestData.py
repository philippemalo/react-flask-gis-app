import bcrypt
from api import engine
from models import User, Project, Model, ProjectModel, Feature, Geom
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import functions

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

newGeomForFeature = Geom(coordinates='POINT(1 1)')
newGeomForFeature.feature_id = newModelFeature.id
session.add(newGeomForFeature)
query8 = session.query(Geom)
for i in query8:
    print(i)
# newProjectModelAssociation = ProjectModel(center_point='POINT(0 0)', rotation=0)
# newProjectModelAssociation.project_id = newProject.id
# newProjectModelAssociation.model_id = newModel.id
# session.add(newProjectModelAssociation)
# session.commit()


