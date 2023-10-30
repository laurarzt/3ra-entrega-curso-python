# recetas/views.py
from django.shortcuts import render
from .models import Receta
from .forms import RecetaForm, BuscarForm

def index(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/index.html', {'recetas': recetas})

def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecetaForm()
    return render(request, 'recetas/agregar_receta.html', {'form': form})

def buscar_receta(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados = Receta.objects.filter(titulo__icontains=busqueda)
            return render(request, 'recetas/buscar_receta.html', {'resultados': resultados, 'form': form})
    else:
        form = BuscarForm()
    return render(request, 'recetas/buscar_receta.html', {'form': form})
