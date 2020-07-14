class Solution:
    def create_map(self, arr):
        freq_map = {}
        for elem in arr:
            if elem in freq_map:
                freq_map[elem] += 1
            else:
                freq_map[elem] = 1
        return freq_map
    
    def eqMap(self, m1, m2):
        if len(m1.keys()) != len(m2.keys()):
            return False
        for k,v in m1.items():
            if k not in m2:
                return False
            if v != m2[k]:
                return False
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        if not s or not p:
            return out
        if len(p) > len(s):
            return out
        len_p = len(p)
        p_map = self.create_map(p)
        first_counter = 0
        last_counter = len_p
        s_map = self.create_map(s[first_counter:last_counter])
        if self.eqMap(s_map, p_map):
            out.append(first_counter)
        while(last_counter < len(s)):
            if s_map[s[first_counter]] ==1:
                s_map.pop(s[first_counter])
            else:
                s_map[s[first_counter]] -= 1
            if s[last_counter] in s_map:
                s_map[s[last_counter]] += 1
            else:
                s_map[s[last_counter]] = 1
            if self.eqMap(s_map, p_map):
                out.append(first_counter+1)
            first_counter += 1
            last_counter += 1
        return out
