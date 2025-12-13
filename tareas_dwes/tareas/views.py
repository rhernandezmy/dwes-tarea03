from django.views.generic import DetailView
from types import SimpleNamespace
from datetime import date, timedelta

# Create your views here.
class DetalleTarea(DetailView):
    template_name = 'tareas/detalle_tarea.html'

    def get_object(self, queryset=None):
        fecha_hoy = date.today()
        fecha_recordatorio = fecha_hoy + timedelta(days=7)  # Una semana después

        return SimpleNamespace(
            titulo="Detalle de la Tarea",
            descripcion="Muestra información detallada de la tarea",
            completada=False,
            fecha_creacion=fecha_hoy,
            fecha_recordatorio=fecha_recordatorio
        )


