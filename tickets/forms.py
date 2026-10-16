from django import forms
from .models import ticket

class TicketForm(forms.ModelForm):
    prioridad = forms.ChoiceField(
        choices=[
            ('', 'Seleccione prioridad'),
            ('Baja', 'Baja'),
            ('Media', 'Media'),
            ('Alta', 'Alta'),
            ('Urgente', 'Urgente'),
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True}),
    )

    estado = forms.ChoiceField(
        choices=[
            ('', 'Seleccione estado'),
            ('Pendiente', 'Pendiente'),
            ('En proceso', 'En proceso'),
            ('Finalizado', 'Finalizado'),
            ('Cerrado', 'Cerrado'),
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True}),
    )

    fechacierre = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'required': True}),
    )

    class Meta:
        model = ticket
        fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'fechacierre']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Falla en servidor', 'required': True}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el problema o solicitud de mantenimiento', 'required': True}),
        }