# -*- coding: utf-8 -*-
import os
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

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

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
