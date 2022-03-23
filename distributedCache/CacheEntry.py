from tokenize import String


from threading import Lock

class CacheEntry(object):
    def __init__(self, value: String, lock=Lock()) -> None:
        self.value = value
        self.lock = lock