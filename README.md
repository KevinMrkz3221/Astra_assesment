# Astra Assesment

## Descripción

Esta API permite la creación de usuarios y la gestión de tareas o notas por parte de cada usuario registrado. Una vez autenticado, el usuario puede realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre sus notas o tareas personales. El sistema está diseñado para ofrecer una interfaz eficiente y fácil de usar para la gestión de información personal.

## Características

- Registro y autenticación de usuarios.
- CRUD completo para [recursos gestionados, como notas, tareas].
- Autenticación basada en JWT (JSON Web Tokens).
- Manejo de bases de datos con SQLAlchemy.
- Documentación automática de la API usando Swagger UI y Redoc.

## Requisitos

- Python python-3.10.12
- alembic==1.13.2
- annotated-types==0.7.0
- anyio==4.4.0
- bcrypt==4.2.0
- click==8.1.7
- exceptiongroup==1.2.2
- fastapi==0.114.1
- greenlet==3.1.0
- h11==0.14.0
- idna==3.8
- Mako==1.3.5
- MarkupSafe==2.1.5
- passlib==1.7.4
- pydantic==2.9.1
- pydantic-settings==2.5.2
- pydantic_core==2.23.3
- PyJWT==2.9.0
- python-dotenv==1.0.1
- sniffio==1.3.1
- SQLAlchemy==2.0.34
- starlette==0.38.5
- typing_extensions==4.12.2
- uvicorn==0.30.6


## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/usuario/proyecto-fastapi.git
    cd proyecto-fastapi
    ```

2. Crea un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura la base de datos en `app/database.py` o usando variables de entorno.

## Ejecución

1. Inicia el servidor de desarrollo:
    ```bash
    uvicorn main:app --reload or python3 main.py
    ```

2. Visita la documentación interactiva de la API:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Uso de la API

### Endpoints principales:

- **`POST /register`**: Registra un nuevo usuario.
- **`POST /login`**: Inicia sesión y genera un token JWT.
- **`GET /notes/`**: Obtiene todas las notas del usuario autenticado.
- **`POST /notes/`**: Crea una nueva nota.
- **`PUT /notes/{id}`**: Actualiza una nota existente.
- **`DELETE /notes/{id}`**: Elimina una nota.
- **`GET /tasks/`**: Obtiene todas las tareas del usuario autenticado.
- **`POST /tasks/`**: Crea una nueva tarea.
- **`PUT /tasks/{id}`**: Actualiza una tarea existente.
- **`DELETE /tasks/{id}`**: Elimina una tarea.

### Ejemplo de solicitud

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}'
