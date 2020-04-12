#https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.p_util(0, 0, n, [""])
    
    
    
    def p_util(self, left_count, right_count, n, out_list):
        if left_count == n and right_count == n :
            return out_list
        l1 = []
        l2 = []
        if left_count < n:
            list1 = [x+"(" for x in out_list]
            l1 = self.p_util(left_count+1, right_count, n , list1)
        if right_count < n and right_count < left_count:
            list1 = [x+")" for x in out_list]
            l2 = self.p_util(left_count, right_count+1, n , list1)
        return l1+l2
