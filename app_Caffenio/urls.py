from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_caffenio, name='inicio'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/actualizar/<int:proveedor_id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/actualizar/realizar/<int:proveedor_id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
]
