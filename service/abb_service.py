from model.abb import ABB
from model.pet import Pet
from exception.abb_exceptions import DuplicateIdException, NotFoundException

class ABBService:
    def __init__(self):
        self.abb = ABB()
        self._initialize_data()

    def _initialize_data(self):
        ejemplos = [
            Pet(id=4,  name="Quijada",     age=6),
            Pet(id=5,  name="Castambo",    age=3),
            Pet(id=11, name="Chandoberman",age=8),
            Pet(id=7,  name="Careperro",   age=10),
            Pet(id=2,  name="Carepedal",   age=4),
            Pet(id=9,  name="Perro Viejo", age=12),
        ]
        for pet in ejemplos:
            self.abb.add(pet)

    def create_pet(self, pet: Pet):
        if self.abb.exists(pet.id):
            raise DuplicateIdException()
        self.abb.add(pet)

    def update_pet(self, pet: Pet):
        if not self.abb.update(pet):
            raise NotFoundException()

    def delete_pet(self, pet_id: int):
        if not self.abb.delete(pet_id):
            raise NotFoundException()

    def list_pets(self):
        return self.abb.list_all()

    def get_by_name(self, name: str):
        return self.abb.find_by_name(name)

    def count_by_name(self, name: str) -> int:
        return self.abb.count_by_name(name)

    def exists(self, pet_id: int) -> bool:
        return self.abb.exists(pet_id)