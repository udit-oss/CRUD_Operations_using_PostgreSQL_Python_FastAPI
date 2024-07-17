from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

# Creating instance of the application
app = FastAPI()  
db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class PersonOut(OurBaseModel):
    id: int
    first_name: str
    last_name: str
    is_Male: bool

@app.get('/', response_model=list[PersonOut], status_code=status.HTTP_200_OK)
async def getAll_Persons():
    getAllPersons = db.query(models.Person).all()
    return getAllPersons

@app.get('/getbyID/{person_id}', response_model=PersonOut, status_code=status.HTTP_200_OK)
async def getBy_ID(person_id:int):
    getByID = db.query(models.Person).filter(models.Person.id == person_id).first()
    if getByID is not None:
        return getByID
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")  

@app.post('/addperson', response_model=PersonOut, status_code=status.HTTP_200_OK)
def addPerson(person:PersonOut):
    newPerson = models.Person(
        id = person.id,
        first_name = person.first_name,
        last_name = person.last_name,
        is_Male = person.is_Male
    )
    find_person = db.query(models.Person).filter(models.Person.id == person.id).first()
    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Person with this ID already exists")

    db.add(newPerson)
    db.commit()
    return newPerson

@app.put('/update_person/{person_id}', response_model=PersonOut, status_code=status.HTTP_202_ACCEPTED)
def updatePerson(person_id:int, person:PersonOut):
    find_person  = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is not None:
        find_person.id = person.id
        find_person.first_name = person.first_name
        find_person.last_name = person.last_name
        find_person.is_Male = person.is_Male
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person with this ID does not exists")
    db.commit()
    return find_person

@app.delete('/delete_person/{person_id}', response_model=PersonOut, status_code=200)
def deletePerson(person_id:int):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()

    if find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person with this id is already deleted or doesn't exist")




# @app.get('/', response_model=list[Person])
# async def getAll_Persons():
#     getAllPersons = db.query(models.Person).all()
#     return getAll_Persons()

# @app.get("/", status_code=200)
# async def getCar_Info():
#     return {"message": "server is running"} 

# @app.get("/getPersonbyID/{person_id}", status_code=200)
# async def getPerson_by_ID(person_id: int):
#     return {"message" : f"The ID of this person is {person_id}"}

# @app.post("/addPersonInfo", status_code=200)
# async def addPerson_Info(person: Person_data):
#     return{
#         "id": person.id,
#         "first_name" : person.first_name,
#         "last_name" : person.last_name,
#         "is_Male" : person.is_Male
#     }
