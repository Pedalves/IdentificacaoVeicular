from invoke import task
import os
import json

from gunicorn.app.base import Application

import iv.api


class IV(Application):
    def __init__(self):
        super().__init__(self)

    def init(self, parser, opts, args):
        self.load_config_from_module_name_or_filename('settings/config_gunicorn.py')

    def load(self):
        api = iv.api.create_app(gunicorn=True)
        return api

    @staticmethod
    def load_environment_variables():
        """
        Load environment variables defined in config.json
        """
        config_json = json.load(open('settings/config.json'))

        for key in config_json.keys():
            if key not in os.environ:
                os.environ[key] = config_json[key]


@task(default=True)
def run(context):
    """
    Start the Server with Gunicorn
    """

    # Hack to load environment variables when running Gunicorn locally
    if os.getenv('FLASK_CONFIG') is None:
        IV.load_environment_variables()
    app = iv.api.create_app()
    app.run(port=8046, debug=False)
