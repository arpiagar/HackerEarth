# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Dict
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level_map = {}
        self.traverse_tree(root,0, level_map)
        out = []
        for key in sorted(level_map.keys()):
            out.append(level_map[key])
        return out
    
    def traverse_tree(self, node:TreeNode, level:int, level_map:Dict[str,List[TreeNode]]) -> None:
        if node:
            #if level is for the first time, it is rightmost node
            #since we are traversing right first.
            if level not in level_map:
                level_map[level] = node.val
            #Always travers right node first.
            self.traverse_tree(node.right, level+1, level_map)
            self.traverse_tree(node.left, level+1, level_map)
            
        else:
            return 
