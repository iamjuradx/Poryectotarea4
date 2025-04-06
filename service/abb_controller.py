from fastapi import APIRouter, HTTPException
from service.abb_service import ABBService
from model.pet import Pet
from config.properties import *
from exception.abb_exceptions import DuplicateIdException, NotFoundException

router = APIRouter(prefix="/abb")
svc = ABBService()

@router.get("/", response_model=list[Pet])
def list_pets():
    return svc.list_pets()

@router.post("/")
def create_pet(pet: Pet):
    try:
        svc.create_pet(pet)
        return {"message": MSG_ADDED}
    except DuplicateIdException:
        raise HTTPException(400, MSG_ID_EXISTS)

@router.put("/")
def update_pet(pet: Pet):
    try:
        svc.update_pet(pet)
        return {"message": MSG_UPDATED}
    except NotFoundException:
        raise HTTPException(404, MSG_NOT_FOUND)

@router.delete("/{pet_id}")
def delete_pet(pet_id: int):
    try:
        svc.delete_pet(pet_id)
        return {"message": MSG_DELETED}
    except NotFoundException:
        raise HTTPException(404, MSG_NOT_FOUND)

@router.get("/by-name/{name}", response_model=list[Pet])
def get_by_name(name: str):
    return svc.get_by_name(name)

@router.get("/count/{name}")
def count_by_name(name: str):
    return {"count": svc.count_by_name(name)}

@router.get("/exists/{pet_id}")
def exists(pet_id: int):
    return {"exists": svc.exists(pet_id)}