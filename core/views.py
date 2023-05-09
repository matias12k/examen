from django.shortcuts import render
from .models import formulario

#Create your views here.
def inicio(request):
    #return render(request, 'core/inicio.html')
    formularios = formulario.objects.all()  #Sentencia select * from Formulario;
    contexto = {"formularios": formularios} #usuario es el nombre del objeto formulario de la base de datos con el que podemos llamar en HTML 
    return render(request, 'core/inicio.html', contexto)

def registro(request):
    return render(request, 'core/registrarse.html')

#def inicio2(request):
    
