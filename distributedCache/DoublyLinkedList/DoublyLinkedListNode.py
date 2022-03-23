class DoublyLinkedListNode(object):
    __spec__ = 'value', 'prev', 'next'

    def __init__(self, value, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next