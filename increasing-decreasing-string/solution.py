#https://leetcode.com/problems/increasing-decreasing-string/submissions/


from collections import defaultdict
class Solution:
    def sortString(self, s: str) -> str:      
        s = "".join(sorted(s))
        s_list = [x for x in s]
        out = []
        while len(s):
            idx = 0
            while idx < len(s):
                idx = s.rfind(s[idx])
                out.append(s[idx])
                s_list[idx] = "|"
                idx += 1
            s_list = [x for x in s_list if x != "|"]
            s = "".join(s_list)
            idx = len(s)-1
            while idx >= 0:
                idx = s.find(s[idx])
                out.append(s_list[idx])
                s_list[idx] = "|"
                idx -= 1
            s_list = [x for x in s_list if x != "|"]
            s = "".join(s_list)
        return "".join(out)
                
