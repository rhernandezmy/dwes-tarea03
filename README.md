# dwes-tarea03
Tarea 03 Modelo–Vista–Controlador (MVC)

## 2.1. Modelo (M)

En tareas/models.py, crear un modelo Tarea con los siguientes campos:
Campo	Tipo	Descripción

* [X] id	UUIDField (primary key)	Identificador único
* [X] titulo	CharField	Nombre o título de la tarea
* [X] descripcion	TextField	Descripción detallada
* [X] completada	BooleanField (por defecto False)	Estado de la tarea
* [X] fecha_creacion	DateTimeField (auto_now_add=True)	Fecha de creación
* [X] fecha_recordatorio	DateTimeField	Fecha recordatorio

    💡 [X] Añade el método __str__() para mostrar el título de la tarea en el panel de administración.