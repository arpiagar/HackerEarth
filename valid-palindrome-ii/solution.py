#https://leetcode.com/problems/valid-palindrome-ii/submissions/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isValidPalindrome(s,0, len(s)-1, 0)
    def isValidPalindrome(self, s, i, j, count):
        if i >=j:
            return True
        if s[i] == s[j]:
            return self.isValidPalindrome(s, i+1, j-1, count)
        else:
            if not count:
                return self.isValidPalindrome(s, i+1, j, count+1) or self.isValidPalindrome(s, i, j-1, count+1)
            else:
                return False
