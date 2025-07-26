from django.urls import path
from .views import InbdexView, ListaProductosTemplateView, AgregarProductoView, ProductoDetalleView, ActualizarProductoView, EliminarProductoView


app_name = 'inventario'  # Definimos el nombre de la aplicación para el namespace
urlpatterns = [
    path('', InbdexView.as_view(), name='index'),
    path('productos/', ListaProductosTemplateView.as_view(), name='productos'),
    path('nuevo/', AgregarProductoView.as_view(), name='agregar_producto'),
    path('producto/<int:pk>/', ProductoDetalleView.as_view(), name='producto_detalle'),
    path('producto/<int:pk>/uproduct/', ActualizarProductoView.as_view(), name='actualizar_producto'),

]
