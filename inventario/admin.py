from django.contrib import admin
from .models import Producto, Comentario # Importamos el nuevo modelo

@admin.register(Producto) # Registramos el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_actualizacion')
    list_filter = ('fecha_creacion', 'stock')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(Comentario) # Registramos el modelo Comentario
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'autor', 'fecha_creacion', 'texto')
    list_filter = ('fecha_creacion', 'autor')
    search_fields = ('texto', 'autor', 'producto__nombre') # Permite buscar por nombre de producto
    date_hierarchy = 'fecha_creacion' # Jerarquía de fechas para navegar
    raw_id_fields = ('producto',) # Para que el selector de producto sea un widget de búsqueda, útil con muchos productos
