class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if(self.head is None):
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    def remove(self, value):

        if(self.head is None):
            return None

        if self.head.data == value:
            self.head = self.head.next
            return

        previous = self.head
        node = self.head.next

        while(node):
            if node.data == value:
                previous.next = node.next
                break
            previous = node
            node = node.next


class LRUCache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError()
        self.capacity = capacity
        self.cache = dict()
        self.priority = Linkedlist()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if(key in self.cache):
            self.priority.remove(key)
            self.priority.enqueue(key)
            return self.cache[key]

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if(self.is_full()):
            removed = self.priority.dequeue()
            self.cache.pop(removed)

        if(key in self.cache):
            self.priority.remove(key)

        self.priority.enqueue(key)
        self.cache[key] = value

    def size(self):
        return len(self.cache)

    def is_full(self):
        return self.size() == self.capacity


if __name__ == '__main__':
    our_cache = LRUCache(5)

    our_cache.set(98, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    # returns -1 because 9 is not present in the cache
    print(our_cache.get(9))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))
