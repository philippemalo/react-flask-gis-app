from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import time
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from queries import resolve_users, resolve_userProjects, resolve_projectFeatures

app = Flask(__name__)

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

@app.route('/api/time')
def current_time():
    return {'time': time.time()}

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
    return jsonify(result), status_code

query = ObjectType("Query")

query.set_field("users", resolve_users)
query.set_field("userProjects", resolve_userProjects)
query.set_field("projectFeatures", resolve_projectFeatures)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)