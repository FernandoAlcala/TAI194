from pydantic import BaseModel, Field, EmailStr


class modelUsuario(BaseModel):
    name: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios.")
    age: int = Field(..., gt=0, le=120, description="Edad entre 1 y 120 años.")
    email: str = Field(..., pattern=r'^[a-z0-9]+[\._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$', description="Correo válido.")

class modelAuth(BaseModel):
    mail: EmailStr
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña es de mínimo 8 caracteres, sólo letras sin espacios")