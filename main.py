from typing import Optional

from pydantic import BaseModel


from fastapi import FastAPI
from fastapi import Body, Query, Path


app= FastAPI()

class  Location(BaseModel):
    city: str
    state:str
    country: str

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
    Name: Optional[str]= Query(
    None,
    min_length=1,
    max_length=50,
    title="Person Name",
    description="This is the person name"
    ),
    age: str= Query(...,
    title="Person age",
    description="This is the person age, required")
    ):

    return{Name: age }

#validaciones parametros

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(...,gt=0),
    title="ID",
    description="ID_USER"
):
    return{person_id: "It exists"}

@app.put("/person/{person_id}")
def update_person(
    person_id: int =Path(...,
    title="Person ID",
    description="This is the ID",
    gt=0
    ),
    person:Person =Body(...),
    location: Location= Body(...)

):
    result=person.dict()
    result.update(location.dict())
    return result
