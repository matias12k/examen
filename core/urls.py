from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    # otras rutas de URL aquí
]