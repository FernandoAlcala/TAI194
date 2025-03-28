from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Optional, List
#from pydantic import BaseModel
from modelsPydantic import modelUsuario, modelAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
	title="Mi primer API",
	description="Fernando López Alcalá",
	version="1.0.1"
)

Base.metadata.create_all(bind=engine)

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
		return JSONResponse(content=token)
	else:
		return{"Aviso:":"El usuario no cuenta con permiso"}

#EndPoint CONSULTA TODOS
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
def leer():
	db=Session()
	try:
		consulta=db.query(User).all()
		return JSONResponse(content= jsonable_encoder(consulta))
	except Exception as e:
		db.rollback()
		return JSONResponse(status_code=500,content={"message":"No fue posible consultar", "error": str(e)})
	finally:
		db.close()

#EndPoint BUSCAR POR ID
@app.get('/usuario/{id}', tags=['Operaciones CRUD'])
def leeruno(id:int):
	db=Session()
	try:
		consulta1=db.query(User).filter(User.id == id).first()
		if not consulta1:
			return JSONResponse(status_code=404, content={"mensaje":"Usuario no encontrado"})
		else:
			return JSONResponse(content= jsonable_encoder(consulta1))
	except Exception as e:
		db.rollback()
		return JSONResponse(status_code=500,content={"message":"No fue posible consultar", "error": str(e)})
	finally:
		db.close()
	
#EndPoint POST
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
	db=Session()
	try:
		db.add(User(**usuario.model_dump()))
		db.commit()
		return JSONResponse(status_code=201,content={"message":"Usuario Guardado", "usuario":usuario.model_dump()})
	except Exception as e:
		db.rollback()
		return JSONResponse(status_code=500,content={"message":"Error al guardar", "error": str(e)})
	finally:
		db.close()

#EndPoint Actualizar
@app.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario):
	db=Session()
	try:
		usuario_db = db.query(User).filter(User.id == id).first()
		if not usuario_db:
			return JSONResponse(status_code=404, content={"mensaje":"Usuario no encontrado"})
		
		for key, value in usuarioActualizado.model_dump().items():
			setattr(usuario_db, key, value)
		
		db.commit()
		return JSONResponse(status_code=200, content={"message":"Usuario Actualizado", "usuario":usuarioActualizado.model_dump()})
	except Exception as e:
		db.rollback()
		return JSONResponse(status_code=500,content={"message":"Error al actualizar", "error": str(e)})
	finally:
		db.close()

#EndPoint Eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int):
	db=Session()
	try:
		usuario_db = db.query(User).filter(User.id == id).first()
		if not usuario_db:
			return JSONResponse(status_code=404, content={"mensaje":"Usuario no encontrado"})
		
		db.delete(usuario_db)
		db.commit()
		return JSONResponse(status_code=200, content={"message":"Usuario Eliminado"})
	except Exception as e:
		db.rollback()
		return JSONResponse(status_code=500, content={"message":"Error al eliminar", "error": str(e)})
	finally:
		db.close()