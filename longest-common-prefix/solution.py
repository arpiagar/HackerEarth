#https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min([len(x) for x in strs])
        out = []
        flag = True
        for i in range(0, min_len):
            char = strs[0][i]
            for elem in strs:
                if elem[i] != char:
                    flag = False
                    break
            if not flag:
                break
            out.append(char)
        return "".join(out)
