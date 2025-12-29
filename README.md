# FastAPI Task API

API REST construida con FastAPI para gestión de tareas, como parte de una prueba técnica de Backend Python.

Incluye autenticación JWT, persistencia con PostgreSQL, migraciones con Alembic y CRUD completo de tareas por usuario.

---

## 🧰 Tecnologías

- Python 3.11
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL (Docker)
- Alembic
- JWT (python-jose)
- Passlib (bcrypt)

---

## 📋 Requisitos

- Python 3.11+
- Docker y Docker Compose
- pip / virtualenv

---

## ⚙️ Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=technical_test
DB_USER=postgres
DB_PASSWORD=postgres

JWT_SECRET_KEY=supersecretkey
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```

---

## 🐘 Base de datos (PostgreSQL con Docker)

Levantar la base de datos localmente:

```
docker compose up -d
```

La base quedará disponible en localhost:5432.

---

## 🚀 Instalación y ejecución

Crear un archivo `.env` a partir de `.env.example` y ajustar las variables según sea necesario.

Crear y activar entorno virtual:

```
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

Instalar dependencias:
```
pip install -r requirements.txt
```

Ejecutar migraciones:
```
alembic upgrade head
```

Levantar la aplicación:
```
uvicorn app.main:app --reload
```

La API estará disponible en:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs

---

## 👤 Usuario inicial

La aplicación crea automáticamente un usuario administrador mediante una migración de Alembic.

Credenciales por defecto:
```
username: admin
password: 1234
```

---

## 🔐 Autenticación (Postman)

La API utiliza autenticación basada en JWT (JSON Web Tokens).  
Todos los endpoints de tareas están protegidos y requieren un token válido.

Login

Endpoint:
```
POST /auth/login
```

Configuración en Postman:

- Method: `POST`
- URL: `http://localhost:8000/auth/login`
- Headers:
  - `Content-Type: application/x-www-form-urlencoded`
- Body → `x-www-form-urlencoded`:
  - `username`: `admin`
  - `password`: `1234`

Al enviar la request correctamente, la API devuelve:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

---

## 📝 Endpoints principales
Crear tarea
```
POST /tasks/
```

Listar tareas (paginación)
```
GET /tasks/?skip=0&limit=10
```

Los parámetros `skip` y `limit` son opcionales y controlan la paginación del listado.

Obtener tarea
```
GET /tasks/{task_id}
```

Actualizar tarea
```
PUT /tasks/{task_id}
```

Eliminar tarea
```
DELETE /tasks/{task_id}
```

Todos los endpoints de tareas requieren autenticación.

---
## Decisiones técnicas

- Se utilizó JWT para autenticación con expiración configurable.
- Las contraseñas se almacenan utilizando hash seguro con bcrypt.
- Las tareas están asociadas al usuario autenticado.
- Se utilizó paginación basada en skip y limit para simplicidad.
- No se agregó una capa services ya que la lógica de negocio es simple y específica de cada endpoint.
- El campo `completed` se utilizó en lugar de un `status` con múltiples estados para simplificar el modelo de dominio, dado que los requisitos funcionales del ejercicio no requieren flujos de estado más complejos. La arquitectura permite extender fácilmente a un enum de estados si fuera necesario.
