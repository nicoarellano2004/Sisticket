from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required, login_required
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm

# Create your views here.

@permission_required('usuarios.view_usuario', raise_exception=True)
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    form = UsuarioForm()
    permisos_disponibles = Permission.objects.select_related('content_type').order_by('content_type__app_label', 'content_type__model', 'name')
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios, 'form': form, 'permisos_disponibles': permisos_disponibles})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            rol = form.cleaned_data.get('rol')
            if rol:
                usuario.groups.add(rol)
            return redirect('listar_usuarios')
        usuarios = Usuario.objects.all()
        permisos_disponibles = Permission.objects.select_related('content_type').order_by('content_type__app_label', 'content_type__model', 'name')
        return render(request, 'lista_usuarios.html', {'usuarios': usuarios, 'form': form, 'permisos_disponibles': permisos_disponibles})

    return redirect('listar_usuarios')

@login_required
def perfil_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'perfil_usuario.html', {'usuario': usuario})

def crear_rol(request):
    if request.method == 'POST':
        nombre_rol = request.POST.get('nombre_rol', '').strip()
        permisos_seleccionados = request.POST.getlist('permisos')
        if nombre_rol:
            grupo, creado = Group.objects.get_or_create(name=nombre_rol)
            permisos = Permission.objects.filter(id__in=permisos_seleccionados)
            grupo.permissions.set(permisos)
    return redirect('listar_usuarios')