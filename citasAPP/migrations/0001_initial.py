# Generated by Django 4.2.6 on 2023-11-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_reserva', models.CharField(max_length=10)),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('horario', models.DateTimeField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]