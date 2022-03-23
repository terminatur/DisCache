from threading import Lock
from typing import List

from DoublyLinkedListNode import DoublyLinkedListNode

class DoublyLinkedList(object):
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.length = 0
        self.updateLock = Lock()

    def pushBack(self, item) -> DoublyLinkedListNode:
        newNode = None
        with self.updateLock:
            if self.back is None:
                newNode = DoublyLinkedListNode(item)
                self.front = newNode
            else:
                newNode = DoublyLinkedListNode(item, self.back)
                self.back.next = newNode
            
            self.back = newNode
            self.length += 1

        return newNode

    def popFront(self):
        return self.popNFront(1)

    def popNFront(self, n) -> List:
        numToPop = min(n, self.length)

        if numToPop == 0:
            return []

        values = [None] * numToPop
        
        with self.updateLock:
            ptr = self.front
            idx = 0
            while ptr != None and idx < numToPop:
                values[idx] = ptr.value
                ptr = ptr.next
                idx += 1

            self.front = ptr

            if self.length == numToPop:
                self.back = None
            if self.front is not None:
                self.front.prev = None

            self.length -= numToPop

        return values

    def moveToBack(self, node: DoublyLinkedListNode) -> None:
        with self.updateLock:
            # node is first
            # node is last
            # node is middle

            if node.next is None:
                return
            if node.prev is None:
                self.front = node.next
            else:
                prevTemp = node.prev
                node.prev.next = node.next
                node.next.prev = prevTemp

            node.prev = self.back
            node.next = None
            self.back.next = node
            self.back = node

    def __str__(self) -> str:
        ptr = self.front
        result = f"length: {self.length}: "
        while ptr is not None:
            result += f'{ptr.value} -> '
            ptr = ptr.next

        return result


ll = DoublyLinkedList()
ll.pushBack("1")
print(str(ll))
ll.pushBack("2")
ll.pushBack("3")
v4 = ll.pushBack("4")
ll.pushBack("5")
print(str(ll))
ll.popFront()
print(str(ll))
ll.popNFront(2)
print(str(ll))
ll.moveToBack(v4)
print(str(ll))
