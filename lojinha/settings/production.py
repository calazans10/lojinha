# -*- coding: utf-8 -*-
import dj_database_url
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config()}
