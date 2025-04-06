from typing import Optional, List
from model.pet import Pet

class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left: Optional[NodeABB] = None
        self.right: Optional[NodeABB] = None
        self.size = 1

    def add(self, pet: Pet):
        if pet.id < self.pet.id:
            if self.left: self.left.add(pet)
            else: self.left = NodeABB(pet)
        elif pet.id > self.pet.id:
            if self.right: self.right.add(pet)
            else: self.right = NodeABB(pet)
        self.size += 1

class ABB:
    def __init__(self):
        self.root: Optional[NodeABB] = None

    def add(self, pet: Pet):
        if not self.root: self.root = NodeABB(pet)
        else: self.root.add(pet)

    def _get_min(self, node: NodeABB) -> NodeABB:
        while node.left: node = node.left
        return node

    def _delete(self, node: Optional[NodeABB], pet_id: int) -> (Optional[NodeABB], bool):
        if not node: return None, False
        if pet_id < node.pet.id:
            node.left, deleted = self._delete(node.left, pet_id)
        elif pet_id > node.pet.id:
            node.right, deleted = self._delete(node.right, pet_id)
        else:
            if not node.left: return node.right, True
            if not node.right: return node.left, True
            successor = self._get_min(node.right)
            node.pet = successor.pet
            node.right, _ = self._delete(node.right, successor.pet.id)
            return node, True
        return node, deleted

    def delete(self, pet_id: int) -> bool:
        self.root, deleted = self._delete(self.root, pet_id)
        return deleted

    def _search(self, node: Optional[NodeABB], pet_id: int) -> Optional[NodeABB]:
        if not node or node.pet.id == pet_id: return node
        if pet_id < node.pet.id: return self._search(node.left, pet_id)
        return self._search(node.right, pet_id)

    def update(self, pet: Pet) -> bool:
        node = self._search(self.root, pet.id)
        if not node: return False
        node.pet = pet
        return True

    def list_all(self) -> List[Pet]:
        out: List[Pet] = []
        def inorder(n: Optional[NodeABB]):
            if not n: return
            inorder(n.left); out.append(n.pet); inorder(n.right)
        inorder(self.root)
        return out

    def find_by_name(self, name: str) -> List[Pet]:
        out: List[Pet] = []
        def dfs(n: Optional[NodeABB]):
            if not n: return
            if n.pet.name.lower() == name.lower(): out.append(n.pet)
            dfs(n.left); dfs(n.right)
        dfs(self.root)
        return out

    def exists(self, pet_id: int) -> bool:
        return self._search(self.root, pet_id) is not None

    def count_by_name(self, name: str) -> int:
        return len(self.find_by_name(name))