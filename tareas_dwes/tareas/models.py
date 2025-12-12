import uuid
from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recordatorio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Devuelve el título de la tarea en el panel de administración
        return self.titulo