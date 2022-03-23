from typing import List
from DoublyLinkedList.HashedDoublyLinkedList import HashedDoublyLinkedList

class LRUEvictionStrategy(object):
    def __init__(self) -> None:
        self.hashedLinkedList = HashedDoublyLinkedList()

    def hit(self, key) -> None:
        self.hashedLinkedList.

    def insert(self, key) -> None:
        self.hashedLinkedList.pushBack(key)

    def evict(self, num) -> List[str]:
        pass
    