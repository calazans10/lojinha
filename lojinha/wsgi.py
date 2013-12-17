import os


DJANGO_SETTINGS = os.environ.get('DJANGO_SETTINGS')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS)

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# application = get_wsgi_application()
application = Cling(get_wsgi_application())
