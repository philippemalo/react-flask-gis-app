import time
from flask import Flask
from flask_graphql import GraphQLView

from flask_sqlalchemy.models import db_session
from flask_sqlalchemy.schema import schema, Shape

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return "Hello world from Flask!"


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
