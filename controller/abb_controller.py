from fastapi import APIRouter, HTTPException
from service.abb_service import ABBService
from model.pet import Pet

abb_service = ABBService()
abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.list_pets()

@abb_route.post("/")
async def create_pet(pet: Pet):
    if abb_service.validate_id(pet.id):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    abb_service.add_pet(pet)
    return {"message": "Mascota agregada exitosamente"}

@abb_route.delete("/{pet_id}")
async def delete_pet(pet_id: int):
    if not abb_service.delete_pet(pet_id):
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return {"message": "Mascota eliminada exitosamente"}

@abb_route.put("/")
async def update_pet(pet: Pet):
    if not abb_service.update_pet(pet):
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return {"message": "Mascota actualizada exitosamente"}

@abb_route.get("/by-name/{name}")
async def get_pets_by_name(name: str):
    return abb_service.get_pets_by_name(name)
