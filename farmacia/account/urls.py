from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    # Ruta para agregar ccomentarios
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("user_register", views.user_register, name="user_register"),
]