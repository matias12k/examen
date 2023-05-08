from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
