class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)