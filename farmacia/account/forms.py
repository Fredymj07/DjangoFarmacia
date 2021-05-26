from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django import forms
from django.forms import widgets

# Esta clase corresponde al formulario personalizado para la creación de un usuario
""" Esta clase permite agregar campos al formulario de creación de usuarios """
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres', min_length=3, max_length=50, error_messages={'Invalid':'El nombre ingresado no cumple con los parámetros necesarios.'})
    last_name = forms.CharField(label='Apellidos', min_length=4, max_length=70, error_messages={'Invalid':'El apellido no cumple con los parámetros necesarios.'})
    email = forms.EmailField(label='Email', max_length=50, help_text='Ingresa tu correo electrónico', error_messages={'Invalid':'La dirección de correo ingresada no es válida.'})
    
    """ Este método permite validar si un email ingresado ya se encuentra registrado en la base de datos """
    def clean_email(self):
        email_user = self.cleaned_data['email'].lower()
        user_data = User.objects.filter(email=email_user)
        if user_data.count():
            raise ValidationError('El email ingresado ya se encuentra registrado.')
        return email_user
    
    """ Este método permite validar si el nombre de usuario ingresado ya se encuentra registrado en la base de datos """
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        data = User.objects.filter(username=username)
        if data.count():
            raise  ValidationError("El usuario ingresado ya se encuentra registrado en la plataforma")
        return username
    
    """ Este método permite sobreescibir el método guardar, de acuerdo con el campo (email) agregado al formulario """
    def save(self, commit=True):
        user_data = User.objects.create_user(
            self.cleaned_data['username'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],            
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
        )
        return user_data
    
""" Esta clase permite agregar el avatar a un usuario """
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'user',)
        
    """ Este método permite sobreescribir el campo user para que sea oculto ante el usuario """
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].required = False
        self.fields['avatar'].widget.attrs['class'] = "custom-file-input"
        self.fields['avatar'].widget.attrs['id'] = "customFile"
        
    """ Este método permite establecer las dimensiones permitidas para la imagen """
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        
        # Obtención de las dimensiones de la imegen
        widht, height = get_image_dimensions(avatar)
        
        # Establecimiento de las dimenciones permitidas
        max_widht = max_height = 600
        
        # Validación de las dimesiones de la imagen
        if widht > max_widht or height > max_height:
            raise forms.ValidationError("El tamaño de la imagen no es válido. Recuerde que las dimensiones permitidas son %spx (alto) y %spx (ancho)"% (max_widht, max_height))
        
        # Validación de la extensión permitida
        img, ext = avatar.content_type.split('/')
        if not(img == 'image' and ext in ['jpeg', 'jpg', 'gif', 'png']):
            raise forms.ValidationError("Imagen no soportada, solamente soportamos: 'jpeg', 'jpg', 'gif', 'png'")
        
        # Validación del tamaño permitido
        if len(avatar) > (30 * 1024):
            raise forms.ValidationError("La imagen seleccionada supera el tamaño permitido. Por favor modifique el tamaño e intente nuevamente.")
        
        # Tamano de la imagen 1 KB equivale a 1024B
        if len(avatar) > (30 * 1024):
            raise forms.ValidationError("Imagen no puede superar los 30kb")
        
        return avatar
    
""" Esta clase permite editar los valores que se encuentran registrados en el perfil de un usuario """
class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)