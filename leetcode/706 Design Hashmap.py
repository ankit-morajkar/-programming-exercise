class MyHashMap:

    def __init__(self):
        self.hash_map = []
        

    def put(self, key: int, value: int) -> None:
        key_present = False
        for pair in self.hash_map:
            if key == pair[0]:
                key_present = True
                pair[1] = value
                
        if key_present == False:
            self.hash_map.append([key, value])
                
        

    def get(self, key: int) -> int:
        for pair in self.hash_map:
            if pair[0] == key:
                return pair[1]
            
        return -1
        
    def remove(self, key: int) -> None:
        key_present = False
        for i in range(len(self.hash_map)):
            if self.hash_map[i][0] == key:
                key_present = True
                break
                
        if key_present:
            del self.hash_map[i]
                
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)