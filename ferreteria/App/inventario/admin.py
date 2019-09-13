from django.contrib import admin
from App.inventario.models import Producto
from App.inventario.models import Impuesto
from App.inventario.models import Unidad


class productAdmin(admin.ModelAdmin):
    list_display=('codigo','descripcion','precio_costo','precio_venta_1','precio_venta_2','precio_venta_3')
    search_fields=(list_display)
    
class impuestoAdmin(admin.ModelAdmin):
    list_display=('id','nomImpuesto','valor')
        

# Register your models here.
admin.site.register(Producto,productAdmin)
admin.site.register(Impuesto,impuestoAdmin)
admin.site.register(Unidad)
