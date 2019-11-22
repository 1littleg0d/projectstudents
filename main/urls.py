from django.contrib import admin
from main import views
from django.urls import path 
from django.conf.urls import url

urlpatterns = [
  path("",views.index,name="index"),
  path("detalles_alumno/<int:pk>",views.detalles_alumno, name="detalles_alumno"),
  path("crear_alumno/",views.crear_alumno, name="crear_alumno"),
  path("alumnos/borrar_alumno/<int:pk>",views.borrar_alumno,name="borrar_alumno"),
  path("modificar_alumno/<int:pk>", views.modificar_alumno, name="modificar_alumno"),
  path(r'admin/', admin.site.urls),
  path("alumnos/",views.indexdos,name="alumnos"),
]