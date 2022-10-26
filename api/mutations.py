from flask import request
import jwt
from models import User, Model, Project, Feature, Geom
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import bcrypt
import json
import geojson
from shapely.geometry import shape

engine = create_engine("postgresql://user:pass@localhost:5432/db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def resolve_createUser(obj, info, email, password):
    try:
        check_email = bool(session.query(User).filter_by(email=email).first())
        
        if check_email:
            raise Exception('This email is already in use!')

        byte_pwd = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(byte_pwd, bcrypt.gensalt())

        new_user = User(email=email, password=hashed_password.decode('utf-8'))

        session.add(new_user)
        session.commit()

        # Make sure the new user is created before returning the payload
        created_user = session.query(User).filter_by(email=new_user.email).first()

        payload = {
            "success": True,
            "user": created_user.to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_createModel(obj, info, modelName, userId):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])
        
        new_model = Model(name=modelName)
        new_model.user_id = userId
        session.add(new_model)
        session.commit()

        created_model = session.query(Model).filter_by(id=new_model.id).first()

        payload = {
            "success": True,
            "model": created_model.to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_createProject(obj, info, projectName, userId):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])

        new_project = Project(name=projectName)
        new_project.user_id = userId
        session.add(new_project)
        session.commit()

        created_project = session.query(Project).filter_by(id=new_project.id).first()

        payload = {
            "success": True,
            "project": created_project.to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_deleteModel(obj, info, modelId, userId):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])

        model_to_delete: Model | None = session.query(Model).filter_by(id=modelId).first()

        if not model_to_delete:
            raise Exception('This model does not exist in the database')

        if int(model_to_delete.user_id) != int(userId):
            raise Exception('This model cannot be deleted by this user')

        session.delete(model_to_delete)
        session.commit()

        payload = {
            "success": True
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_deleteProject(obj, info, projectId, userId):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])
        
        project_to_delete: Project | None = session.query(Project).filter_by(id=projectId).first()
        
        if not project_to_delete:
            raise Exception('This project does not exist in the database')

        if int(project_to_delete.user_id) != int(userId):
            raise Exception('This project cannot be deleted by this user')

        session.delete(project_to_delete)
        session.commit()

        payload = {
            "success": True
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_createModelFeature(obj, info, modelId, geometry):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])

        newFeature = Feature(type='Feature', properties="{}")
        newFeature.model_id = modelId
        session.add(newFeature)
        session.commit()

        geom = {
            "coordinates": geometry["coordinates"],
            "type": geometry["type"]
        }

        geom_shapely = shape(geom)
        
        print('WKTTTTTTTTTTTTTTT: ', geom_shapely.wkt)
        newGeom = Geom(coordinates=geom_shapely.wkt)
        newGeom.feature_id = newFeature.id

        session.add(newGeom)
        session.commit()

        updatedModel = session.query(Model).filter_by(id=modelId).first()
        print('updatedModel: ', updatedModel)

        payload = {
            "success": True,
            "model": updatedModel.to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload