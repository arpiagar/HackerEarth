#https://leetcode.com/problems/subtree-of-another-tree/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and t:
            return False
        if s and not t:
            return False
        out = []
        node = self.findNode(s,t, out)

        if not out:
            return False
        flag = False
        for node in out:
            flag= flag or self.compareTree(node, t)
        return flag

    def findNode(self, t,s, out):
        if not t:
            return
        if t.val == s.val:
            out.append(t)
        left = self.findNode(t.left,s, out)
        right = self.findNode(t.right,s, out)


    def compareTree(self, s, t):
        if not s and not t:
            return True
        if not s and t:
            return False
        if not t and s:
            return False
        if s.val == t.val:
            return self.compareTree(s.left,t.left) and self.compareTree(s.right,t.right)
        return False
