from django.db import models
from App.inventario.models import Producto

# Create your models here.
class typePago(models.Model):
    idtp = models.IntegerField(default=20)
    nomtypepago = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nomtypepago


class Cliente(models.Model):
    idclie = models.IntegerField(default=10)
    nombres = models.CharField(max_length=40,blank=True)
    ID = models.IntegerField(blank=True)
    direccion =models.CharField(max_length=50,blank=True)
    telefono = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.nombres

class pedidoCliente(models.Model):
    product = models.ForeignKey(Producto, null=True,blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product

class facturaClient(models.Model):
    factura = models.IntegerField()
    fecha = models.DateField()
    formaPago = models.ForeignKey(typePago,null=True, blank=True,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,null=True, blank=True,on_delete=models.CASCADE)
    pedido = models.ManyToManyField(pedidoCliente)
