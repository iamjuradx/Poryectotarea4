from fastapi import APIRouter, HTTPException
from typing import List
from model.pet import Pet
from service.abb_service import PetService
from exception.abb_exceptions import DuplicateIdException, NotFoundException

router = APIRouter(prefix="/pets")
service = PetService()

# 1. CREATE
@router.post("/", response_model=dict)
def create_pet(pet: Pet):
    try:
        service.create_pet(pet)
        return {"message": "Pet added"}
    except DuplicateIdException:
        raise HTTPException(400, "ID already exists")

# 2. LIST ALL
@router.get("/", response_model=List[Pet])
def list_pets():
    return service.list_pets()

# 3. GET BY ID
@router.get("/by-id/{pet_id}", response_model=Pet)
def get_pet(pet_id: int):
    try:
        return service.get_by_id(pet_id)
    except NotFoundException:
        raise HTTPException(404, "Pet not found")

# 4. UPDATE
@router.put("/", response_model=dict)
def update_pet(pet: Pet):
    try:
        service.update_pet(pet)
        return {"message": "Pet updated"}
    except NotFoundException:
        raise HTTPException(404, "Pet not found")

# 5. DELETE
@router.delete("/{pet_id}", response_model=dict)
def delete_pet(pet_id: int):
    try:
        service.delete_pet(pet_id)
        return {"message": "Pet deleted"}
    except NotFoundException:
        raise HTTPException(404, "Pet not found")

# 6. EXISTS
@router.get("/exists/{pet_id}", response_model=dict)
def exists_pet(pet_id: int):
    return {"exists": service.exists(pet_id)}

# 7. TRAVERSAL
@router.get("/traversal/{order}", response_model=List[Pet])
def traversal(order: str):
    try:
        return service.list_traversal(order)
    except ValueError as e:
        raise HTTPException(400, str(e))

# 8. VACCINATED FILTER
@router.get("/vaccinated/{status}", response_model=List[Pet])
def vaccinated(status: bool):
    return service.count_vaccinated(status)

# 9. REPORT BY CITY & GENDER
@router.get("/report", response_model=List[dict])
def report():
    return service.report_by_city_gender()