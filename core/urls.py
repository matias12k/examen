from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('confirmacion', views.inicio, name='confirmacion'),
    path('inicio_sesion', views.inicio_sesion, name ='inicio_sesion'),
    path('login', views.pagina_juegos, name='login'),
    path('juegos', views.pagina_juegos, name='juegos'),
    path('api/', include('rest_api.urls')),
    #path('inicio2', views.inicio, name='inicio2'),
    # otras rutas de URL aquí
]