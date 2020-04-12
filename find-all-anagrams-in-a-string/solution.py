#https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        if len(p) > len(s):
            return out
        smaller_len = len(p)
        #5  ABCDE
        #3  abc

        compare_dict = self.makeDict(p, 0, len(p)-1)
        for i in range(0, len(s)-len(p)+1):
            if not i:
                m_dict = self.makeDict(s, i , i+smaller_len-1)
            else:
                m_dict = self.editDict(m_dict, s[i-1], s[i+smaller_len-1])
            if self.isAnagram(m_dict, compare_dict):
                out.append(i)
        return out

    def editDict(self, m_dict, remove, add):
        if m_dict[remove] == 1:
            m_dict.pop(remove)
        else:
            m_dict[remove] -= 1
        m_dict[add] += 1

        return m_dict
    def makeDict(self, nums, start, end):
        d = defaultdict(int)
        print(nums, start, end)
        for i in range(start, end+1):
            d[nums[i]] += 1
        return d

    def isAnagram(self, p1,p2):
        for k,v in p1.items():
            if k not in p2:
                return False
            if p2[k] != v:
                return False
        return True
