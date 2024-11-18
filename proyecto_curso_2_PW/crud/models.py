from django.db import models

# Create your models here.
class Dulce(models.Model):
    """
    Modelo que representa la estructura de datos de
    los postres de una dulcería en base de datos
    """
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=250)
    stock = models.IntegerField()
    vencimiento = models.DateTimeField()
    imagen = models.FileField(upload_to="dulces/")
    precioCompra = models.IntegerField()
    precioVenta = models.IntegerField()

    def __str__(self):
        return self.nombre
