#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        out = []
        if not root:
            return out
        current_l = [root]
        temp_l = []

        while current_l:
            for elem in current_l:
                if elem : # ignore null node
                    temp_l.append(elem.left)
                    temp_l.append(elem.right)
            val_list = [x.val for x in current_l if x] #only non null nodes
            if val_list:
                out.append(val_list)
            current_l = temp_l
            temp_l=[]
        return out[::-1]
