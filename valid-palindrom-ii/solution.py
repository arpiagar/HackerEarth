#https://leetcode.com/problems/valid-palindrome-ii/submissions/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validPalidromeUtil(s,0)
    
    def validPalidromeUtil(self, s, count):
        if not s:
            return True
        start = 0
        end = len(s)-1
        f1 = f2 = False
        while start < end:
            if s[start] != s[end]:
                if count == 0 :
                    if s[start+1] == s[end] :
                        f1 = self.validPalidromeUtil(s[start+1:end+1],count+1)
                    if  s[start] == s[end-1] :
                        f2 = self.validPalidromeUtil(s[start:end],count+1)
                    return f1 or f2
                else:
                    return False
            start += 1
            end -= 1
        return True
