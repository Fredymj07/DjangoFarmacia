from django.forms import ModelForm, widgets
from django import forms
from django.core.validators import EmailValidator
from proveedor.models import Proveedor
from .models import Categoria, Producto
from bootstrap_datepicker_plus import DatePickerInput
from django.core.files.images import get_image_dimensions

class AgregarProductoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', min_length=3, max_length=14)
    cantidad_disponible = forms.IntegerField(label='Stock')
    fecha_vencimiento = forms.DateField(label='Fecha de Vencimiento', widget=DatePickerInput(format='%Y-%m-%d'))
    categoria = forms.ModelChoiceField(label='Categoría', queryset=Categoria.objects.all())
    proveedor = forms.ModelChoiceField(label='Proveedor', queryset=Proveedor.objects.all())
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}), max_length=500)
    imagen = forms.ImageField(widget=forms.FileInput,)
    
    """ Este método permite establecer las dimensiones permitidas para la imagen """
    def clean_imagen(self):
        imagen = self.cleaned_data['imagen']
        
        # Obtención de las dimensiones de la imegen
        widht, height = get_image_dimensions(imagen)
        
        # Establecimiento de las dimenciones permitidas
        max_widht = max_height = 600
        
        # Validación de las dimesiones de la imagen
        if widht > max_widht or height > max_height:
            raise forms.ValidationError("El tamaño de la imagen no es válido. Recuerde que las dimensiones permitidas son %spx (alto) y %spx (ancho)"% (max_widht, max_height))
        
        # Validación de la extensión permitida
        img, ext = imagen.content_type.split('/')
        if not(img == 'image' and ext in ['jpeg', 'jpg', 'gif', 'png']):
            raise forms.ValidationError("Imagen no soportada, solamente soportamos: 'jpeg', 'jpg', 'gif', 'png'")
        
        # Validación del tamaño permitido
        if len(imagen) > (30 * 1024):
            raise forms.ValidationError("La imagen seleccionada supera el tamaño permitido. Por favor modifique el tamaño e intente nuevamente.")
        
        # Tamano de la imagen 1 KB equivale a 1024B
        if len(imagen) > (30 * 1024):
            raise forms.ValidationError("Imagen no puede superar los 30kb")
        
        return imagen
    
class ActualizarProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'cantidad_disponible', 'fecha_vencimiento', 'categoria', 'proveedor', 'descripcion', 'imagen',) 
        widgets = {
            'cantidad_disponible':widgets.NumberInput,
            # 'fecha_vencimiento':DatePickerInput(format='%d-%m-%Y'),
            'fecha_vencimiento':DatePickerInput ( 
                options = { 
                    "format" :  "YYYY-MM-DD" ,  # formato de fecha y hora de momento 
                    "showClose" :  True , 
                    "showClear" :  True , 
                    "showTodayButton" :  True , 
                } 
            ), 
            'categoria':widgets.Select(),
            'proveedor':widgets.Select(),
            'imagen':widgets.FileInput,
        }