class MyHashSet:

    def __init__(self):
        self.hash_set = []
        

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.hash_set.append(key)
        

    def remove(self, key: int) -> None:
        try:
            b = self.hash_set.index(key)
            del self.hash_set[b]
        except:
            pass
        

    def contains(self, key: int) -> bool:
        for i in self.hash_set:
            if key == i:
                return True
            
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)