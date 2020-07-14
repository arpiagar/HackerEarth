i#https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        node_map = {}
        self.smaller(root, node_map)
        return self.findKSmall(root, node_map, k)


    def findKSmall(self, node, node_map, k):
        if node_map[node]["left"] == k-1:
            return node.val
        if node_map[node]["left"] >= k:
            return self.findKSmall(node.left, node_map, k)
        offset = node_map[node]["left"]+1
        remaining = k-offset
        return self.findKSmall(node.right, node_map, remaining)


    def smaller(self, node , node_map):
        if node not in node_map: #{3 :{l:2, r:1}, 1 :{l:0, r:1}, 2 :{l:0, r:0}, 4 :{l:0, r:0}}}}
                node_map[node] = {"left":0 , "right": 0}
        if node.left:
            self.smaller(node.left, node_map)
            node_map[node]["left"] = 1 + node_map[node.left]["left"] + node_map[node.left]["right"]
        if node.right:
            self.smaller(node.right, node_map)
            node_map[node]["right"] = 1 + node_map[node.right]["left"] + node_map[node.right]["right"]

