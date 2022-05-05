from pyclbr import Class
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Telefono {self.telefono}"


class Amigos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Telefono {self.telefono}"


class AmigosCoder(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Telefono {self.telefono}"


class Avatar(models.Model):
    # vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
