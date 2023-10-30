from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    unidad = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    preparacion = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo