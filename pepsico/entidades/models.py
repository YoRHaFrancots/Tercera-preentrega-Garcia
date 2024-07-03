from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock  = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email  = models.EmailField()
    def __str__(self):
        return f"{self.nombre}"

class Pedido(models.Model):
    descripcion=models.CharField(max_length=500)
    direccion=models.CharField(max_length=100,)
    fechaEntrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
     return f"{self.direccion}"