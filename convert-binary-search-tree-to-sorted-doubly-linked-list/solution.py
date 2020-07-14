#https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/submissions/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.last = None
        self.head = None
        if not root:
            return root
        self.helper(root)
        self.last.right = self.head
        self.head.left = self.last
        return self.head

    def helper(self,node):
        if not node:
            return
        if node.left:
            self.helper(node.left)
        if self.last:
            self.last.right = node
            node.left = self.last
        else:
            self.head = node
        self.last = node
        if node.right:
            self.helper(node.right)

