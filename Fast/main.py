from fastapi import FastAPI, HTTPException
from typing import Optional, List
#from pydantic import BaseModel
from models import modelUsuario, modelAuth
from genToken import createToken

app = FastAPI(
	title="Mi primer API",
	description="Fernando López Alcalá",
	version="1.0.1"
)

#class modelUsuario(BaseModel):
#	id:int
#	nombre:str
#	edad:int
#	correo:str

usuarios=[
	{"id":1,"nombre":"Fernando", "edad":30, "correo":"fernando@gmail.com"},
	{"id":2,"nombre":"Roberto", "edad":34, "correo":"roberto@gmail.com"},
	{"id":3,"nombre":"Graciela", "edad":24, "correo":"graciela@gmail.com"},
	{"id":4,"nombre":"Jesus", "edad":27, "correo":"jesus@gmail.com"},
	{"id":5,"nombre":"Daniela", "edad":27, "correo":"daniela@gmail.com"},
]

#EndPoint home
@app.get('/',tags=['Inicio'])
def home():
	return {'hello':'Hello FastAPI!'}

#EndPoint para generar Token
@app.post('/auth', tags=['Autentificacion'])
def auth(credenciales:modelAuth):
	if credenciales.mail == 'fernando@example.com' and credenciales.passw == '123456789':
		token:str = createToken(credenciales.model_dump())
		print(token)
		return{"Aviso:":"Token Generado"}
	else:
		return{"Aviso:":"El usuario no cuenta con permiso"}

#EndPoint CONSULTA TODOS
@app.get('/todosUsuarios', response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
	return usuarios
	
#EndPoint POST
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
	for usr in usuarios:
		if usr["id"] == usuario.id:
			raise HTTPException(status_code=400, detail="El usuario ya existe")
	usuarios.append(usuario)
	return usuario

#EndPoint Actualizar
@app.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
	for index, usr in enumerate(usuarios):
		if usr["id"] == id:
			usuarios[index] = usuarioActualizado.model_dump()
			return usuarios[index]
	raise HTTPException(status_code=400, detail="El usuario no existe")

#EndPoint Eliminar
@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int):
	for index, usr in enumerate(usuarios):
		if usr["id"] == id:
			usuarios.pop(index)
			return
	raise HTTPException(status_code=400, detail="El usuario que estás buscando no existe")