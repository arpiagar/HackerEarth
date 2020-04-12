https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out_list = []
        for i in range(len(s)-1, -1, -1):
            elem = s[i]
            if elem == " " :
                if len(out_list):
                    break
            else:
                out_list.append(elem)
        return len(out_list)
