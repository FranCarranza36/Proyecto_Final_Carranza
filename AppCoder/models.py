from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    edad = models.IntegerField()
    def __str__(self):
        return f'Futbolista {self.apellido} {self.nombre} , Edad: {self.edad}'

class Basquetbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    triples = models.IntegerField()
    def __str__(self):
        return f'Basquetbolista {self.apellido} {self.nombre}, Triples: {self.triples}'
    
class Tenista(models.Model):
    nombre =models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    titulos = models.IntegerField()
    def __str__(self):
        return f'Tenista {self.apellido} {self.nombre}, Títulos: {self.titulos}'
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to= 'avatares', null= True, blank= True)
    def __str__(self):
         return f'{self.user}'
