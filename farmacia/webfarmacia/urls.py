from django.urls import path
from . import views

app_name='webfarmacia'
urlpatterns = [
    # Ruta principal de la aplicación creada en Django
    path('', views.index, name='indexFarmacia'),
]