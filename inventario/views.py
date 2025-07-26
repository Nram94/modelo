# inventario/views.py

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView # ¡Importante! Importamos TemplateView y DetailView
from .models import Producto # Importamos el modelo Producto
from django.forms import ModelForm, CharField, DecimalField, IntegerField, Textarea, ValidationError
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse


class InbdexView(TemplateView):
    """
    Controlador basado en clases que hereda de TemplateView para
    mostrar una lista de productos.
    Actúa como el "C" de MVC: maneja la lógica de negocio simple
    y pasa los datos a la vista.
    """
    template_name = 'inventario/index.html'  # Especificamos el template a usar



class ListaProductosTemplateView(TemplateView):
    """
    Controlador basado en clases que hereda de TemplateView para
    mostrar una lista de productos de forma más concisa.
    """
    template_name = 'inventario/productos.html' # Indicamos el template directamente
    model = Producto # Definimos el modelo para usar en el contexto
    def get_context_data(self, **kwargs):
        """
        Este método se usa para añadir datos al contexto del template.
        """
        contexto = super().get_context_data(**kwargs) # Llama al método de la clase padre
        productos = Producto.objects.all() 
        contexto['productos'] = productos # Agregamos nuestros productos al contexto
        return contexto

# ¡Punto Clave! `TemplateView` nos permite definir el `template_name` directamente.
# La lógica para añadir datos al contexto se hace en `get_context_data()`,
# lo que mantiene nuestra lógica de negocio separada de la representación.

# --- Clase de formulario básica (sin cambios) ---
class ProductoFormularioBasico(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise ValidationError("El stock no puede ser negativo.")
        return stock

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise ValidationError("El precio no puede ser negativo.")
        return precio

# --- Vista para Listar Productos (sin cambios) ---
class ListaProductosTemplateView(TemplateView):
    template_name = 'inventario/lista_productos.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        productos = Producto.objects.all().order_by('id')  # Ordenamos por nombre
        contexto['productos'] = productos
        return contexto

# --- Vista para Agregar Productos ( ---
class AgregarProductoView(CreateView):
    """
    Vista para agregar un nuevo producto al inventario.
    Utiliza un formulario basado en el modelo Producto.
    """
    model = Producto
    form_class = ProductoFormularioBasico
    template_name = 'inventario/agregar_producto.html'
    
    def form_valid(self, form):
        """
        Este método se llama cuando el formulario es válido.
        Aquí guardamos el producto y redirigimos a la lista de productos.
        """
        form.save()  # Guarda el producto
        return redirect(reverse('productos'))  # Redirige a la lista de productos

# --- Vista para Detalle de Producto (con Comentarios) ---
class ProductoDetalleView(DetailView):
    """
    Vista para mostrar los detalles de un producto y sus comentarios.
    Utiliza el modelo Producto y muestra los comentarios relacionados.
    """
    model = Producto
    template_name = 'inventario/producto_detalle.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregamos los comentarios del producto al contexto
        context['comentarios'] = self.object.comentarios.all()
        return context
    
# --- Vista para Actualizar Producto ---
class ActualizarProductoView(UpdateView):
    """
    Vista para actualizar un producto existente en el inventario.
    Utiliza un formulario basado en el modelo Producto.
    """
    model = Producto
    form_class = ProductoFormularioBasico
    template_name = 'inventario/actualizar_producto.html'

    def form_valid(self, form):
        """
        Este método se llama cuando el formulario es válido.
        Aquí actualizamos el producto y redirigimos a su detalle.
        """
        form.save()  # Actualiza el producto
        return redirect(reverse('producto_detalle', kwargs={'pk': self.object.pk}))
    
# --- Vista para Eliminar Producto ---
class EliminarProductoView(DeleteView): 
    """
    Vista para eliminar un producto del inventario.
    Utiliza el modelo Producto y redirige a la lista de productos.
    """
    model = Producto
    template_name = 'inventario/eliminar_producto.html'
    
    def get_success_url(self):
        """
        Este método se llama después de eliminar el producto.
        Redirige a la lista de productos.
        """
        return reverse('lista_productos')