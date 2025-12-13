from django.urls import path
from .views import DetalleTarea

urlpatterns = [
    path('', DetalleTarea.as_view(), name='detalle_tarea'),
]
