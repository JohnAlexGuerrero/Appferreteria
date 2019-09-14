from django.contrib import admin
from App.proveedor.models import Proveedor
from App.proveedor.models import facturaProveedor

#Register your models here.
admin.site.register(Proveedor)
admin.site.register(facturaProveedor)