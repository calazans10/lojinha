# -*- coding: utf-8 -*-
import os
import sys
from unipath import Path


BASE_DIR = Path(__file__).parent.parent

sys.path.append(BASE_DIR.child('apps'))

SECRET_KEY = os.environ.get('LOJINHASECRETKEY')

SERVE_MEDIA = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Jeferson Farias Calazans', 'calazans10@gmail.com'),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'model_utils',
    'metadata',
    'south',
    'mptt',

    'core',
    'clients',
    'products',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'lojinha.urls'

WSGI_APPLICATION = 'lojinha.wsgi.application'

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (BASE_DIR.child('static'),)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

GRAPPELLI_ADMIN_TITLE = 'Lojinha'
