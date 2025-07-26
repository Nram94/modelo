from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True,
                              verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True,
                                   verbose_name="Descripción Detallada")
    precio = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name="Precio Unitario")
    stock = models.IntegerField(default=0,
                                verbose_name="Cantidad en Stock")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto de Inventario"
        verbose_name_plural = "Productos de Inventario"
        ordering = ['nombre']

    def clean(self):
        if self.precio < 0:
            raise ValidationError({'precio': _('El precio no puede ser negativo.')})
        if self.stock < 0:
            raise ValidationError({'stock': _('El stock no puede ser negativo.')})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"


class Comentario(models.Model):
    """
    Modelo para los comentarios de los productos.
    Muestra una relación Many-to-One con Producto.
    """
    #  product = models.ForeignKey (Product, related_name='comments' on_delete=models.CASCADE)
    # Usamos 'comentarios' como related_name para acceder fácilmente a los comentarios de un producto.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,
                                 related_name='comentarios',
                                 verbose_name="Producto Asociado")
    texto = models.TextField(verbose_name="Contenido del Comentario")
    autor = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name="Autor del Comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Comentario de Producto"
        verbose_name_plural = "Comentarios de Productos"
        ordering = ['-fecha_creacion'] # Ordenar por los más recientes primero

    def __str__(self):
        return f"Comentario de {self.autor or 'Anónimo'} en {self.producto.nombre[:20]}..."

# ¡Punto Clave! La `ForeignKey` es el corazón de las relaciones de uno a muchos.
# El `related_name` nos permite `producto.comentarios.all()` en lugar de `producto.comment_set.all()`.