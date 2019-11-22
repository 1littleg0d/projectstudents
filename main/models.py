from django.db import models
from django.forms import Field

MODALIDADES=(
("Informatica","Informatica"),
("Electromecanica","Electromecanica")
)
  

class Alumno(models.Model):
  dni=models.PositiveIntegerField("DNI",null=False,primary_key=True)
  apellido=models.CharField("Apellido",max_length=40)
  nombre=models.CharField("Nombre",max_length=40)
  email=models.EmailField("Email")
  modalidad=models.CharField("Modalidad",choices=MODALIDADES, max_length=70, default="Informatica")
  debe_previas=models.BooleanField("Previas",default=False)