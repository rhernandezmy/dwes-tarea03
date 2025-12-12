from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Tarea

class DetalleTarea(DetailView):

    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'

class ListaTareas(ListView):
    model = Tarea
    template_name = 'tareas/lista_tareas.html'  # Plantilla para listar las tareas
    context_object_name = 'tareas' 