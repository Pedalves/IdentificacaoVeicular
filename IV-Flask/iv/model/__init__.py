"""Module with the super class of the models and shared functions.
"""
import json

from iv.utils.json_util import default_to_json


class Model:
    """Super class for all the models

    Attributes:
        DICT_COLUMN (dict): Dictionary used to translate a database dict to a
        model object
        IGNORE_COLUMN (list): Columns to be ignored from the database when
        converting to model
        IGNORE_FIELD (list): Fields to be ignored from the dict when
        converting to api

    """

    # TODO: check if this is correct? this is a class property, not instance
    DICT_COLUMN = dict()
    IGNORE_COLUMN = ()
    IGNORE_FIELDS = []

    def __repr__(self):
        return str(self.to_json())

    def __init__(self):
        self._ignore_fields = []

    def ignore_fields(self, *args):
        self._ignore_fields = self._ignore_fields + args
        return self

    def pick(self, keys):
        return {k: getattr(self, k) for k in keys if hasattr(self, k)}

    def to_json(self, zipped=False):
        """Transforms a model object in json

        Returns:
            str: JSON string representing the object
        """
        args = dict(default=default_to_json)
        if not zipped:
            args = dict(args, sort_keys=True, indent=4)

        return json.dumps(self, **args)

    def to_dict(self):
        return json.loads(self.to_json())

    @classmethod
    def to_object(cls, object_dict, **kwargs):
        """Transforms a model-like dict from the database in a model object

        Args:
            object_dict (dict): Description
            **kwargs (dict): Extra arguments needed to create the object

        Returns:
            Model: The model created using the dict and the kwargs


        """
        model_dict = dict()
        for key, db_key in cls.DICT_COLUMN.items():
            if db_key not in cls.IGNORE_COLUMN:
                model_dict[key] = object_dict[db_key]
        return cls(**model_dict, **kwargs)
