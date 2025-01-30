from fastapi import FastAPI

app = FastAPI()

#EndPoint home
@app.get('/')
def home():
	return {'hello':'Hello FastAPI!'}

#EndPoint promedio
@app.get('/promedio')
def promedio():
	return 10.5

#EndPoint parámetro obligatorio
@app.get('/usuario/{id}')
def consultausuario(id:int):
	#Caso ficticio de busqueda en BD
	return {"Se encontró el usuario":id}