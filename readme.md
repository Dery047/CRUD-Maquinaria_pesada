# Vehicles API

Proyecto API REST para gestionar vehículos, construido con Django y Django REST Framework.

 **En desarrollo**  
Actualmente la API está funcional para CRUD de vehículos, pero el proyecto está en proceso.  
Faltan cosas importantes, como la integración del frontend con React, no agregaré por el momento autenticación porque es solo para uso local de un cliente, podría incluirse autenticación con admin de Django.

---

## Estado actual

- API básica funcionando con endpoints para vehículos.
- Modelo, serializadores y vistas configurados.
- Rutas y configuración Django listas.
- Falta interfaz de usuario y autenticación robusta.

---

## Próximos pasos

-Estaré desarrollando una vista de front end con una vista simple pero amigable y que sea usable dentro de un entorno real de producción
- Agregar autenticación si es necesario, usando tokens JWT


---

## Cómo ejecutar

1. Clonar repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar migraciones: `python manage.py migrate`
5. Correr servidor: `python manage.py runserver`

---

Cualquier contribución o sugerencia será bienvenida.


# Vehicles API

REST API project to manage vehicles, built with Django and Django REST Framework.

 **Work in progress**  
The API is currently functional for vehicle CRUD, but the project is still in progress.  
Important stuff like React frontend integration is missing.  
No authentication added for now since it’s just for local use by a client. Could use Django admin auth if needed.

---

## Current status

- Basic API working with vehicle endpoints.  
- Models, serializers, and views set up.  
- Django routes and settings configured.  
- Missing user interface.

---

## Next steps

- i'll be adding a basic but simple frontend view so it can be used in a real production environment.
- (Optional) Add Django admin authentication if needed.  
- 

---

## How to run

1. Clone the repo  
2. Create and activate a virtual environment  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run migrations: `python manage.py migrate`  
5. Start the server: `python manage.py runserver`

---

Any contributions or suggestions are welcome!
