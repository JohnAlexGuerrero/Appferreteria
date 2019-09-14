from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idproveedor = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=20)
    vendedor = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.empresa

class facturaProveedor(models.Model):
    factura = models.CharField(max_length=20, primary_key=True)
    empresa = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    vence = models.DateField()
