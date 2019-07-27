#From a binary tree, return all nodes which are visible (value greater than that of all its ancestors.)

class Node:
    def __init__(self, value):
        self.value = value
        self.left =  None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, root, value):
        if self.root == None:
            self.root = Node(value)
            return self.root
        if root == None:
            root = Node(value)
            return self.root
        else:
            if root.left == None:
                root.left = Node(value)
                return self.root
            else:
                if root.right == None:
                    root.right = Node(value)
                    return self.root
                else:
                    return self.add(root.left, value)



def recurse_and_print_greater_than_ancestors( root, output, maximum):
    if root == None:
        return
    else:
        curr_value = root.value
        if root.value > maximum:
            output.append(root)
            recurse_and_print_greater_than_ancestors(root.left, output, root.value)
            recurse_and_print_greater_than_ancestors(root.right, output, root.value)
        else:
            recurse_and_print_greater_than_ancestors(root.left, output, maximum)
            recurse_and_print_greater_than_ancestors(root.right, output, maximum)
    return

if __name__ == "__main__":
    tree  = BinaryTree()
    input_array = [2,4,5,66,3,44,12,56]


    for value in input_array:
        root = tree.add(tree.root , value)
    output = []
    if root != None:
        import pdb;pdb.set_trace()
        recurse_and_print_greater_than_ancestors(root, output, root.value)

