from fastapi import FastAPI

app = FastAPI()

#Ruta o EndPoint
@app.get('/')
def home():
	return {'hello':'Hello FastAPI!'}