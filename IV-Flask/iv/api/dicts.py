
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
        }
    ],
    'responses': {
        '201': {
            'description': 'OK'
        }
    }

}