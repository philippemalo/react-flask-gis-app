from api import engine
from models import User, Project, Feature
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import functions

# create session and bind engine
Session = sessionmaker(bind=engine)
session = Session()

# create User object
toto = User(email='toto@gmail.com', password='toto')
# add User object to session
session.add(toto)
# commit session changes
session.commit()
# query User table and print results
query1 = session.query(User)
for i in query1:
    print(i.to_dict())

# create Project object and assign user foreign key
newProject = Project(name='My beautiful park')
newProject.user_id = toto.id
# add Project object to session and commit
session.add(newProject)
session.commit()
query2 = session.query(Project)
for i in query2:
    print(i.to_dict())

# create Feature object and assign project foreign key
newFeature1 = Feature(type='POINT', geom='POINT(0 0)')
newFeature1.project_id = newProject.id
# add feature object to session and commit
session.add(newFeature1)
session.commit()
# create Feature object and assign project foreign key
newFeature2 = Feature(type='LINESTRING', geom='LINESTRING(0 0, 1 1)')
newFeature2.project_id = newProject.id
# add feature object to session and commit
session.add(newFeature2)
session.commit()
# create Feature object and assign project foreign key
newFeature3 = Feature(type='POINT', geom='POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))')
newFeature3.project_id = newProject.id
# add feature object to session and commit
session.add(newFeature3)
session.commit()

query3 = session.query(functions.ST_AsText(Feature.geom))
for i in query3:
    print(i)