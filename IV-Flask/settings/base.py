import os

from iv.utils.json_util import default_to_json

DEBUG = False
TESTING = False
PROPAGATE_EXCEPTIONS = True
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
API_SPEC_URL = '/specification'
API_TITLE = 'IV API'
RESTFUL_JSON = {'sort_keys': True, 'indent': 4, 'default': default_to_json}
AWS_PROFILE = None
