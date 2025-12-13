# DWES-UT03-Practica-2025-2026
Tarea 03 Modelo–Vista–Controlador (MVC)

## 1. Creación del proyecto Django

* [X] Crear un nuevo proyecto Django: django-admin startproject tareas_dwes
* [X] Crear la aplicación principal: python3 manage.py startapp tareas
* [X] Registrar la app tareas en settings.py dentro de INSTALLED_APPS.
* [X] Ejecutar las migraciones iniciales: python3 manage.py migrate
* [X] Verificar el funcionamiento: python3 manage.py runserver
* [X] Una vez llegados a este punto y con todo funcionado, debes crear un commit con el texto Estructura básica funcionando

## 2 Modelo (M)

En tareas/models.py, crear un modelo Tarea con los siguientes campos:
Campo	Tipo	Descripción

* [X] id	UUIDField (primary key)	Identificador único
* [X] titulo	CharField	Nombre o título de la tarea
* [X] descripcion	TextField	Descripción detallada
* [X] completada	BooleanField (por defecto False)	Estado de la tarea
* [X] fecha_creacion	DateTimeField (auto_now_add=True)	Fecha de creación
* [X] fecha_recordatorio	DateTimeField	Fecha recordatorio

* [X] 💡Añade el método __str__() para mostrar el título de la tarea en el panel de administración.

* [X] Commit realizado con el texto Modelo funcionando

## 3. Creación de la vista y la template para mostrar una Tarea

En tareas/views.py, implementar la siguiente vista (funciones que realizan las tareas):
Nombre	Tipo	Descripción

* [X] detalle_tarea	DetailView	Muestra el detalle de una tarea
    
* [X] Commit realizado con el texto Vista funcionando
      
## 4. Creación de la url para mostrar la tarea y el template que la muestre

URLs (C)
* [X] En tareas/urls.py: Crear la ruta correspondiente a la vista.
* [X] Incluir el fichero tareas/urls.py en el urls.py principal del proyecto.

Templates (C)
Crear una carpeta templates/tareas con el siguiente archivo:
Archivo	Descripción
* [X] detalle_tarea.html	Muestra información detallada de la tarea
      
* [X] Commit realizado con el texto Vistas funcionando

* [X] Resultado final en la web

https://github.com/rhernandezmy/DWES-UT03-Practica-2025-2026
