from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    age: int
    vaccinated: bool
    gender: str
    city: str