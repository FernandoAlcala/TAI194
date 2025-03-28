from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

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

app.include_router(routerUsuario)
app.include_router(routerAuth)