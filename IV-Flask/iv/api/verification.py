import webargs


FIELD_CONSTRUCTOR = dict(integer=webargs.fields.Int,
                         double=webargs.fields.Float,
                         number=webargs.fields.Number,
                         string=webargs.fields.String,
                         boolean=webargs.fields.Boolean
                         )
FIELD_CONSTRUCTOR['image/jpeg'] = webargs.fields.Raw


def create_args(swagger_dict):
    parameters = swagger_dict["parameters"]
    return_dict = dict()
    for parameter in parameters:
        if parameter["in"] == "query":
            constructor = FIELD_CONSTRUCTOR[parameter["type"]]
            args = dict(validate=[])
            args["required"] = False
            keys = parameter.keys()
            if "required" in keys and parameter["required"]:
                args["required"] = True

            return_dict[parameter["name"]] = constructor(**args)

    return return_dict