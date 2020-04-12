#https://leetcode.com/problems/merge-two-binary-trees/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left , t2.left)
            node.right = self.mergeTrees(t1.right , t2.right)
            return node
        if not t1 and not t2:
            return
        if not t1:
            node = TreeNode(t2.val)
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)
            return node
        if not t2:
            node = TreeNode(t1.val)
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
            return node

