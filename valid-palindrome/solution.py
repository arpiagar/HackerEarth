#https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_set = set()
        for i in range(0,10):
            valid_set.add(str(i))
        for i in range(0,26):
            valid_set.add(chr(ord('a')+i))
        s_arr = [x for x in s if x in valid_set]
        if not s_arr :
            return True
        start = 0
        end = len(s_arr)-1 # 0,1.
        for i in range(0, int(len(s_arr)/2)+1):
            if s_arr[start+i] != s_arr[end-i]:
                return False
        return True

