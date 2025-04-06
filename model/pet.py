from pydantic import BaseModel, Field

class Pet(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0)