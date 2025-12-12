from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import Tarea

class DetalleTarea(DetailView):

    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'