from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField("Producto", max_length=50)
    descripcion = models.TextField("Descripcion")
    precio = models.DecimalField("Precio", max_digits=7, decimal_places=0)
    stock = models.PositiveIntegerField("stock", default=0)
    imagen = models.ImageField("Imagen", upload_to="productos/")

    def __str__(self):
        return self.nombre_producto
    