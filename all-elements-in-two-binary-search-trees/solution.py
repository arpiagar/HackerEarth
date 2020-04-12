#https://leetcode.com/problems/all-elements-in-two-binary-search-trees/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        node_map = defaultdict(int)
        node_map = self.parseTree(root1, node_map)
        node_map = self.parseTree(root2, node_map)
        out = []
        for elem in sorted(node_map.keys()):
            count = node_map[elem]
            for i in range(0, count):
                out.append(elem)
        return out
    
    def parseTree(self, root, node_map) :
        if not root:
            return node_map
        node_map[root.val] += 1
        node_map = self.parseTree(root.left, node_map)
        return self.parseTree(root.right, node_map)
