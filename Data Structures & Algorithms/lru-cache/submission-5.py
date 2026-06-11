class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}

        self.size = 0
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # get the node first from the cache
            node = self.cache[key]

            #remove from current position and move to front as most recently used (The attempt before this is incorrect)
            self.remove(node)
            self.move_to_front(node)

            #return the value of the node
            return node.value

    def put(self, key: int, value: int) -> None:
        #create new node if key does not exist in cache
        if key not in self.cache:
            node = Node(key,value)
            self.cache[key] = node

            #put in front since this is the most recent
            self.move_to_front(node)
            
            #increase size
            self.size+=1
        else:
            #get the node
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.move_to_front(node)
        
        if self.size > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            self.size -= 1
            del self.cache[lru.key]
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_front(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
