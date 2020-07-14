i#https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        out = []
        i,j,k = 0,0,0

        while(i < len(nums1) and j<len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                out.append(nums1[i])
                i += 1
                j += 1
        return out
        if len(nums1) < len(nums2):
            for elem in nums1:
                if self.binary_search(nums2, elem) != -1:
                    out.append(elem)
        else:
            for elem in nums2:
                if self.binary_search(nums1, elem) != -1:
                    out.append(elem)
        return out

    def binary_search(self, nums, target):
        left, right = 0 , len(nums)
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1


