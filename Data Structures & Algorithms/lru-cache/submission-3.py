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

        # create a head and a tail node and connect them
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.bring_to_front(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.bring_to_front(node)
            self.cache[key] = node
            self.size += 1
        else:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.bring_to_front(node)

        if self.size > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            self.size -= 1
            del self.cache[lru.key]

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def bring_to_front(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
            
