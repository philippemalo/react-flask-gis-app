from api import engine
from models import Point, Linestring, Polygon, Project, User, Model, ModelPoint, ModelLinestring, ModelPolygon, ProjectModel
from sqlalchemy import inspect, text

if inspect(engine).has_table('projectmodel'):
    ProjectModel.__table__.drop(engine)
    
if inspect(engine).has_table('point'):
    Point.__table__.drop(engine)

if inspect(engine).has_table('linestring'):
    Linestring.__table__.drop(engine)

if inspect(engine).has_table('polygon'):
    Polygon.__table__.drop(engine)

if inspect(engine).has_table('project'):
    Project.__table__.drop(engine)

if inspect(engine).has_table('modelpoint'):
    ModelPoint.__table__.drop(engine)

if inspect(engine).has_table('modellinestring'):
    ModelLinestring.__table__.drop(engine)

if inspect(engine).has_table('modelpolygon'):
    ModelPolygon.__table__.drop(engine)

if inspect(engine).has_table('model'):
    Model.__table__.drop(engine)

if inspect(engine).has_table('user'):
    User.__table__.drop(engine)