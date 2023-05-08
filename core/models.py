from django.db import models

class formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=50)
# Create your models here.
