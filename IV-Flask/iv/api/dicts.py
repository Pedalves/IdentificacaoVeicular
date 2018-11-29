
VEHICLE = {
    'tags': ['Vehicle'],
    'description': "Get the license plate of a given vehicle.",
    'consumes': ['image/jpeg'],
    'parameters': [
        {
            'name': 'vehicle_img',
            'description': 'Vehicle binary image.',
            'in': 'body',
            'type': 'image/jpeg',
            'required': True,
            'schema': {
                'type': 'string',
                'format': 'byte'

            }
        },
        {
            'name': 'debug',
            'description': 'debug',
            'in': 'query',
            'type': 'boolean',
            'default': False,
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': 'OK'
        }
    }

}