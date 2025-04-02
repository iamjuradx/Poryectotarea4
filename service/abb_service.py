from model.abb import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.abb = ABB()
        self._initialize_data()

    def _initialize_data(self):
        self.abb.add(Pet(id=7, name="Lulu", age=13))
        self.abb.add(Pet(id=2, name="Rocky", age=5))
        self.abb.add(Pet(id=9, name="Bella", age=4))

    def add_pet(self, pet: Pet):
        self.abb.add(pet)

    def delete_pet(self, pet_id: int) -> bool:
        return self.abb.delete(pet_id)

    def update_pet(self, pet: Pet) -> bool:
        return self.abb.update(pet)

    def list_pets(self):
        return self.abb.list_all()

    def get_pets_by_name(self, name: str):
        return self.abb.find_by_name(name)

    def validate_id(self, pet_id: int) -> bool:
        return self.abb.validate_id(pet_id)