from datetime import datetime


class EvictionNode(object):
    def __init__(self, key) -> None:
        self.key = key
        self.insertTime = datetime.utcnow
        self.lastHitTime = datetime.utcnow