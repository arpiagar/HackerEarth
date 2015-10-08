def bt_to_dll(root):
    if root ==  None:
        return root
    if root.left == None and root.right ==None:
        return root
    
    if root.left != None:
        left  =  bt_to_dll(root.left)
    
    if root.right != None:
        right = bt_to_dll(root.right)
        
    if left != None:
        left.right = root
        if right == None:
            return root
        
    if right != None:
        right.left = root
        return right
        
    
class Node():
    def __init__(self,v):
        self.val = v
        self.left =  None
        self.right = None
    
class Tree():
    def __init__(self):
        self.root =  None
    
    def add_to_tree(self,root,node):
        if root ==  None:
            self.root =  node
            return
        else:
            temp = root
            if  node.val > root.val:
                if root.right != None:
                    self.add_to_tree(root.right,node)
                else:
                    root.right = node
            else:
                if root.left != None:
                    self.add_to_tree(root.left,node)
                else:
                    root.left = node

tree =  Tree()
tree.add_to_tree(tree.root, Node(6))
tree.add_to_tree(tree.root, Node(4))
tree.add_to_tree(tree.root, Node(5))
tree.add_to_tree(tree.root, Node(2))
tree.add_to_tree(tree.root, Node(1))
tree.add_to_tree(tree.root, Node(3))
tree.add_to_tree(tree.root, Node(8))
tree.add_to_tree(tree.root, Node(7))
tree.add_to_tree(tree.root, Node(10))
tree.add_to_tree(tree.root, Node(9))
tree.add_to_tree(tree.root, Node(11))
import pdb;pdb.set_trace()
dll_list =  bt_to_dll(tree.root)
print tree


    