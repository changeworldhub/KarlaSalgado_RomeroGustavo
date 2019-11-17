from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Voluntario(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=10)
    pais = models.CharField(max_length=30)

        
    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


    def get_absolute_url(self):
        return reverse('voluntario-detail', args=[str(self.id)])



