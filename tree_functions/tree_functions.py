#WAP tp find a tree is a BST or not

import sys

class Node:
    def __init__(self, value):
        self.value =  value
        self.left =  None
        self.right =  None

class BST:
    def __init__(self):
        self.root = None


    def is_bst_util(self, node, min_value, max_value):
      if node == None:
        return True
      if (node.value < min_value or node.value > max_value):
        return False
      return self.is_bst_util(node.left, min_value, node.value-1) and self.is_bst_util(node.right, node.value+1, max_value)
  

    def is_bst(self, root):
      return self.is_bst_util(self.root, sys.maxint*-1, sys.maxint)

    def insert(self,root,node):
        if self.root == None:
            self.root =  node
            return 
        elif root.value > node.value:
            if root.left == None:
                root.left = node
                return
            else:
                return self.insert(root.left,node)
        elif  root.value < node.value:
            if root.right == None:
                root.right =  node
                return 
            else:
                return self.insert(root.right, node)

    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print root.value
            self.inorder(root.right)
        else:
            return 


if __name__=='__main__':
    bst =  BST()
    bst.insert(bst.root, Node(10))
    bst.insert(bst.root, Node(5))
    bst.insert(bst.root, Node(15))
    bst.insert(bst.root, Node(7))
    bst.insert(bst.root, Node(9))
    bst.insert(bst.root, Node(13))
    bst.insert(bst.root, Node(17))
    #import pdb;pdb.set_trace()
    #print bst.inorder(bst.root)
    print bst.is_bst(bst.root)

