from api import engine
from models import Feature, Project, User

Feature.__table__.drop(engine)
Project.__table__.drop(engine)
User.__table__.drop(engine)