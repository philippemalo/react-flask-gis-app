from models import User, Project
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:pass@localhost:5432/db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def resolve_users(obj, info):
    try:
        result = session.query(User)

        users = []

        for user in result:
            users.append(user.to_dict())

        payload = {
            "success": True,
            "users": users
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_userProjects(obj, info, userId):
    try:
        result = session.query(Project).filter_by(user_id=userId)

        projects = []

        for project in result:
            projects.append(project.to_dict())

        payload = {
            "success": True,
            "users": projects
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload