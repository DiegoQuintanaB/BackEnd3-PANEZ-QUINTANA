from django.shortcuts import render, redirect
from .forms import * 
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
#menu
def menu(request):
    return render(request, 'menu.html')

# Crear citas
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Haz guardado tu cita con éxito.')
            return redirect('crear_cita')
    else:
        form = CitaForm()

    return render(request, 'citas.html', {'form': form})

#ver citas
from .models import Cita

def ver_citas(request):
    citas = Cita.objects.all()
    return render(request, 'vercitas.html', {'citas': citas})

#login
#registrarse
def registrarse(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, 'Registrado con exito.')
            return render(request, 'registration/login.html')
        else:
            messages.error(request, 'El nombre de usuario ya existe.')
    else:
        form = FormUser()

    data = {
        'form': form
    }
    return render(request, 'registro.html', data)
#cerrar sesion
from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    return redirect('menu')  





