from django.forms import ModelForm, widgets
from django import forms
from django.core.validators import EmailValidator
from .models import Cliente, Sexo, TipoDocumento, Ciudad

class AgregarClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', min_length=3, max_length=14)
    apellido = forms.CharField(label='Apellido', min_length=3, max_length=14)
    direccion = forms.CharField(label='Dirección', min_length=15, max_length=100)
    sexo = forms.ModelChoiceField(label='Sexo', queryset=Sexo.objects.all())
    ciudad = forms.ModelChoiceField(label='Ciudad', queryset=Ciudad.objects.all())
    tipo_documento = forms.ModelChoiceField(label='Tipo de Documento', queryset=TipoDocumento.objects.all())
    numero_documento = forms.CharField(label='Número de Documento', min_length=3, max_length=10)
    telefono = forms.CharField(label='Teléfono', min_length=7, max_length=10)
    email = forms.CharField(label='Correo', validators=[EmailValidator(message='Correo inválido', whitelist='mail, gmail, outlook, hotmail, yahoo')])
    
class ActualizarClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'direccion', 'sexo', 'ciudad', 'telefono', 'email',) 
        widgets = {
            'direccion': widgets.TextInput(),
            'ciudad': widgets.Select(),
            'telefono':widgets.NumberInput(),
            'email':widgets.EmailInput(attrs={'type': 'email'})
        }