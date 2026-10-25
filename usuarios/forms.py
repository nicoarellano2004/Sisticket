from django import forms
from django.contrib.auth.models import Group
from usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):
    rol = forms.ModelChoiceField(
        queryset=Group.objects.none(),
        required=True,
        empty_label='Seleccione un rol',
        label='Rol',
    )

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'username', 'rut', 'password', 'rol', 'telefono', 'direccion', 'img']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario', 'required': True}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT (sin puntos ni guión)', 'required': True, 'pattern': r'^\d{7,8}-[0-9kK]$'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'required': True, 'pattern': r'^\+?\d{7,15}$'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'required': True, 'minlength': 5}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'required': True}),
        }
        exclude = ['last_login', 'date_joined', 'groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rol'].queryset = Group.objects.order_by('name')
        self.fields['rol'].widget.attrs.update({'class': 'form-select'})