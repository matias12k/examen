from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('confirmacion', views.inicio, name='confirmacion'),
    path('inicio_sesion', views.inicio_sesion, name ='inicio_sesion'),
    #path('inicio2', views.inicio, name='inicio2'),
    # otras rutas de URL aquí
]