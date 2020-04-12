#https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderIterative(self, root: TreeNode) -> List[List[int]]:
        out = []
        if not root:
            return out
        curr_l = [root]
        temp_l = []
        while(curr_l):
            for elem in curr_l:
                if elem:
                    temp_l.append(elem.left)
                    temp_l.append(elem.right)
            val_list = [x.val for x in curr_l if x]
            if val_list:
                out.append(val_list)
            curr_l = temp_l
            temp_l = []
        return out


 def levelOrderRecursive(self, root: TreeNode) -> List[List[int]]:
        m_map = {0:[root]}
        if not root:
            return []
        self.levelOrderWithMap(root, 1, m_map)
        out = []
        for key in sorted(m_map.keys()):
            val_list = [x.val for x in m_map[key] if x]
            if val_list:
                out.append(val_list)
        return out

    def levelOrderWithMap(self, node, level,  m_map):
        if not node:
            return
        if level in m_map:
            m_map[level].append(node.left)
            m_map[level].append(node.right)
        else:
            m_map[level] = [node.left, node.right]
        self.levelOrderWithMap(node.left, level+1, m_map)
        self.levelOrderWithMap(node.right, level+1, m_map)

