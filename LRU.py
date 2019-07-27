def opertion(key):
    # does something long
    return db.retrieve(key)

#LRU cache
#get would return least recently used , also update the timestamp of the entry
#put would add an entry /update the timestamp an existing entry with current timestamp
# hashmap[key]=  ref to node
# DLL  node1 ->
#node
class Node:
    def __init__(self, k,v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.start = None
        self.end = None

    def add_to_linked_list(self, node):
        if self.start == None:
            self.start = node
            self.end = node
        else:
            current_end = self.end
            current_end.next = node
            node.prev = current_end
            self.end = node


    def remove_from_linked_list(self):
        if self.start == None:
            raise Exception("List empty")
        else:
            node = self.start
            self.start = self.start.next
        return node

    def remove_a_node(self, node):
        if self.start != self.end:
            if node == self.start:
                self.start = node.next
                node.next.prev = None
                node.next = node.prev =None

            if node == self.end:
                self.end = self.end.prev
                node.prev.next = None
                node.next = node.prev =None

            else:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
        else:
            self.start = self.end = None
        node.next = node.prev =None




class Cache:

    def __init__ (self, capacity, operation):
        self.capacity = capacity
        self.operation = operation
        self.map = {}
        self.dll = DLL()
        self.current_capacity = 0

    def get(self, key):
        if self.map.has_key(key):
            node = self.map[key]
            self.dll.remove_a_node(node)
            seld.dll.add_to_linked_list(node)
            return node.value
        else:
            value = self.operation(key)
            self.put(key, value)
            return value

    def put(self, key, value):
        if self.map.has_key(key):
            node = self.map[key]
            node.value = value
            self.dll.remove_a_node(node)
            seld.dll.add_to_linked_list(node)
        else:
            node = Node(key, value)
            self.map[key] =  node
            if self.current_capacity == self.capacity:
                self.dll.remove_from_linked_list()
                self.dll.add_to_linked_list(node)

            else:
                self.dll.add_to_linked_list(node)
                self.current_capacity += 1



