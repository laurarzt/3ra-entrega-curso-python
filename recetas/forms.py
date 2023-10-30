from django import forms
from .models import Categoria, Ingrediente, Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'ingredientes', 'instrucciones']

class BuscarForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    