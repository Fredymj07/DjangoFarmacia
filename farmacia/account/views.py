import os
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as make_login
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomerUserCreationForm, UserProfileForm
from .models import UserProfile
from django.contrib import messages

# Create your views here.
""" Este método permite cerrar la sesión del usuario una vez ha hecho login """
def logout_view(request):
    logout(request)
    return redirect('wefarmacia:index')

""" Este método permite cargar los datos del usuario que se encuentra logueado en la aplicación """
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
    userRegistrationForm = CustomerUserCreationForm()
    if request.method == 'POST':
        userRegistrationForm = CustomerUserCreationForm(request.POST)
        if userRegistrationForm.is_valid():
            user = userRegistrationForm.save()
            if user is not None:
                make_login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
                return redirect(reverse('webfarmacia:indexFarmacia'))            
    else:
        userRegistrationForm = CustomerUserCreationForm()
    return render(request, 'user_register.html', {'userRegistrationForm':userRegistrationForm})