from django.db import models
# Create your models here.

class Diario(models.Model):
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=30)
    idioma=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre_usuario= models.CharField(max_length=20, primary_key=True)
    passwd=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_usuario

class Tipo(models.Model):
    tipo_noticia = models.CharField(max_length=80, primary_key=True, verbose_name="Tipos noticias", unique=True)
    def __str__(self):
        return self.tipo_noticia

class Autor(models.Model):
    autor_id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    usuarios_interesados=models.ManyToManyField(Usuario)
    fecha= models.CharField(max_length=20)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE)
    titular=  models.CharField(max_length=80)
    autores= models.ManyToManyField(Autor)
    resumen= models.CharField(max_length=300)
    tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titular




