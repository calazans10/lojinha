from django.contrib import admin
from clients.models import Client, Address


class ClientAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Address, AddressAdmin)
