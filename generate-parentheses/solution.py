class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lc = rc = 0
        out = []
        return self.gen(0,0,n,[],out)
        
    
        
    def gen(self, lc, rc,n, curr, out):
        if rc > lc:
            return
        if lc == n:
            out.append("".join(curr) + ")"* (n-rc))
        else:
            self.gen(lc+1, rc,n, [x for x in curr]+["("], out )
            self.gen(lc, rc+1 ,n, [x for x in curr]+[")"], out )
        return out
            
                
                
            
