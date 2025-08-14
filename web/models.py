from django.db import models
import uuid

# Create your models here.

class Producto(models.Model):
    id_producto = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_producto = models.CharField("Producto", max_length=50)
    descripcion = models.TextField("Descripcion")
    precio = models.DecimalField("Precio", max_digits=7, decimal_places=0)
    stock = models.PositiveIntegerField("stock", default=0)
    imagen = models.ImageField("Imagen", upload_to="productos/")
    slug = models.SlugField(default="", null=False, blank=False)
    is_private = models.BooleanField(default=False) #corresponde a productos premium o no

    def __str__(self):
        return self.nombre_producto
    