from django.contrib import admin
from diario_app.models import Diario, Usuario,Tipo,Autor,Noticia

# Register your models here.
admin.site.register(Diario)
admin.site.register(Usuario)
admin.site.register(Tipo)
admin.site.register(Autor)
admin.site.register(Noticia)