i#https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root :
            return self.bstCheck(root, -float("inf"), float("inf"))
        else:
            return True
        
        
    def bstCheck(self,node:TreeNode, min_val:float, max_val:float) -> bool:
        if node:
            if min_val < node.val < max_val:
                return self.bstCheck(node.left, min_val, node.val ) and self.bstCheck(node.right, node.val, max_val)
            else:
                return False
        return True
        
        
        
        
   
