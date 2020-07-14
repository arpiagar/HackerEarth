#https://leetcode.com/problems/permutation-in-string


class Solution:
    def createMap(self, s):
        freq_map = {}
        for elem in s:
            if elem not in freq_map:
                freq_map[elem] = 1
            else:
                freq_map[elem] += 1
        return freq_map
    def checkMap(self, m1, m2):
        if len(m1.keys()) != len(m2.keys()):
            return False
        for k,v in m2.items():
            if k not in m1:
                return False
            if m1[k]!= v:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2,s1=s1,s2
        if len(s2) > len(s1):
            return False
        if not len(s2):
            return False
        m2 = self.createMap(s2)
        m1 = self.createMap(s1[0:len(s2)])
        if self.checkMap(m1,m2):
            return True
        first_counter = 0
        last_counter = len(s2)
        while(last_counter < len(s1)):
            elem = s1[first_counter]
            if m1[elem] == 1:
                m1.pop(elem)
            else:
                m1[elem] -= 1
            new_elem = s1[last_counter]
            if new_elem in m1:
                m1[new_elem] += 1
            else:
                m1[new_elem] = 1
            if self.checkMap(m1,m2):
                return True
            last_counter += 1
            first_counter +=1

        return False












