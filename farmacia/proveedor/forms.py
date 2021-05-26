from django.forms import ModelForm, widgets
from django import forms
from django.core.validators import EmailValidator
from cliente.models import Ciudad, TipoDocumento
from .models import Proveedor

class AgregarProveedorForm(forms.Form):
    nombre = forms.CharField(label='Nombre', min_length=3, max_length=14)
    direccion = forms.CharField(label='Dirección', min_length=15, max_length=100)
    ciudad = forms.ModelChoiceField(label='Ciudad', queryset=Ciudad.objects.all())
    tipo_documento = forms.ModelChoiceField(label='Tipo de Documento', queryset=TipoDocumento.objects.all())
    numero_documento = forms.CharField(label='Número de Documento', min_length=3, max_length=14)
    telefono = forms.CharField(label='Teléfono', min_length=7, max_length=10)
    email = forms.CharField(label='Correo', max_length=100, validators=[EmailValidator(message='Correo inválido', whitelist='mail, gmail, outlook, hotmail, yahoo')])
    
class ActualizarProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre', 'direccion', 'ciudad', 'telefono', 'email',) 
        widgets = {
            'direccion': widgets.TextInput(),
            'ciudad': widgets.Select(),
            'telefono':widgets.NumberInput(),
            'email':widgets.EmailInput(attrs={'type': 'email'})
        }