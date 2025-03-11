from pydantic import BaseModel, Field


class ModelVehiculo(BaseModel):
    modelo: str = Field(..., min_length=4, max_length=25, description="Modelo del vehículo.")
    anio: int = Field(..., ge=1900, le=2026, description="Año del vehículo entre 1900 y 2026.")
    placa: str = Field(..., min_length=6, max_length=10, pattern="^[A-Z0-9]+$", description="Placa del vehículo (sólo mayúsculas y números).")
