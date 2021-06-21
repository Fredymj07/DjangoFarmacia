import os
from django.shortcuts import redirect, render, reverse
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as make_login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomUserCreationForm, UserProfileForm, EditUserProfileForm
from .models import UserProfile


# Create your views here.
""" Este método permite cerrar la sesión del usuario una vez ha hecho login """
def logout_view(request):
    logout(request)
    return redirect('webfarmacia:index')

""" Este método permite cargar los datos del usuario y actualizar el avatar del perfil """
@login_required
def profile(request):
    formUserProfile = UserProfileForm()    
    if request.method == 'POST':
        pathOldAvatar = None
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            formUserProfile = UserProfileForm(request.POST, request.FILES, instance=userprofile)
            # La variable pathOldUserAvatar se utiliza para concatenar la ruta real del avatar que se encuentra creado
            pathOldAvatar = os.path.join(settings.MEDIA_ROOT, userprofile.avatar.name)
            
        except ObjectDoesNotExist:
            formUserProfile = UserProfileForm(request.POST, request.FILES)
        
        if formUserProfile.is_valid():
            if pathOldAvatar is not None and os.path.isfile(pathOldAvatar):
                os.remove(pathOldAvatar)
                
            userprofile = formUserProfile.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
    return render(request, 'profile.html', {'formUserProfile':formUserProfile})

""" Este método permite crear un nuevo usuario dentro de la aplicación """
def user_register(request):
    userRegistrationForm = CustomUserCreationForm()
    if request.method == 'POST':
        userRegistrationForm = CustomUserCreationForm(request.POST)
        if userRegistrationForm.is_valid():
            user = userRegistrationForm.save()
            if user is not None:
                make_login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
                return redirect(reverse('webfarmacia:indexFarmacia'))            
    else:
        userRegistrationForm = CustomUserCreationForm()
    return render(request, 'user_register.html', {'userRegistrationForm':userRegistrationForm})

""" Este método permite editar los datos de un usuario registrado en la aplicación """
def edit_user_profile(request):
    if request.method == "POST":
        formEditUserProfile = EditUserProfileForm(request.POST, instance=request.user)
        if formEditUserProfile.is_valid():
            formEditUserProfile.save()
    else:
        formEditUserProfile = EditUserProfileForm(instance=request.user)        
        
    return render(request, 'profile.html', {'formEditUserProfile':formEditUserProfile})