#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for elem in strs:
            s_elem = "".join(sorted(elem))
            if s_elem in s:
                s[s_elem].append(elem)
            else:
                s[s_elem] = [elem]
        return s.values()
