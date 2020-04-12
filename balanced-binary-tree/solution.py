#https://leetcode.com/problems/balanced-binary-tree/solution/



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
        if self.isBalancedTree(node.left):
            l_depth = self.depth(node.left)
        else:
            return False
        if self.isBalancedTree(node.right):
            r_depth = self.depth(node.right)
        else:
            return False
        if abs(l_depth-r_depth) <= 1:
            return True
        return False

    def depth(self, node):
        if not node :
            return 0
        if not node.left and not node.right:
            return 1
        l_depth = 1+ self.depth(node.left)
        r_depth = 1+ self.depth(node.right)
        return max(l_depth,r_depth)
