#https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:



class MinHeap:

    def __init__(self, size):
        self.size = size
        self.internal_list = []


    def add(self, value):
        if len(self.internal_list) < self.size:
            self.internal_list.append(value)
        else:
            raise "Cannot add more"


    def heapify(self):
        if len(self.internal_list):
            i = 0
            while (i < len(self.internal_list)):
                temp = self.internal_list[i]
                left, right = 2*i+1 , 2*i+2




