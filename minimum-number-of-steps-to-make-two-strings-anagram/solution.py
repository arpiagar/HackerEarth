#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/

from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1
        length = len(t)
        count = 0
        for key in t_map.keys():
            if key in s_map:
                if t_map[key] > s_map[key]:
                    count += s_map[key]
                else:
                    count += t_map[key]
        return length-count
