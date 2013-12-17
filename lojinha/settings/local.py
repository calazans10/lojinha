# -*- coding: utf-8 -*-
import os
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

POSTGRESPASSWORD = os.environ.get('POSTGRESPASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lojinha_db',
    }
}
