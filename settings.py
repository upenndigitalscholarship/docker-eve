MONGO_HOST = "db"
MONGO_PORT = 27017
MONGO_DBNAME = "eve"

DOMAIN = {
    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
            }
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST']
