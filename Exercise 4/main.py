from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    nombre:str
    rol:str

usuarios = {
    1: {"nombre": "Tomas", "rol": "Developer"},
    2: {"nombre": "Brais", "rol": "Teacher"}
}

@app.put("/usuarios/{usuario_id}")
def updated_user(usuario_id: int, updated_user: User):
    usuarios.get(usuario_id)["nombre"] = updated_user.nombre
    usuarios.get(usuario_id)["rol"] = updated_user.rol
    return usuarios.get(usuario_id)

@app.delete("/usuarios/{usuario_id}")
def Eliminar(usuario_id: int):
    del usuarios.get(usuario_id)
    return {"mensaje": "Usuario eliminado correctamente"}

    