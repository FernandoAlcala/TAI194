from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
	title="Mi primer API",
	description="Fernando López Alcalá",
	version="1.0.1"
)

usuarios=[
	{"id":1,"nombre":"Fernando", "edad":30},
	{"id":2,"nombre":"Roberto", "edad":34},
	{"id":3,"nombre":"Graciela", "edad":24},
	{"id":4,"nombre":"Jesus", "edad":27},
	{"id":5,"nombre":"Daniela", "edad":27},
]

#EndPoint home
@app.get('/',tags=['Inicio'])
def home():
	return {'hello':'Hello FastAPI!'}

#EndPoint CONSULTA TODOS
@app.get('/todosUsuarios',tags=['Operaciones CRUD'])
def leer():
	return {'Usuarios Registrados' : usuarios}
	
#EndPoint POST
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def guardar(usuario:dict):
	for usr in usuarios:
		if usr["id"] == usuario.get("id"):
			raise HTTPException(status_code=400, detail="El usuario ya existe")
	usuarios.append(usuario)
	return usuario

#EndPoint Actualizar
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
	for index, usr in enumerate(usuarios):
		if usr["id"] == id:
			usuarios[index].update(usuarioActualizado)
			return usuarios[index]
	raise HTTPException(status_code=400, detail="El usuario no existe")