from api import engine
from models import Project, User, Model, ProjectModel, Feature, Geom
from sqlalchemy import inspect

# Table deletion order matters because of relationships and the use of foreign keys
if inspect(engine).has_table('geom'):
    Geom.__table__.drop(engine)

if inspect(engine).has_table('feature'):
    Feature.__table__.drop(engine)

if inspect(engine).has_table('projectmodel'):
    ProjectModel.__table__.drop(engine)

if inspect(engine).has_table('model'):
    Model.__table__.drop(engine)

if inspect(engine).has_table('project'):
    Project.__table__.drop(engine)

if inspect(engine).has_table('user'):
    User.__table__.drop(engine)