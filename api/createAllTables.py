from models import Project, User, Model, ProjectModel, Feature, Geom
from api import engine
from sqlalchemy import inspect

# Table creation order matters because of relationships and the use of foreign keys
if not inspect(engine).has_table('user'):
    User.__table__.create(engine)

if not inspect(engine).has_table('project'):
    Project.__table__.create(engine)

if not inspect(engine).has_table('model'):
    Model.__table__.create(engine)

if not inspect(engine).has_table('projectmodel'):
    ProjectModel.__table__.create(engine)

if not inspect(engine).has_table('feature'):
    Feature.__table__.create(engine)

if not inspect(engine).has_table('geom'):
    Geom.__table__.create(engine)
