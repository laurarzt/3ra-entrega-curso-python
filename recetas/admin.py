from django.contrib import admin
from ..models import Receta, Ingrediente

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidad')
    search_fields = ('nombre',)

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'mostrar_ingredientes', 'preparacion')
    search_fields = ('titulo', 'descripcion')

    def mostrar_ingredientes(self, obj):
        return ", ".join([ingrediente.nombre for ingrediente in obj.ingredientes.all()])

admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receta, RecetaAdmin)

admin.site.site_header = 'Mi Pastelería'
admin.site.site_title = 'Mi Pastelería'
admin.site.index_title = 'Bienvenido a Mi Pastelería'


# Register your models here.
