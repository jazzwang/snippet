from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    status: str

app = FastAPI()

@app.post("/pet/")
async def create_pet(pet: Pet):
    return pet
