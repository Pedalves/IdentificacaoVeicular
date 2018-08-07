import decimal
import json

import datetime


class JsonEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        super(JsonEncoder, self).__init__(**kwargs)

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime.datetime):
            serial = o.isoformat()
            return serial
        if isinstance(o, bytes):
            return o.decode(encoding='utf8')
        return super(JsonEncoder, self).default(o)


def default_to_json(object_to_convert):
    """Default function to convert an object to json

    Args:
        object_to_convert (object): Object to be converted to json

    Returns:
        object: Representation of o to be used on the conversion
    """
    if hasattr(object_to_convert, "__dict__"):
        json_dict = {k: v for k, v in object_to_convert.__dict__.items() if k[0] != "_"}
        if hasattr(object_to_convert, 'IGNORE_FIELDS'):
            json_dict = {k: v for k, v in json_dict.items() if k not in object_to_convert.IGNORE_FIELDS}
        return json_dict
    else:
        return str(object_to_convert)
