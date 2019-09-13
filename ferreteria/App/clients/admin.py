from django.contrib import admin
from App.clients.models import Cliente
from App.clients.models import facturaClient
from App.clients.models import typePago
from App.clients.models import pedidoCliente

class clientAdmin(admin.ModelAdmin):
    list_display=('nombres','ID')

# Register your models here.
admin.site.register(Cliente,clientAdmin)
admin.site.register(facturaClient)
admin.site.register(pedidoCliente)
admin.site.register(typePago)