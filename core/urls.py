from django.urls import path
from . import views
from .views import show_time


urlpatterns = [
    path('', views.matias, name='matias'),
    path('registro', views.registro, name='registro'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('confirmacion', views.inicio, name='confirmacion'),
    path('iniciarsesion', views.iniciarsesion, name='iniciarsesion'),
    path('time/', show_time, name='show_time'),
    path('hora', show_time, name='hora'),
    path('inicio', views.inicio, name='inicio'),




    
    #path('inicio2', views.inicio, name='inicio2'),
    # otras rutas de URL aquí
]