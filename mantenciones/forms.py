from django import forms
from .models import mantencion
from tickets.models import ticket

class MantencionForm(forms.ModelForm):
    idticket = forms.ModelChoiceField(
        queryset=ticket.objects.all(),
        empty_label="Seleccione un ticket",
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False
    )

    estado = forms.ChoiceField(
        choices=[
            ('', 'Seleccione estado'),
            ('Pendiente', 'Pendiente'),
            ('En Proceso', 'En Proceso'),
            ('Finalizado', 'Finalizado'),
            ('Cerrado', 'Cerrado'),
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'required': True}),
    )

    fechatermino = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'required': True}),
    )

    class Meta:
        model = mantencion
        fields = ['idticket', 'descripcion', 'estado', 'observaciones', 'fechatermino']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe la mantención a realizar', 'required': True, 'minlength': 10}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Observaciones adicionales (opcional)'}),
        }