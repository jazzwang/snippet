from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import random

class Pet(BaseModel):
    id: int
    name: str
    status: str

app = FastAPI()

@app.post("/pet")
async def create_pet(pet: Pet):
    if pet.id == 0:
        pet.id = random.randint(10^9, 10^10-1)
        return pet
    else:
        raise HTTPException(status_code=405)