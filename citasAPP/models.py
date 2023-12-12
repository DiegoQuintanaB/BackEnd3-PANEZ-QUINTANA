from django.db import models

# Create your models here.

class Cita(models.Model):
    numero_reserva = models.CharField(max_length=10)
    tipo_servicio = models.CharField(max_length=50)
    horario = models.DateTimeField()
    fecha = models.DateField()
    

    def __str__(self):
        return f"Cita {self.numero_reserva}"
    

#login

