#https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: # ahbgdc #axc
        if len(s) > len(t):
            return False
        t_map = {}
        for i in range(len(t)): #{a:0,h:1,b:2,g:3,d:4,c:5}
            if t[i] in t_map:
                t_map[t[i]].append(i)
            else:
                t_map[t[i]] = [i]
        index = -1
        for elem in s:
            if elem not in t_map:
                return False
            index_list = t_map[elem] #[0]
            temp = [x for x in index_list if x> index]
            if not temp:
                return False
            index= min(temp)
        return True
