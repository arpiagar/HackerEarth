i#https://leetcode.com/problems/balanced-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedTree(root)


    def isBalancedTree(self, node):
        if not node:
            return True
        if not node.left and not node.right:
            return True
        l_depth = r_depth =0
        l_depth = self.depth(node.left)
        r_depth = self.depth(node.right)
        if abs(l_depth-r_depth) > 1:
            return False
        else:
            return self.isBalancedTree(node.left) and self.isBalancedTree(node.right)

    def depth(self, node):
        if not node :
            return 0
        if not node.left and not node.right:
            return 1
        l_depth = 1+ self.depth(node.left)
        r_depth = 1+ self.depth(node.right)
        return max(l_depth,r_depth)
