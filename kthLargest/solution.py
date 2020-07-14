#https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class MinHeap:
        def __init__(self, capacity):
            self.capacity = capacity
            self.heap = []
            self.count = 0

        def heappush(self, value):
            if self.count < self.capacity:
                self.heap.append(value)
                self.count += 1
                i = self.count-1
                while(i != 0):
                    parent = i//2
                    if self.heap[i] < self.heap[parent]:
                        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                    i = parent
            else:
                if value > self.heap[0]:
                    self.heap[0] = value
                    self.heapify(0)


        def heappop(self):
            self.heap.pop(0)
            self.count -= 1
            self.heapify(0)

        def heapify(self, index):

            left = index*2 +1
            right = index*2 +2
            smallest = index
            if (left < len(self.heap) and self.heap[smallest] > self.heap[left]):
                smallest = left
            if (right < len(self.heap) and self.heap[smallest] > self.heap[right]):
                smallest = right
            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index],self.heap[smallest]
                self.heapify(smallest)



        def top(self):
            return self.heap[0]

class Solution:


    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        if k > len(nums):
            return -1
        heap = MinHeap(k)
        for i in range(k):
            heap.heappush(nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap.top():
                heap.heappush(nums[i])
        return heap.top()




