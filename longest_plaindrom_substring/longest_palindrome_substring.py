class Solution(object):
    def check_longest_palindrom_length(self,s, idx1, idx2):
        count = 0
        start_idx = idx1
        while(idx1 >=0 and idx2 < len(s) and s[idx1] == s[idx2]):
            count += 1
            idx1 -= 1
            idx2 += 1
        return count, start_idx

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag =0
        max_count = 0
        if not len(s):
            return ""
        for i in xrange(0, len(s)):
            c1, start_idx1 = self.check_longest_palindrom_length(s,i,i+1)
            c2, start_idx2 = self.check_longest_palindrom_length(s,i-1,i+1)
            if (c2+1 > c1):
                if c2+1 > max_count:
                    start_idx = start_idx2
                    max_count = c2
                    flag = 1
            else:
                if c1 > max_count:
                    start_idx = start_idx1
                    max_count = c1
                    flag = 0

        if flag :
            return s[start_idx-max_count+1:start_idx+max_count+2]
        else:
            return s[start_idx-max_count+1:start_idx+max_count+1]
