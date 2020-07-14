#https://leetcode.com/problems/sort-characters-by-frequency/submissions/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}
        for elem in s:
            if elem in freq_map:
                freq_map[elem] += 1
            else:
                freq_map[elem] = 1
        sorted_l = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)
        out = []
        for elem in sorted_l:
             out.append(elem[0]*elem[1])
        return "".join(out)
