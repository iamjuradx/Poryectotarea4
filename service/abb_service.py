from model.pet import Pet
from exception.abb_exceptions import DuplicateIdException, NotFoundException

class PetService:
    def __init__(self):
        self.pets: list[Pet] = []
        # Semilla de datos con 'age' incluido
        example_pets = [
            Pet(id=1, name="Careperro",    type="Dog",    gender="M", vaccinated=True,  city="Manizales", age=7),
            Pet(id=2, name="Quijada",      type="Dog",    gender="F", vaccinated=False, city="Manizales", age=5),
            Pet(id=3, name="Mateo",        type="Cat",    gender="M", vaccinated=True,  city="Manizales", age=3),
            Pet(id=4, name="Perro Viejo",  type="Dog",    gender="M", vaccinated=False, city="Manizales", age=12),
            Pet(id=5, name="Peluca Vieja", type="Cat",    gender="F", vaccinated=True,  city="Manizales", age=9),
            Pet(id=6, name="Castambo",     type="Bird",   gender="M", vaccinated=False, city="Manizales", age=2),
        ]
        for pet in example_pets:
            self.pets.append(pet)

    def create_pet(self, pet: Pet):
        if any(p.id == pet.id for p in self.pets):
            raise DuplicateIdException()
        self.pets.append(pet)

    def list_pets(self) -> list[Pet]:
        return self.pets

    def get_by_id(self, pet_id: int) -> Pet:
        for p in self.pets:
            if p.id == pet_id:
                return p
        raise NotFoundException()

    def update_pet(self, pet: Pet):
        for idx, p in enumerate(self.pets):
            if p.id == pet.id:
                self.pets[idx] = pet
                return
        raise NotFoundException()

    def delete_pet(self, pet_id: int):
        for p in self.pets:
            if p.id == pet_id:
                self.pets.remove(p)
                return
        raise NotFoundException()

    def exists(self, pet_id: int) -> bool:
        return any(p.id == pet_id for p in self.pets)

    def list_traversal(self, order: str) -> list[Pet]:
        if order == "inorder":
            return sorted(self.pets, key=lambda p: p.id)
        if order == "preorder":
            return sorted(self.pets, key=lambda p: p.name)
        if order == "postorder":
            return sorted(self.pets, key=lambda p: p.age)
        raise ValueError("Invalid order")

    def count_vaccinated(self, status: bool) -> list[Pet]:
        return [p for p in self.pets if p.vaccinated == status]

    def report_by_city_gender(self) -> list[dict]:
        report = {}
        for p in self.pets:
            key = (p.city, p.gender)
            report[key] = report.get(key, 0) + 1
        return [{"city": c, "gender": g, "count": cnt} for (c, g), cnt in report.items()]