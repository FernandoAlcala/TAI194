from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

#Crud de usuarios

#EndPoint CONSULTA TODOS
@routerUsuario.get('/todosUsuarios', tags=['Operaciones CRUD'])
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
@routerUsuario.get('/usuario/{id}', tags=['Operaciones CRUD'])
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
@routerUsuario.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
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