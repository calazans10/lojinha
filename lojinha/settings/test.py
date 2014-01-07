# -*- coding: utf-8 -*-
from .base import *

TEST_RUNNER = "redgreenunittest.django.runner.RedGreenDiscoverRunner"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'memory',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
