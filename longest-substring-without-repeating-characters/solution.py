#https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bitmap = [0 for x in range(0,256)]
        max_len = 0
        u_map={}
        for i in range(len(s)):
            elem = s[i]
            if elem in u_map:
                max_len = max(max_len, i-u_map[elem])
                keys = []
                for k,v in u_map.items():
                    if v <= u_map[elem]:
                        keys.append(k)
                for key in keys:
                    u_map.pop(key)
                u_map[elem] = i
            else:
                u_map[elem] = i
                max_len = max(max_len, len(u_map.keys()))
        return max_len


