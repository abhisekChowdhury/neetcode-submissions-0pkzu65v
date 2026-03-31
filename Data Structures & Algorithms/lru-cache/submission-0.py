# create Node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # define dictionary
        self.cache = {}

        # define size = capacity
        self.size = 0
        self.capacity = capacity

        # define two dummy nodes and connect them - head and tail
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        # if key doesn't exist, return -1
        if key not in self.cache:
            return -1
        else:
            # get the node from the cache
            node = self.cache[key]
            # remove node from linkedlist
            self.remove(node)
            # move it to the front of the linkedlist
            self.move_to_front(node)
            # return the value of the node
            return node.value

    def put(self, key: int, value: int) -> None:
        # if key doesn't exist, create new node and insert in front of head
        if key not in self.cache:
            # create node
            node = Node(key, value)
            # store node in dictionary
            self.cache[key] = node
            # put in front of head
            self.move_to_front(node)
            # increase size
            self.size += 1
        else:
            # get the node
            node = self.cache[key]
            # remove node from its position in linkedlist
            self.remove(node)
            # update value of node
            node.value = value
            # move in front of head
            self.move_to_front(node)

        # check size constraint
        if self.size > self.capacity:
            # remove least recently used node
            lru = self.tail.prev
            self.remove(lru)
            # decrease size
            self.size -= 1
            # delete key from cache
            del self.cache[lru.key]

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def move_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

            
            

        
