from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def ramos(request):
    return render(request, 'app/ramos.html')

def perfil(request):
    return render(request, 'app/perfil.html')