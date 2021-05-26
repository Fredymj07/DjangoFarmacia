from django.db import models
from cliente.models import Sexo, Ciudad, TipoDocumento
from django.db.models.deletion import PROTECT

# Create your models here.
class Empleado(models.Model):    
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    direccion = models.CharField(max_length=255, null=False)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=20, null=False)
    telefono =  models.CharField(max_length=14, null=False)
    email =  models.CharField(max_length=20, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido