#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list=[]
        q_list=[]
        self.find(root, p, p_list)
        self.find(root, q, q_list)
        min_len = min(len(p_list), len(q_list))
        p_list = p_list[::-1]
        q_list = q_list[::-1]

        if not min_len:
            return None
        if p_list[0] != q_list[0]:
            return None
        else:
            last = p_list[0]
        for i in range(1, min_len):
            if p_list[i] != q_list[i]:
                return last
            else:
                last = p_list[i]

        return last


    def find(self, node, p, path_list):
        if node == None:
            return False
        if node == p:
            path_list.append(p)
            return True
        if (self.find(node.left, p, path_list)  or self.find(node.right, p, path_list)):
            path_list.append(node)
            return True
        else:
            return False

