from fastapi import FastAPI,HTTPException


app = FastAPI()

usuarios = {
    1: {"nombre": "Tomas", "rol": "Developer"},
    2: {"nombre": "Brais", "rol": "Teacher"}
}

@app.get("/usuarios/{usuario_id}")
def Buscar_ID(usuario_id: int):
    if usuarios.get(usuario_id):
        return usuarios.get(usuario_id)
    raise HTTPException(status_code=404,detail="El elemento solicitado no fue encontrado")
    