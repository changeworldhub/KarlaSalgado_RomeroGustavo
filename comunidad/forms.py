from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = [
            'rut',
            'nombre',
            'apellido',
            'email',
            'telefono',
            'pais',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Email',
            'telefono': 'Telefono',
            'pais': 'Pais',
        }

