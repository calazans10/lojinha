import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling


DJANGO_SETTINGS = os.environ.get('DJANGO_SETTINGS')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS)

application = Cling(get_wsgi_application())
