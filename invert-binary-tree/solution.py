#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        flag = True
        q = [root]
        while q:
            new_q = []
            for elem in q:
                temp = elem.left
                elem.left = elem.right
                elem.right = temp
                if elem.left:
                    new_q.append(elem.left)
                if elem.right:
                    new_q.append(elem.right)
            q = new_q
        return root
