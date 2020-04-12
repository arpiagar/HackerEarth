#https://leetcode.com/problems/symmetric-tree/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        current_list = [root]
        new_list = []
        while current_list:
            for i in range(len(current_list)//2):
                if not current_list[i] and not current_list[len(current_list)-i-1]:
                    continue
                elif not current_list[i] or not current_list[len(current_list)-i-1]:
                    return False
                elif current_list[i].val != current_list[len(current_list)-i-1].val:
                    return False

            for elem in current_list:
                if elem:
                    new_list.append(elem.left)
                    new_list.append(elem.right)
            current_list = new_list
            new_list = []
        return True


    def isSym(self, node, level):
        if not node:
            return
        else:
            pass


