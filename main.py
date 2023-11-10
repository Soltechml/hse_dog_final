from enum import Enum
from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel
import time

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind=DogType.terrier),
    1: Dog(name='Marli', pk=1, kind=DogType.bulldog),
    2: Dog(name='Snoopy', pk=2, kind=DogType.dalmatian),
    3: Dog(name='Rex', pk=3, kind=DogType.dalmatian),
    4: Dog(name='Pongo', pk=4, kind=DogType.dalmatian),
    5: Dog(name='Tillman', pk=5, kind=DogType.bulldog),
    6: Dog(name='Uga', pk=6, kind=DogType.bulldog)
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return "Welcome to our dog API-service"


@app.post('/post', response_model=Timestamp)
def create_post():
    new_id = max(post_db[-1].id + 1, len(dogs_db))  # Используем максимальный ID из списка post или текущее количество собак
    timestamp = int(time.time())
    new_post = Timestamp(id=new_id, timestamp=timestamp)
    post_db.append(new_post)
    return new_post


@app.get('/dogs/', response_model=list[Dog])
def read_dogs(kind: DogType = Query(None, alias="type")):
    if kind:
        return [dog for dog in dogs_db.values() if dog.kind == kind]
    return list(dogs_db.values())


@app.post('/dogs/', response_model=Dog)
def create_dog(dog: Dog):
    if dog.pk in dogs_db:
        raise HTTPException(status_code=400, detail="Dog with this PK already exists")
    dogs_db[dog.pk] = dog
    return dog


@app.get('/dogs/{pk}', response_model=Dog)
def read_dog(pk: int = Path(...)):
    dog = dogs_db.get(pk)
    if dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dog


@app.patch('/dogs/{pk}', response_model=Dog)
def update_dog(pk: int = Path(...), dog_update: Dog = Body(...)):
    stored_dog_data = dogs_db.get(pk)
    if not stored_dog_data:
        raise HTTPException(status_code=404, detail="Dog not found")
    stored_dog_model = Dog(**stored_dog_data.dict())
    update_data = dog_update.dict(exclude_unset=True)
    updated_dog = stored_dog_model.copy(update=update_data)
    dogs_db[pk] = updated_dog
    return updated_dog

print(dogs_db)