from fastapi import FastAPI


app = FastAPI()

videojuegos = ["Godot Quest", "Python Strike", "FastAPI Runner", "Cyber Code"]
@app.get("/buscar")
async def  Videojuegos():
    return videojuegos
@app.get("/buscar/")
async def buscar_videojuegos(limite: int):
    juegos_a_mostrar = [game for index,game in enumerate(videojuegos) if not index >= limite ]
    return juegos_a_mostrar