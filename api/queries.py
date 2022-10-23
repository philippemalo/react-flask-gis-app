import bcrypt
import jwt
from models import User, Project, Model
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import request

engine = create_engine("postgresql://user:pass@localhost:5432/db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def resolve_isConnected(obj, info):
    try:
        token = request.cookies.get('react-flask-app')

        if token is None:
            raise Exception('User is not logged in')

        decoded_jwt = jwt.decode(token, "secret", algorithms=["HS256"])
        connected_user = session.query(User).filter_by(email=decoded_jwt['user']['email'])

        payload = {
            "success": True,
            "user": connected_user.first().to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_login(obj, info, email, password):
    try:
        user = session.query(User).filter_by(email=email)
        check = bcrypt.checkpw(password.encode('utf-8'), user.first().password.encode('utf-8'))
        if not check:
            raise Exception('Wrong password!')

        payload = {
            "success": True,
            "user": user.first().to_dict()
        }
        
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def resolve_logout(obj, info):
    try:
        token = request.cookies.get('react-flask-app')

        if token is None:
            raise Exception('User is not logged in')
            
        decoded_jwt = jwt.decode(token, "secret", algorithms=["HS256"])
        connected_user = session.query(User).filter_by(email=decoded_jwt['user']['email'])

        payload = {
            "success": True,
            "user": connected_user.first().to_dict()
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

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
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])

        result = session.query(Project).filter_by(user_id = userId)
        projects = []

        for project in result:
            projects.append(project.to_dict())

        payload = {
            "success": True,
            "projects": projects
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload

def resolve_userModels(obj, info, userId):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])

        result = session.query(Model).filter_by(user_id = userId)
        models = []

        for model in result:
            models.append(model.to_dict())

        print(type(models[0]["featureCollection"][0]["geometry"]))
        payload = {
            "success": True,
            "models": models
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    print('PAYLOAD: ', payload)
    return payload

def resolve_allModels(obj, info):
    try:
        token = request.cookies.get('react-flask-app')
        if token is None:
            raise Exception('User is not logged in')
        jwt.decode(token, "secret", algorithms=["HS256"])
        
        result = session.query(Model)
        models = []

        for model in result:
            models.append(model.to_dict())

        payload = {
            "success": True,
            "models": models
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload

# def resolve_projectFeatures(obj, info, projectId):
#     try:
#         print('bleh')
#         # result = session.query(Feature.id, Feature.type, functions.ST_AsGeoJSON(Feature.geom).label('geojson')).filter_by(project_id = projectId)
#         # features = []
    
#         # for feature in result:
#         #     print('feature: ', feature)
#         #     print('type: ', type(feature.geojson))
#         #     geojson = json.loads(feature.geojson)
            
#         #     print('COOOOOOOORDS: ', geojson['coordinates'])
#         #     features.append({"id": feature.id, "type": feature.type, "coordinates": geojson['coordinates']})

#         # payload = {
#         #     "success": True,
#         #     "features": features
#         # }

#         # --- graphql return type ---
#         # type Feature {
#         #     id: ID!
#         #     type: GeometryType!
#         #     geom: [Coordinates!]!
#         # }

#         # type Coordinates {
#         #     latitude: Float!
#         #     longitude: Float!
#         # }

#     except Exception as error:
#         payload = {
#             "success": False,
#             "errors": [str(error)]
#         }
    
#     return payload