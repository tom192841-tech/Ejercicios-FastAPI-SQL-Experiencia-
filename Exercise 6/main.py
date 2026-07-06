from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Habilidad(BaseModel):
    nombre: str
    nivel: int
    
class PerfilProgramador(BaseModel):
    nombre: str
    lenguaje_principal: str
    habilidades: List[Habilidad]
    
@app.post("/perfil")
def Agregar_perfil(perfil:PerfilProgramador):
    Habilidades = [hab for hab in perfil.habilidades]
    return {"Habilidades deL usuario": Habilidades}
    