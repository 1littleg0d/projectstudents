from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

class AlumnoForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(AlumnoForm, self).__init__(*args, **kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['dni'].widget.attrs['readonly'] = True
  
  class Meta:
    model = Alumno
    fields= ["dni","apellido","nombre","modalidad","debe_previas","email"]

def index(request,template_name="main/index.html"):
  alumnos=Alumno.objects.all()
  return render(request,template_name, {"alumnos":alumnos})

def indexdos(request, template_name="main/alumnos.html"):
  alumnos=Alumno.objects.all()
  return render (request, template_name,  {"alumnos":alumnos}) 

def detalles_alumno(request,pk,template_name="main/detalles_alumno.html"):
  alumno=get_object_or_404(Alumno, pk=pk)
  return render(request,template_name,  {"alumno":alumno}) 
@csrf_exempt

def crear_alumno (request, template_name="main/crear_alumno.html"):
  form=AlumnoForm(request.POST or None)
  
  if form.is_valid():
    form.save()
    return redirect("alumnos")
  
  return render(request, template_name, {"form": form})
@csrf_exempt

def modificar_alumno(request,pk,template_name="main/modificar_alumno.html"):
  alumno=get_object_or_404(Alumno,pk=pk)
  form=AlumnoForm(request.POST or None, instance=alumno)
  
  if form.is_valid():
    form.save()
    return redirect("alumnos")
  
  return render(request, template_name, {'form': form} )
@csrf_exempt

def borrar_alumno(request, pk, template_name="main/borrar_alumno.html"):
  alumno = get_object_or_404( Alumno, pk = pk )
  alumno.delete()
  return redirect("alumnos")
  

