from model.pet import Pet

class ABB:
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if self.root is None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def delete(self, pet_id: int):
        self.root, deleted = self._delete(self.root, pet_id)
        return deleted

    def _delete(self, node, pet_id: int):
        if node is None:
            return node, False
        if pet_id < node.pet.id:
            node.left, deleted = self._delete(node.left, pet_id)
        elif pet_id > node.pet.id:
            node.right, deleted = self._delete(node.right, pet_id)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            min_larger_node = self._get_min(node.right)
            node.pet = min_larger_node.pet
            node.right, _ = self._delete(node.right, min_larger_node.pet.id)
            return node, True
        return node, deleted

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def update(self, pet: Pet):
        node = self._search(self.root, pet.id)
        if node:
            node.pet = pet
            return True
        return False

    def _search(self, node, pet_id: int):
        if node is None or node.pet.id == pet_id:
            return node
        if pet_id < node.pet.id:
            return self._search(node.left, pet_id)
        return self._search(node.right, pet_id)

    def list_all(self):
        pets = []
        self._inorder_traversal(self.root, pets)
        return pets

    def _inorder_traversal(self, node, pets):
        if node:
            self._inorder_traversal(node.left, pets)
            pets.append(node.pet)
            self._inorder_traversal(node.right, pets)

    def find_by_name(self, name: str):
        result = []
        self._search_by_name(self.root, name.lower(), result)
        return result

    def _search_by_name(self, node, name: str, result: list):
        if node:
            if node.pet.name.lower() == name:
                result.append(node.pet)
            self._search_by_name(node.left, name, result)
            self._search_by_name(node.right, name, result)

    def validate_id(self, pet_id: int):
        return self._search(self.root, pet_id) is not None

class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet: Pet):
        if pet.id < self.pet.id:
            if self.left:
                self.left.add(pet)
            else:
                self.left = NodeABB(pet)
        elif pet.id > self.pet.id:
            if self.right:
                self.right.add(pet)
            else:
                self.right = NodeABB(pet)
        self.size += 1
