from django.shortcuts import render

# Create your views here.
""" Este método permite visualizar la página principal de la farmacia """
def index(request):
    
    return render(request, 'index.html')