from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from .models import Voluntario

class RegistroForm(UserCreationForm):
        model = User
        fields = [
            'username',    
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
        }



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

