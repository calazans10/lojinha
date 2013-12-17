import os
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

POSTGRESPASSWORD = os.environ.get('POSTGRESPASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lojinha_db',
        'USER': 'postgres',
        'PASSWORD': POSTGRESPASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
