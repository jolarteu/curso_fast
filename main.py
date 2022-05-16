from typing import Optional

from pydantic import BaseModel


from fastapi import FastAPI
from fastapi import Body
from fastapi import Query


app= FastAPI()


class  Person(BaseModel):
    first_name:str
    last_name:str
    age:str
    hair_color: Optional[str]=None
    is_married: Optional[bool]=None

@app.get("/")
def home():
    return{"hello": "Wolrd"}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

#validaciones

@app.get("/person/detail")
def show_person(
    Name: Optional[str]= Query(None, min_length=1, max_length=50),
    age: str= Query(...)
    ):

    return{name: age}
