
# libreria de pydantic nos va a permitir crear un modelo de datos
from pydantic import BaseModel
from typing import Optional  # tipo de dato opcional
from fastapi import FastAPI
# libreria de fastapi nos va a permitir crear una ruta
from fastapi import Body, Query


app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    # quiere decir que no existe es una opcion
    hair_color: Optional[str] = None
    # quiere decir que no existe es una opcion
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello": "word"}

# Request and response Body


@app.post("/person/new")
def create_person(person: Person = Body(...)):  # ... es obligatorio
    return person

# validaciones: Query Parameters


@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=3, max_length=50),
    age: str = Query(...),
    hair_color: Optional[str] = None,
    is_married: Optional[bool] = None
):
    return {
        "name": name,
        "age": age,
        "hair_color": hair_color,
        "is_married": is_married
    }
