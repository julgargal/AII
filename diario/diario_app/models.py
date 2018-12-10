from django.db import models

# Create your models here.

class Diario(models.Model):
    nombre=
    pais=
    idioma=
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre_usuario=
    passwd=
    email=
    nombre=
    apellidos=
    def __str__(self):
        return self.nombre_usuario

class Tipo(models.Model):
    tipo_noticia = models.CharField(max_length=80, primary_key=True, verbose_name="Tipos noticias", unique=True)
    def __str__(self):
        return self.tipo_noticia

class Usuario(models.Model):

class Noticia(models.Model):
    usuarios_interesados=
    fecha= models.CharField(max_length=20)
    diario = models.OneToOneField(Diario, on_delete=models.CASCADE)
    titular=  models.CharField(max_length=80)
    autores= models.ManyToManyField(Autor)
    resumen= models.CharField(max_length=300)
    tipo=models.OneToOneField(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titular




