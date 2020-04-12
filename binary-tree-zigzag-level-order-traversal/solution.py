#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        out = []
        if not root:
            return out
        current_l = [root]
        temp_l = []
        flag = True # left-> right
        while(current_l):
            for elem in current_l:
                if elem:
                    temp_l.append(elem.left)
                    temp_l.append(elem.right)
            if flag:
                val_list = [x.val for x in current_l if x]
            else:
                val_list = [x.val for x in current_l[::-1] if x]
            if val_list:
                out.append(val_list)
            flag = not flag
            current_l = temp_l
            temp_l = []
        return out


