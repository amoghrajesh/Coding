class MyHashSet:

    def __init__(self):
        self.ds = dict()
        

    def add(self, key: int) -> None:
        if key not in self.ds:
            self.ds[key] = 1
        return
        

    def remove(self, key: int) -> None:
        if key in self.ds:
            self.ds.pop(key)
        return
        

    def contains(self, key: int) -> bool:
        if key in self.ds:
            return True
        return False
        