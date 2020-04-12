#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha_map = {}
        for i in range(0, 9):
            alpha_map[str(i+1)] = chr(ord('a')+i)
        for i in range(10, 27):
            alpha_map[str(i)+"#"] = chr(ord('a')+i-1)

        index = 0
        out = ""
        while index < len(s)-2:
            current = s[index]
            next_c = s[index+1]
            next_next_c = s[index+2]
            if next_next_c == "#":
                out += alpha_map[s[index:index+3]]
                index += 3
            elif current != "#":
                out += alpha_map[s[index]]
                index += 1
            else:
                index += 1
        while(index < len(s)):
            out += alpha_map[s[index]]
            index += 1
        return out

