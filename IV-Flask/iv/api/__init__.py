"""

Swagger docs at http://127.0.0.1:5000/docs/index.html

Application factory pattern http://flask.pocoo.org/docs/0.10/patterns/appfactories/

"""
import sys
import os
from flask import Flask
from flask import json
from flask_cors import CORS
from flask_restful_swagger_2 import Api
from werkzeug.exceptions import HTTPException

import iv


def create_app(gunicorn=False, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    iv.with_gunicorn = bool(gunicorn)

    # App instantiation
    app = Flask(__name__, static_folder='../../static', static_url_path='', **kwargs)

    # Setting CORS due to swagger-ui
    CORS(app)

    @app.route('/')
    def root():
        return app.send_static_file('index.html')

    # App configuration
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name:
        flask_config_name = 'local'
    else:
        flask_config_name = env_flask_config_name

    try:
        app.config.from_object('settings.local')
    except ImportError:
        print('ERROR!')
        sys.exit(1)

    # API instantiation
    api = Api(app, title=app.config['API_TITLE'], api_spec_url=app.config['API_SPEC_URL'])

    # this is important for dispatching resource methods decorators in the correct order
    from iv.api.resources import Vehicle

    api.add_resource(Vehicle, '/vehicle')

    @app.errorhandler(Exception)
    def handle_error(error):
        response = json.jsonify(dict(error=str(error)))
        response.status_code = 500
        if hasattr(error, "code"):
            response.status_code = error.code
        return response

    # for any http status code force json response
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, handle_error)

    return app
