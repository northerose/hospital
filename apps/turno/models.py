from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(max_length=8)
    email = models.EmailField()


class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)


class Especialidad(models.Model):
    nombre = models.CharField(max_length=200)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)


class Profesional(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=8)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)


horarios = [
            ('manana', "Mañana"),
            ('tarde', "Tarde"),
            ('noche', "Noche"),
            ]
class Horario(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100, choices= horarios, default='manana')


class Turno(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()

