#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_map = {}
        self.level_sum(root, 1, level_map)
        maxkey = list(level_map.keys())[0]
        maxval =level_map[maxkey]
        return max(level_map, key = level_map.get)
        for k,v in level_map.items():
            if v > maxval:
                maxkey = k
                maxval = v
        return maxkey
    
    def level_sum(self, node, level, level_map):
        if node == None:
            return 
        if level in level_map:
             level_map[level] += node.val
        else:
            level_map[level] = node.val
            
        self.level_sum(node.left, level+1, level_map)
        self.level_sum(node.right, level+1, level_map)
            

