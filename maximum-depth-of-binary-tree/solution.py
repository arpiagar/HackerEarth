#https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthTree(root)

    def maxDepthTree(self, node):
        if not node :
            return 0
        if not node.left and not node.right:
            return 1
        max_depth = -1
        if node.left:
            l_depth = 1+self.maxDepthTree(node.left)
            max_depth = max(max_depth, l_depth)
        if node.right:
            r_depth = 1+self.maxDepthTree(node.right)
            max_depth = max(max_depth, r_depth)
        return max_depth
