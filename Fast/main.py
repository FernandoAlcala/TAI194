from fastapi import FastAPI
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

#EndPoint promedio
@app.get('/promedio',tags=['Mi calificación TAI'])
def promedio():
	return 10.5

#EndPoint parámetro obligatorio
@app.get('/usuario/{id}',tags=['Endpoint Parámetro Obligatorio'])
def consultausuario(id:int):
	#Caso ficticio de busqueda en BD
	return {"Se encontró el usuario":id}

#EndPoint parámetro opcional
#No lleva el parámetro en las llaves
@app.get('/usuario2/',tags=['Endpoint Parámetro Opcional'])
def consultausuario2(id: Optional[int]=None):
	if id is not None:
		for usuario in usuarios:
			if usuario ["id"]  == id:
				return {"Mensaje":"Usuario encontrado","El usuario es: ":usuario}
		return {"Mensaje":f"No se ha encontrado el id: {id}"}
	return {"Mensaje":"No se proporcionó un id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}