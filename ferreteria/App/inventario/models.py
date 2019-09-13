from django.db import models


# Create your models here.
class Impuesto(models.Model):
    nomImpuesto = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.nomImpuesto

class Unidad(models.Model):
    nomUnidad = models.CharField(max_length=20)

    def __str__(self):
        return self.nomUnidad

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True,default=55)
    descripcion = models.CharField(max_length=60,null=True)
    unidad = models.ForeignKey(Unidad, null=True, blank=True,on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    precio_costo = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    impuesto = models.ForeignKey(Impuesto, null=True, blank=True,on_delete=models.CASCADE)
    precio_venta_1 = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    precio_venta_2 = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    precio_venta_3 = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.descripcion

