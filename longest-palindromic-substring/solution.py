#https://leetcode.com/problems/longest-palindromic-substring/solution/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s :
            return s
        max_l = 1
        id_l = 0
        id_r = 0
        for i in range(1,n):
                if s[i-1] == s[i]:
                    left = i-1
                    right = i
                    while(left >=0 and right <n and s[left]==s[right]):
                        left -= 1
                        right += 1
                    if right-left+1 > max_l:
                        id_l = left+1
                        id_r = right-1
                        max_l = right-left+1
                if i+1 <n and s[i-1]==s[i+1]:
                    left = i-1
                    right = i+1
                    while(left >=0 and right <n and s[left]==s[right]):
                        left -= 1
                        right += 1
                    if right-left+1 > max_l:
                        id_l = left+1
                        id_r = right-1
                        max_l = right-left+1
        return s[id_l:id_r+1]
