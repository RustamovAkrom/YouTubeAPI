import os
from datetime import timedelta


GRAPHQL_JWT = {
    'JWT_PAYLOAD_HANDLER': 'app.utils.jwt_payload',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_SECRET_KEY': os.getenv("SECRET_KEY"),
    'JWT_ALGORITHM': 'HS256',
}
