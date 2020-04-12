#https://leetcode.com/problems/output-contest-matches/submissions/

class Solution:
    def findContestMatch(self, n: int) -> str:
        out = []
        for i in range(1, n+1):
            out.append(i)
        
        while len(out) > 1:
            new_out = []
            for i in range(int(len(out)/2)):
                first_elem = out[i]
                last_elem = out[len(out)-1-i]
                new_out.append(self.createMatch(first_elem,last_elem))
            out = new_out
        return out[0]
        
    def createMatch(self, a, b):
        return "("+str(a)+","+str(b)+")"
