from threading import Lock
from typing import Dict
from DoublyLinkedList import DoublyLinkedList
from DoublyLinkedListNode import DoublyLinkedListNode
from HashedListNode import HashedListNode


class HashedDoublyLinkedList(object):
    def __init__(self) -> None:
        self.keyToNodeMap: Dict[str, DoublyLinkedListNode] = {}
        self.linkedList = DoublyLinkedList()
        self.insertLock = Lock()

    def contains(self, key: str) -> bool:
        return key in self.keyToNodeMap

    def get(self, key: str):
        return self.keyToNodeMap[key].value

    def pushBack(self, key: str, value) -> None:
        with self.insertLock:
            if not self.contains(key):
                hashedNode = HashedListNode(key, value)
                node = self.linkedList.pushBack(hashedNode)
                self.keyToNodeMap[key] = node

    def remove(self, key: str) -> None:
        node = self.keyToNodeMap[key]
        self.linkedList.remove(node)
        self.keyToNodeMap.pop(key)

    def popNFront(self, num: int) -> list:
        hashedNodes = self.linkedList.popNFront(num)

        for n in hashedNodes:
            self.keyToNodeMap.pop(n.key)

        keys = map(lambda x: x.value, hashedNodes)

        return keys

    def moveToBack(self, key) -> None:
        node = self.keyToNodeMap[key]
        self.linkedList.moveToBack(node)

    def __str__(self) -> str:
        ptr = self.linkedList.front
        result = f"length: {self.linkedList.length}:  "
        while ptr is not None:
            result += f'{ptr.value.key} -> '
            ptr = ptr.next

        result += "None"
        return result



# print("Starting")
# hl = HashedDoublyLinkedList()
# hl.pushBack("1", "1abc")
# hl.pushBack("2", "2def")
# hl.pushBack("3", "3hij")
# hl.pushBack("4", "4klm")
# print(hl)

# print("Remove 3")
# hl.remove("3")
# print(hl)

# print("Move 2 to back")
# hl.moveToBack("2")
# print(hl)

# print("Pop front 2")
# hl.popNFront(2)
# print(hl)

# print("Pop last 1")
# hl.popNFront(1)
# print(hl)

# hl.popNFront(1)

# print(hl.keyToNodeMap)