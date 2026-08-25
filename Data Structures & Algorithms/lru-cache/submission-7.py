class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recent = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.recent.remove(key)
            self.recent.append(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.recent.remove(key)
        
        self.cache[key] = value
        self.recent.append(key)
        
        if len(self.cache) > self.capacity:
            del self.cache[self.recent[0]]
            self.recent.pop(0)
        

        
