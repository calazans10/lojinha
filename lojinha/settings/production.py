import dj_database_url
from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config()}
