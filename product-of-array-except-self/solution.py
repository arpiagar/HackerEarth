#https://leetcode.com/problems/product-of-array-except-self

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_zero = [(i,x) for i,x in enumerate(nums) if x==0]
        if len(nums_zero) > 1:
            return [0]*len(nums)
        elif len(nums_zero) == 0:
            product = 1
            for elem in nums:
                product = product * elem
            return [int(product/x) for x in nums]
        else:
            index, num = nums_zero[0][0],nums_zero[0][1]
            product = 1
            out = []
            print("index",index)
            for i in range(0, index):
                product = product * nums[i]
                out.append(0)
            for i in range(index+1, len(nums)):
                product = product * nums[i]
            print(product)
            out.append(product)                
            for i in range(index+1, len(nums)):
                out.append(0)
            return out
#0 1 2 3 4
#0 1 2 3#

# Without division .
# O(N) space and time complexity. 
# We use 2 intermediate arrays of size N and one output array
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1] * len(nums)
        R = [1] * len(nums)
        pr_r = pr_l = 1
        length = len(nums)
        for i in range(1, length):
                pr_l = pr_l * nums[i-1]
                L[i] = pr_l
                pr_r = pr_r * nums[length-i]
                #R[length-i-1] = pr_r
                R[length-i-1] = pr_r
        out = []
        print(L,R)
        for i in range(0, length):
            out.append(L[i]*R[i])
        return out
    
# Without division .
# O(N) space and time complexity. 
# We use 2 intermediate arrays of size N and one output array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        for i in range(1,length):
            answer[i] = answer[i-1] * nums[i-1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i]* R
            R = R * nums[i]
        return answer
            
            
