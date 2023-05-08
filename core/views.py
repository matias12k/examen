from django.shortcuts import render
from .models import Formulario


# Create your views here.
#def inicio(request):
 #   return render(request, 'core/inicio.html')

def registro(request):
    return render(request, 'core/registrarse.html')

def inicio(request):
    formulario = Formulario.objects.all()  #Sentencia select * from Formulario;
    contexto = {"usuario": formulario} #usuario es el nombre del objeto formulario de la base de datos con el que podemos llamar en HTML 
    return render(request, 'core/inicio', contexto)
