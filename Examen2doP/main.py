from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import ModelVehiculo

app = FastAPI(
	title="Registro de Vehículos",
	description="Fernando López Alcalá",
	version="1.0.1"
)

vehículos=[
    {"modelo":"Chevrolet", "anio":2021, "placa":"ABC123"},
    {"modelo":"Ford", "anio":2019, "placa":"DEF456"},
    {"modelo":"Nissan", "anio":2020, "placa":"GHI789"},
    {"modelo":"Toyota", "anio":2021, "placa":"JKL012"},
    {"modelo":"Volkswagen", "anio":2018, "placa":"MNO345"},
]

# EndPoint POST
@app.post('/vehiculos/', response_model=ModelVehiculo, tags=['Operaciones CRUD'])
def guardar(vehiculo: ModelVehiculo):
    for vhl in vehículos:
        if vhl["placa"] == vehiculo.placa:
            raise HTTPException(status_code=400, detail="El vehículo ya existe")
    vehículos.append(vehiculo.dict())
    return vehiculo

# EndPoint CONSULTA POR PLACA
@app.get("/placa/{placa}", tags=["Operaciones CRUD"])
def buscar_por_placa(placa: str):
    for vehiculo in vehículos:
        if vehiculo["placa"] == placa:
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")