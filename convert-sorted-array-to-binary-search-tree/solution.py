# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from random import randint

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(nums, 0, len(nums)-1)
        
    def convert(self,  nums, left, right):
        if left <= right:
            mid = (left+right)//2 #left + ((right-left)//2)#2
            root = TreeNode(nums[mid])
            root.left = self.convert(nums, left, mid-1)        
            root.right = self.convert(nums, mid+1, right)
            return root

        
