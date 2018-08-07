from settings.base import *

DEBUG = True
os.environ['GUNICORN_N_WORKERS'] = "1"
