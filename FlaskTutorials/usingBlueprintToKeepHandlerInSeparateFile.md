Create : error_handlers.py

import flask
blueprint = flask.Blueprint('error_handlers', __name__)

@blueprint.app_errorhandler(404)
def handle404(e):
    return '404 handled'

app.py

import flask
import error_handlers

app = flask.Flask(__name__)
app.register_blueprint(error_handlers.blueprint)


