# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def levelOrderTraversal( node, level, level_map):
    if node:
        if level_map.has_key(level):
            level_map[level].append(node.val)
        else:
            level_map[level] = [node.val]
        levelOrderTraversal(node.left, level+1, level_map)
        levelOrderTraversal(node.right, level+1, level_map)
    else:
        return
class Solution(object):
    def levelOrder(self, root):
        level_map = {}
        levelOrderTraversal( root, 0, level_map)
        out = []
        for elem in sorted(level_map.keys()):
            out.append(level_map[elem])
        return out

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
