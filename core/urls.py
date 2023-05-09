from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    #path('inicio2', views.inicio, name='inicio2'),
    # otras rutas de URL aquí
]