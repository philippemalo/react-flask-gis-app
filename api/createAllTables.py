from models import Feature, Project, User
from api import engine

User.__table__.create(engine)
Project.__table__.create(engine)
Feature.__table__.create(engine)
