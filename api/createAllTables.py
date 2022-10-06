from models import Point, Linestring, Polygon, Project, User, Model, ModelPoint, ModelLinestring, ModelPolygon, ProjectModel
from api import engine
from sqlalchemy import inspect

# Table creation order matters because of relationships and the use of foreign keys
if not inspect(engine).has_table('user'):
    User.__table__.create(engine)

if not inspect(engine).has_table('project'):
    Project.__table__.create(engine)

if not inspect(engine).has_table('point'):
    Point.__table__.create(engine)

if not inspect(engine).has_table('linestring'):
    Linestring.__table__.create(engine)

if not inspect(engine).has_table('polygon'):
    Polygon.__table__.create(engine)

if not inspect(engine).has_table('model'):
    Model.__table__.create(engine)

if not inspect(engine).has_table('modelpoint'):
    ModelPoint.__table__.create(engine)

if not inspect(engine).has_table('modellinestring'):
    ModelLinestring.__table__.create(engine)

if not inspect(engine).has_table('modelpolygon'):
    ModelPolygon.__table__.create(engine)

if not inspect(engine).has_table('projectmodel'):
    ProjectModel.__table__.create(engine)
