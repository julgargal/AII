#encoding:utf-8
import csv
import os
import django
import re
import time
import sys

# Muy importantes las dos líneas siguientes, sino da un error de que no encuentra la app "movies"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diario.settings")
django.setup()
from diario_app import models

listaTipos = ["Deportes","Cultura","Política","Economía","Actualidad"]


def populateTipos():
    models.Tipo.objects.all().delete()
    j = 0
    for i in range(0, len(listaTipos)):
        tipo = models.Tipo(tipo_noticia=listaTipos[i])
        tipo.save()
        j = j + 1
    print("Se han cargado correctamente " + str(j) + " tipos de noticias")



populateTipos()