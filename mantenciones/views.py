from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import mantencion
from .forms import MantencionForm

# Create your views here.

@login_required
def lista_mantenciones(request):
    mantenciones = mantencion.objects.order_by('-fechainicio')
    form = MantencionForm()
    return render(request, 'lista_mantenciones.html', {'mantenciones': mantenciones, 'form': form})

def crear_mantencion(request):
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mantenciones')
        else:
            mantenciones = mantencion.objects.order_by('-fechainicio')
            return render(request, 'lista_mantenciones.html', {'mantenciones': mantenciones, 'form': form})
    return redirect('listar_mantenciones')