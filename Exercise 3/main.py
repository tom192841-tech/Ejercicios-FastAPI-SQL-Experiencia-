from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemInventario(BaseModel):
    nombre:str
    cantidad:int
    precio:float
    
@app.post("/Items")
def Agregar_Item(Item: ItemInventario):
    return {"precio": str(Item.cantidad * Item.precio)}

