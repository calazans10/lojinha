from django.conf.urls import patterns, include, url
from clients.models import Client
from rest_framework import viewsets, routers

# from django.contrib import admin
# admin.autodiscover()


class ClientViewSet(viewsets.ModelViewSet):
    model = Client


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # url(r'^admin/', include(admin.site.urls)),
)
