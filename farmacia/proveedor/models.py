from django.db import models
from django.db.models.deletion import PROTECT
from cliente.models import Ciudad, TipoDocumento

# Create your models here.
class Proveedor(models.Model):    
    nombre = models.CharField(max_length=255, null=False)
    direccion = models.CharField(max_length=255, null=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=20, null=False)
    telefono =  models.CharField(max_length=14, null=False)
    email =  models.CharField(max_length=50, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre