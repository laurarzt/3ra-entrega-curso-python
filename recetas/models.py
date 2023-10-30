from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    instrucciones = models.TextField()
    
