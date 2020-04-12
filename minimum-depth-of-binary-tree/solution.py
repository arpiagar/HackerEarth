#https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.minDepthTree(root)

    def minDepthTree(self, node):
        if not node :
            return 0
        if not node.left and not node.right:
            return 1
        min_depth = float('inf')
        if node.left:
            l_depth = 1+self.minDepthTree(node.left)
            min_depth = min(min_depth, l_depth)
        if node.right:
            r_depth = 1+self.minDepthTree(node.right)
            min_depth = min(min_depth, r_depth)
        return min_depth
