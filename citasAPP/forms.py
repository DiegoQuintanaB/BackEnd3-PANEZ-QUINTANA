# forms.py

from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['numero_reserva', 'tipo_servicio', 'horario', 'fecha']
        widgets = {
            'horario': forms.TextInput(attrs={'type': 'datetime-local'}),
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }


#login
#registrarse usuario
from django.contrib.auth.models import User
#registrar usuario
class FormUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={"class":"form-control", "id":"floatingInput", "placeholder":"nombre usuario"}),
            'first_name': forms.TextInput(attrs={"class":"form-control", "id":"floatingInput", "placeholder":"nombre"}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "id":"floatingInput", "placeholder":"apellido"}),
            'email': forms.EmailInput(attrs={"class":"form-control", "id":"floatingInput", "placeholder":"email"}),
            'password': forms.PasswordInput(attrs={"class":"form-control", "id":"floatingInput", "placeholder":"contraseña"})
        }
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'password': 'Contraseña',

        }
        fields = ['username', 'first_name', 'last_name',  'email', 'password',]