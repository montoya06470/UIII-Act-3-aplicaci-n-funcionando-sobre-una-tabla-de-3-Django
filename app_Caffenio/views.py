from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from datetime import datetime

def inicio_caffenio(request):
    # Pasamos la fecha para el footer
    return render(request, 'inicio.html', {'now': datetime.now()})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        empresa = request.POST.get('empresa', '')
        telefono = request.POST.get('telefono', '')
        correo = request.POST.get('correo', '')
        direccion = request.POST.get('direccion', '')
        pais = request.POST.get('pais', '')
        tipo_producto = request.POST.get('tipo_producto', '')

        Proveedor.objects.create(
            nombre=nombre,
            empresa=empresa,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            pais=pais,
            tipo_producto=tipo_producto
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre', proveedor.nombre)
        proveedor.empresa = request.POST.get('empresa', proveedor.empresa)
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono)
        proveedor.correo = request.POST.get('correo', proveedor.correo)
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion)
        proveedor.pais = request.POST.get('pais', proveedor.pais)
        proveedor.tipo_producto = request.POST.get('tipo_producto', proveedor.tipo_producto)
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', proveedor_id=proveedor.id)

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})
