from django.contrib import admin
from App.inventario.models import Producto
from App.inventario.models import Impuesto
from App.inventario.models import Unidad

# Register your models here.
admin.site.register(Producto)
admin.site.register(Impuesto)
admin.site.register(Unidad)