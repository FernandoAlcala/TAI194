from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="API de Gestión de Tareas",
    description="API para gestionar una lista de tareas con FastAPI",
    version="1.0.1"
)

# Base de datos simulada
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes", "vencimiento": "14-02-2025", "estado": "True"},
    {"id": 2, "titulo": "Tarea matemáticas", "descripcion": "Ecuaciones diferenciales", "vencimiento": "16-02-2025", "estado": "False"},
    {"id": 3, "titulo": "Ensayo de libro", "descripcion": "Ensayo de 10 paginas sobre la revolución", "vencimiento": "18-02-2025", "estado": "True"},
    {"id": 4, "titulo": "Terminar el proyecto de programación", "descripcion": "Finalizar la API con FastAPI", "vencimiento": "20-02-2025", "estado": "False"},
]

# EndPoint home
@app.get("/", tags=["Inicio"])
def home():
    return {"mensaje": "¡Bienvenido a la API de Gestión de Tareas!"}

#EndPoint CONSULTA TODOS
@app.get('/todasTareas',tags=['Operaciones CRUD'])
def leer():
	return {'Tareas Registradas' : tareas}

# EndPoint CONSULTA POR ID
@app.get("/tareas/{id}", tags=["Operaciones CRUD"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# EndPoint POST (Crear una nueva tarea)
@app.post("/tareas", tags=["Operaciones CRUD"])
def crear_tarea(nueva_tarea: dict):
    for tarea in tareas:
        if tarea["id"] == nueva_tarea.get("id"):
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    tareas.append(nueva_tarea)
    return nueva_tarea