#https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        return self.find_first(start, end)

    def find_first(self, start, end):
        if (end >= start):
            mid = int((start+end)/2)
            if isBadVersion(mid):
                ret = self.find_first(start, mid-1)
                if ret == -1:
                    return mid
                else:
                    return ret
            else:
                return self.find_first(mid+1 , end)
        else:
            return -1


