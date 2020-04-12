#https://leetcode.com/problems/closest-binary-search-tree-value/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closestVal = root.val
        offset = abs(target-root.val)
        closestVal, offset = self.cv(root, target, offset, closestVal)
        return closestVal

    def cv(self, node, target, offset, closestVal):
        if not node:
            return closestVal, offset
        if node.val == target:
            return node.val, 0
        if abs(node.val-target) < offset:
            offset = abs(node.val-target)
            closestVal = node.val
        if node.val > target:
            return self.cv(node.left, target, offset, closestVal)
        else:
            return self.cv(node.right, target, offset, closestVal)
