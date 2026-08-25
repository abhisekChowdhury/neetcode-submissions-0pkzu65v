class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #connect head and tail
        self.head = Node(0,0)
        self.tail = Node(0,0)

        #there is nothing in between at the moment
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        nxt, prv = node.next, node.prev
        node.next.prev, node.prev.next = prv, nxt
    
    def insert(self, node):
        #insert at rightmost position before our right pointer
        prv = self.tail.prev
        nxt = self.tail
        prv.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prv
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove and delete the least recently used
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]