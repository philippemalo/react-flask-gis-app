import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from queries import resolve_users, resolve_userProjects, resolve_login, resolve_isConnected, resolve_logout
from mutations import resolve_createUser

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
        print(json.dumps(result, indent=2))
        return jsonify(result), status_code

    elif current_resolver == "userLogout":
        resolver_success = bool(result["data"][current_resolver]["success"])

        if resolver_success:
            # Need to check if cookie already exists. If so, refresh it.
            logged_in_user = result["data"][current_resolver]["user"]
            
            res = jsonify(result)
            res.set_cookie(key='react-flask-app', value='', expires=0)

            return res, status_code

        return jsonify(result), status_code

    else:
        return jsonify(result), status_code

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("isConnected", resolve_isConnected)
query.set_field("userLogin", resolve_login)
query.set_field("userLogout", resolve_logout)
query.set_field("users", resolve_users)
query.set_field("userProjects", resolve_userProjects)

mutation.set_field("createUser", resolve_createUser)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)