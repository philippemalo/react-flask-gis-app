from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType, ScalarType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from scalars import coordinates_serializer
from queries import resolve_users, resolve_userProjects, resolve_login, resolve_isConnected, resolve_logout, resolve_userModels, resolve_allModels
from mutations import resolve_createUser, resolve_createModel, resolve_createProject, resolve_deleteModel, resolve_deleteProject, resolve_createModelFeature

app = Flask(__name__)
CORS(app, supports_credentials=True, origins="http://localhost:3000")

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost:5432/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def get_db_connection():
    conn = psycopg2.connect(host='localhost', port='5432', dbname='db', user='user', password='pass')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    if conn.closed == 0:
        return 'DB connection succesful'
    else:
        return 'DB not connected'

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400

    current_resolver = list(result["data"].keys())[0]

    if current_resolver == "userLogin":
        resolver_success = bool(result["data"][current_resolver]["success"])

        if resolver_success:
            # Need to check if cookie already exists. If so, refresh it.
            logged_in_user = result["data"][current_resolver]["user"]
            
            token = jwt.encode({"user": {"id": logged_in_user['id'], "email": logged_in_user['email']}}, "secret", algorithm="HS256")
            res = jsonify(result)
            res.set_cookie(key='react-flask-app', value=token, max_age=60*60)

            return res, status_code

        return jsonify(result), status_code

    elif current_resolver == "createUser":
        resolver_success = bool(result["data"][current_resolver]["success"])

        if resolver_success:
            created_user = result["data"][current_resolver]["user"]
            
            token = jwt.encode({"user": {"id": created_user['id'], "email": created_user['email']}}, "secret", algorithm="HS256")
            res = jsonify(result)
            res.set_cookie(key='react-flask-app', value=token, max_age=60*60)

            return res, status_code

        return jsonify(result), status_code

    elif current_resolver == "isConnected":
        return jsonify(result), status_code

    elif current_resolver == "userLogout":
        resolver_success = bool(result["data"][current_resolver]["success"])

        if resolver_success:
            logged_in_user = result["data"][current_resolver]["user"]
            
            res = jsonify(result)
            res.set_cookie(key='react-flask-app', value='', expires=0)

            return res, status_code

        return jsonify(result), status_code

    else:
        return jsonify(result), status_code

coordinates_scalar = ScalarType("Coordinates")
coordinates_scalar.set_serializer(coordinates_serializer)

# json_scalar = ScalarType("JSON", json_serializer, json_value_parser, json_literal_parser)

query = QueryType()
mutation = MutationType()

userType = ObjectType("User")
@userType.field("models")
def resolver_userModels(obj, _):
    return obj["models"]
@userType.field("projects")
def resolver_userProjects(obj, _):
    return obj["projects"]

modelType = ObjectType("Model")
@modelType.field("featureCollection")
def resolve_modelFeatureCollection(obj, _):
    return obj["featureCollection"]

projectType = ObjectType("Project")
@projectType.field("featureCollection")
def resolve_projectFeatureCollection(obj, _):
    return obj["featureCollection"]
@projectType.field("models")
def resolve_projectModels(obj, _):
    return obj["models"]

projectModelType = ObjectType("ProjectModel")
@projectModelType.field("featureCollection")
def resolve_projectModelFeatureCollection(obj, _):
    return obj["featureCollection"]
@projectModelType.field("centerPoint")
def resolve_projectModelCenterPoint(obj, _):
    return obj["centerPoint"]

query.set_field("isConnected", resolve_isConnected)
query.set_field("userLogin", resolve_login)
query.set_field("userLogout", resolve_logout)
query.set_field("users", resolve_users)
query.set_field("userProjects", resolve_userProjects)
query.set_field("userModels", resolve_userModels)
query.set_field("allModels", resolve_allModels)

mutation.set_field("createUser", resolve_createUser)
mutation.set_field("createModel", resolve_createModel)
mutation.set_field("createProject", resolve_createProject)
mutation.set_field("deleteModel", resolve_deleteModel)
mutation.set_field("deleteProject", resolve_deleteProject)
mutation.set_field("createModelFeature", resolve_createModelFeature)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, coordinates_scalar, userType, modelType, projectType, projectModelType
)