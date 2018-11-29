from flask import request
from flask_restful_swagger_2 import swagger, Resource
from webargs.flaskparser import use_args

from iv.api import dicts
from iv.api.verification import create_args
from iv.controller import vehicle


class Vehicle(Resource):
    post = dicts.VEHICLE

    @swagger.doc(post)
    @use_args(create_args(post))
    def post(self, args):
        """
        Get a license plate for a given vehicle
        """

        return vehicle.get_lincese_plate(request.data, **args)

