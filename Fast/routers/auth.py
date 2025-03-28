from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from genToken import createToken
from fastapi import APIRouter

routerAuth = APIRouter()

#EndPoint para generar Token
@routerAuth.post('/auth', tags=['Autentificacion'])
def auth(credenciales:modelAuth):
	if credenciales.mail == 'fernando@example.com' and credenciales.passw == '123456789':
		token:str = createToken(credenciales.model_dump())
		print(token)
		return JSONResponse(content=token)
	else:
		return{"Aviso:":"El usuario no cuenta con permiso"}