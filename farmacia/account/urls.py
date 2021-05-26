from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    # Ruta para cerrar la sesión del usuario
    path("logout/", views.logout_view, name="logout"),
    
    # Ruta correspondiente al perfil del usuario
    path("profile/", views.profile, name="profile"),
    
    # Ruta para crear un nuevo usuario
    path("user_register/", views.user_register, name="user_register"),
    
    # Ruta para editar los datos de un usuario registrado
    path("edit_user_profile/", views.edit_user_profile, name="edit_user_profile"),
]