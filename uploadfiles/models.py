from django.db import models
# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombres')
    paterno = models.CharField(max_length=64, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=64, verbose_name='Apellido Materno')

    def __str__(self):
        return '%s' % self.nombre + '%s' % self.paterno
