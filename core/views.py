from django.shortcuts import render, redirect
from .models import formulario
from django.contrib import messages
from django.contrib.auth import authenticate, login
#Create your views here.
def inicio(request):
    #return render(request, 'core/inicio.html')
    formularios = formulario.objects.all()  #Sentencia select * from Formulario;
    contexto = {"formularios": formularios} #usuario es el nombre del objeto formulario de la base de datos con el que podemos llamar en HTML 
    
    return render(request, 'core/inicio.html', contexto)

def registro(request):
    return render(request, 'core/registrarse.html')

#def inicio2(request):

def inicio_sesion(request):
    return render(request, 'core/inicio_sesion.html')

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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Iniciar sesión del usuario
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('inicio') # Redirigir a la página de inicio
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
    
    return render(request, 'login.html')