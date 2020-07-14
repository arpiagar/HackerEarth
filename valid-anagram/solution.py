#https://leetcode.com/problems/valid-anagram/submissions/

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for elem in s:
            s_map[elem] += 1
        for elem in t:
            t_map[elem] += 1
        if len(s_map.keys()) != len(t_map.keys()):
            return False
        for k,v in s_map.items():
            if t_map[k] != v:
                return False
        return True
