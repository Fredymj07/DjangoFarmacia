from django.db import models
from proveedor.models import Proveedor
from django.db.models.deletion import PROTECT

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    cantidad_disponible = models.IntegerField(null=False)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='imagen_producto', null=True)