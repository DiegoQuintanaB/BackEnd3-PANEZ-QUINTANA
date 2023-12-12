"""
URL configuration for citas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from citasAPP.views import * 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    #menu
    path('', menu, name="menu"),
    #servicios
    #agregarcitas
    path('crear_cita/', crear_cita, name='crear_cita'),

    #ver citas
    path('ver_citas/', ver_citas, name='ver_citas'),

    #login
    # iniciar sesion 
    path('accounts/', include('django.contrib.auth.urls')),
    path('cuenta/', include('django.contrib.auth.urls')),
    
    #registrarse
    path('registrarse/',registrarse, name='registrarse'),

    #olvidoContraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    #salirSesionDjango
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),


]
