i#https://leetcode.com/problems/cousins-in-binary-tree/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        q = [root]
        while q :
            flag = False
            new_q = []
            for elem in q:
                if elem:
                    new_q.append(elem.left)
                    new_q.append(elem.right)
                    if elem.left and elem.right and ((elem.left.val == x and elem.right.val ==y) or (elem.left.val == y and elem.right.val ==x)):
                        return False
            flag = any([k.val==x for k in new_q if k]) and any([k.val==y for k in new_q if k])
            if flag:
                return True
            q = new_q
        return False
