class MyHashSet:

    def __init__(self):
        self.hset = ()

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hset = self.hset + (key,)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hset = list(self.hset)
            self.hset.remove(key)
            self.hset = tuple(self.hset)

    def contains(self, key: int) -> bool:
        if key in self.hset:
            return True
        else:
            return False