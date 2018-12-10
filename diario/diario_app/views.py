from django.shortcuts import render
from diario_app.models import Diario
from .forms import DiarioForm
from django.http import HttpResponseRedirect
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def diarios_por_pais(request):
    diarios = Diario.objects.all()
    #genres = Genre.objects.all()
    return render(request, 'lista_diarios_pais.html',{'lista_diarios':diarios})

def crear_diario(request):
    if request.method == 'POST':
        form=DiarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DiarioForm()
    return render(request,'diario_form.html',{'form':form})