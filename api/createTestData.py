from api import engine
from models import Point, Linestring, Polygon, Project, User, Model, ModelPoint, ModelLinestring, ModelPolygon, ProjectModel
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

# create Point object and assign project foreign key
newPoint = Point(geom='POINT(0 0)')
newPoint.project_id = newProject.id
# add Point object to session and commit
session.add(newPoint)
session.commit()
# create Linestring object and assign project foreign key
newLinestring = Linestring(geom='LINESTRING(0 0, 1 1)')
newLinestring.project_id = newProject.id
# add Linestring object to session and commit
session.add(newLinestring)
session.commit()
# create Polygon object and assign project foreign key
newPolygon = Polygon(geom='POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))')
newPolygon.project_id = newProject.id
# add Polygon object to session and commit
session.add(newPolygon)
session.commit()

query3 = session.query(functions.ST_AsText(Point.geom))
for i in query3:
    print(i)
query4 = session.query(functions.ST_AsText(Linestring.geom))
for i in query4:
    print(i)
query5 = session.query(functions.ST_AsText(Polygon.geom))
for i in query5:
    print(i)

# create Model object and assign user foreign key
newModel = Model(name='Park bench')
# add Model object to session and commit
session.add(newModel)
session.commit()
query6 = session.query(Model)
for i in query6:
    print(i.to_dict())

# create Point object and assign project foreign key
newModelPoint = ModelPoint(geom='POINT(3 3)')
newModelPoint.model_id = newModel.id
# add Point object to session and commit
session.add(newModelPoint)
session.commit()
# create Linestring object and assign project foreign key
newModelLinestring = ModelLinestring(geom='LINESTRING(1 1, 2 2)')
newModelLinestring.model_id = newModel.id
# add Linestring object to session and commit
session.add(newModelLinestring)
session.commit()
# create Polygon object and assign project foreign key
newModelPolygon = ModelPolygon(geom='POLYGON((0 0, 2 2, 0 4, 0 0))')
newModelPolygon.model_id = newModel.id
# add Polygon object to session and commit
session.add(newModelPolygon)
session.commit()

newProjectModelAssociation = ProjectModel(lat=0, lng=0, rotation=0)
newProjectModelAssociation.project_id = newProject.id
newProjectModelAssociation.model_id = newModel.id
session.add(newProjectModelAssociation)
session.commit()
