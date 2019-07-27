class Node:
    def __init__(self, id, node):
        self.id = id
        self.node = node

    def next(self):
        return self.node

    def __str__(self):
        return str(self.id)


# n = 2
#() -> () -> () -> (X) -> () -> None
def find_nth_node_from_end(node, n):
    if node == None:
        raise(" No valid node object passed")
    second_counter_node = node
    first_counter = 1
    while(node.node != None):
        first_counter +=  1
        if first_counter > n:
            second_counter_node = second_counter_node.node
        node = node.node
    if first_counter < n:
        raise(" Node caanot be returned since node is not accessible")
    return second_counter_node


# 5 4 3 2 1

node1 = Node('node1', None)
node2 = Node('node2', node1)
node3 = Node('node3', node2)
node4 = Node('node4', node3)
node5 = Node('node5', node4)

#print(find_nth_node_from_end(node1, 2) == node2)

def setup():
    node1 = Node('node1', None)
    node2 = Node('node2', node1)
    node3 = Node('node3', node2)
    node4 = Node('node4', node3)
    node5 = Node('node5', node4)
    return [node1,node2,node3,node4,node5]


def fail_safe(func):
    def try_except(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print "True"
    return try_except

@fail_safe
def test_node_not_accessible_at_specified_counter():
    node_list = setup()
    find_nth_node_from_end(node_list[0],2)

@fail_safe
def test_if_empty_list():
    node = None
    find_nth_node_from_end(node, 2)

def test_if_n_is_length_of_list():
    node_list = setup()
    print find_nth_node_from_end(node_list[4],5) == node_list[4]

test_if_n_is_length_of_list()

test_if_empty_list()
test_node_not_accessible_at_specified_counter()
