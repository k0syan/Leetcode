class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        elif len(self.dict) >= self.cap:
            self.dict.popitem(last=False)
        self.dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
