from django.forms import ModelForm
from django import forms
from diario_app.models import Diario

class DiarioForm(forms.Form):
    class Meta:
        model=Diario
        fields=['nombre','pais','idioma']