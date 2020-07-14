#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        r_count = l_count= 0
        for k,v in shift:
            if k == 1:
                r_count += v
            else:
                l_count += v
        flag = True
        diff = 0
        if r_count < l_count:
            diff = l_count - r_count
            flag = False
        elif r_count == l_count:
            return s
        else:
            diff = r_count - l_count
        diff = diff % len(s)
        s_list = [x for x in s]
        if flag:
            return "".join(s[-diff:]+ s[:-diff])
        else:
            return "".join(s[diff:]+ s[0:diff])
