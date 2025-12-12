from django.urls import path
from .views import ListaTareas, DetalleTarea

urlpatterns = [
    path('tarea/<uuid:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('', ListaTareas.as_view(), name='lista_tareas'),  # Ruta para mostrar todas las tareas
]