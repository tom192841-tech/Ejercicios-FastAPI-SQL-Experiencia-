from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Hola_de_Raiz():
    return {"mensaje": "¡Hola Mundo desde mi API!"}

@app.get("/saludo/{nombre}")
async def Saludo_con_Ruta(nombre: str):
    return{"saludo": f"Hola, {nombre}, bienvenido al backend"}
    
    