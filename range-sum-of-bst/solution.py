#https://leetcode.com/problems/range-sum-of-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        #            10
        #          5.   15
        #        3   7.    18
        count = 0
        if not root:
            return count
        if L<= root.val <= R:
            count += root.val
        if root.val > L:
            count += self.rangeSumBST(root.left,L,R)
        if root.val < R:
            count += self.rangeSumBST(root.right,L,R)
        return count

