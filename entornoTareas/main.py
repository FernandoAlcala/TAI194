from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="API de Gestión de Tareas",
    description="API para gestionar una lista de tareas con FastAPI",
    version="1.0.1"
)

# Base de datos simulada
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes", "vencimiento": "14-02-2025", "estado": True},
    {"id": 2, "titulo": "Tarea matemáticas", "descripcion": "Ecuaciones diferenciales", "vencimiento": "16-02-2025", "estado": False},
    {"id": 3, "titulo": "Ensayo de libro", "descripcion": "Ensayo de 10 paginas sobre la revolución", "vencimiento": "18-02-2025", "estado": True},
    {"id": 4, "titulo": "Terminar el proyecto de programación", "descripcion": "Finalizar la API con FastAPI", "vencimiento": "20-02-2025", "estado": False},
]

# EndPoint home
@app.get("/", tags=["Inicio"])
def home():
    return {"mensaje": "¡Bienvenido a la API de Gestión de Tareas!"}