#  Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
#Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 
#
#We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
#
# 
#
#Example 1:
#
#
#
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
#Output: true
#Explanation: 
#The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
#Other valid sequences are: 
#0 -> 1 -> 1 -> 0 
#0 -> 0 -> 0
#Example 2:
#
#
#
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
#Output: false 
#Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
#Example 3:
#
#
#
#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
#Output: false
#Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
# 
#
#Constraints:
#
#1 <= arr.length <= 5000
#0 <= arr[i] <= 9
#Each node's value is between [0 - 9].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.isValidSequenceUtil(root, arr)

    def isValidSequenceUtil(self, root: TreeNode, rem_arr: List[int]) -> bool:
        flag = False
        if not root.left and not root.right: # Leaf node
            if len(rem_arr) == 1:
                if rem_arr[0] == root.val:
                    return True
            return False
        else: #Non leeaf node
            if not rem_arr:
                return False
            if root.val != rem_arr[0]:
                return False
            if root.left:
                flag = flag or self.isValidSequenceUtil(root.left, [x for x in rem_arr[1:]])
            if root.right:
                flag = flag or self.isValidSequenceUtil(root.right, [x for x in rem_arr[1:]])
        return flag
