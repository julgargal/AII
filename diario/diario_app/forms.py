from django.forms import ModelForm
from django import forms
from diario_app.models import Diario

#class DiarioForm(forms.Form):
#    class Meta:
#        model=Diario
#        fields=['nombre','pais','idioma']

#class DiarioForm(forms.Form):
#    nombre = forms.CharField(label='Nombre ', max_length=100)
#    pais = forms.CharField(label='Pais ', max_length=100)
#    idioma = forms.CharField(label='Idioma ', max_length=100)

class DiarioForm(ModelForm):
    class Meta:
        model=Diario
        fields = ['nombre', 'pais', 'idioma']
