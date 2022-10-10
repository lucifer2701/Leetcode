class MyHashMap:

    def __init__(self):
        self.hash_keys=[]
        self.hash_values=[]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_keys:
            j=self.hash_keys.index(key)
            self.hash_values[j]=value
        else:
            self.hash_keys.append(key)
            self.hash_values.append(value)

    def get(self, key: int) -> int:
        try:
            j=self.hash_keys.index(key)
            return self.hash_values[j]
        except:
            return -1

    def remove(self, key: int) -> None:
        try:
            j=self.hash_keys.index(key)
            self.hash_keys.pop(j)
            self.hash_values.pop(j)
        except:
            pass
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)