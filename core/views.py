from django.shortcuts import render, redirect
from .models import formulario
from django.contrib import messages
import requests
from django.shortcuts import render


#Create your views here.
def inicio(request):
    #return render(request, 'core/inicio.html')
    formularios = formulario.objects.all()  #Sentencia select * from Formulario;
    contexto = {"formularios": formularios} #usuario es el nombre del objeto formulario de la base de datos con el que podemos llamar en HTML 
    
    return render(request, 'core/inicio.html', contexto)

def registro(request):
    return render(request, 'core/registrarse.html')

#def inicio2(request):
    
def registrarse(request):
    if request.method == 'POST':
        # Si el formulario ha sido enviado
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        password = request.POST.get('password')
        # Crea un objeto formulario con los datos del formulario
        form = formulario(nombre=nombre, apellido=apellido, email=email, telefono=telefono, password=password)
        # Guarda el objeto en la base de datos
        form.save()
        # Redirecciona a una página de confirmación
        messages.success(request, 'El usuario nuevo se ha guardado!!!')
        return redirect('confirmacion')
    else:
        # Si el formulario no ha sido enviado, muestra el formulario vacío
        messages.success(request, 'El usuario nuevo no se a guardado!!!')
        return render(request, 'core/registro.html')
    
from django.shortcuts import render

def confirmacion(request):
    return render(request, 'core/inicio.html')

def iniciarsesion(request):
    return render(request, 'core/inicio_sesion.html')


#api externa con la hora
def get_current_time():
    url = 'http://worldtimeapi.org/api/timezone/America/Santiago'
    response = requests.get(url)
    data = response.json()
    current_time = data['datetime']
    return current_time

def show_time(request):
    current_time = get_current_time()
    return render(request,'core/time.html',{'current_time': current_time})

def hora(request):
    return render(request, 'core/time.html')

def matias(request):
    return render(request, 'core/matias.html')