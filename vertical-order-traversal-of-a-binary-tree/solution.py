#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_map = {}
        index = 0
        queue = [(root,0, 0)]
        vertical_list = []
        while queue:
            node, index, level = queue.pop(0)
            if node:
                if index in node_map:
                    print(node.val, index, level)
                    if level in node_map[index]:
                        node_map[index][level].append(node.val)
                    else:
                        node_map[index].update({level : [node.val]})
                else:
                    node_map[index] = {level : [node.val]}
                queue.append((node.left,index-1, level+1))
                queue.append((node.right,index+1, level+1))
        for index in sorted(node_map.keys()):
            index_list = []
            for level in sorted(node_map[index].keys()):
                index_list += sorted(node_map[index][level])
            vertical_list.append(index_list)
        return vertical_list


