from django.db import models

class Vinilo(models.Model):
    artista = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    precio = models.FloatField()
    def __str__(self):
        return f'Artista: {self.artista} - Álbum: {self.album} - Género: {self.genero} - Precio: ${self.precio}'

class Reproductor(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField()

class Parlante(models.Model):
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    potencia = models.CharField(max_length=50)
    precio = models.FloatField()