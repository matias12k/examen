from django.shortcuts import render

def inicio(request):
    return render(request, 'core/inicio.html')

def registro(request):
    return render(request, 'core/registrarse.html')
# Create your views here.
