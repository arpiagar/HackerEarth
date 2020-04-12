from typing import Dict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoizedDict = {}
        return self.wordBreakMemoized(s, wordDict, memoizedDict)
    
    def wordBreakMemoized(self, s: str, wordDict: List[str], memoizedDict: Dict[str,bool]) -> bool:
        if s == "":
            return True
        curr_string = ""
        flag = False
        for i in range(len(s)):
            letter = s[i]
            curr_string += letter
            if curr_string in wordDict:
                if s[i+1:] in memoizedDict:
                    ret_flag = memoizedDict[s[i+1:]]
                else:
                    ret_flag = self.wordBreakMemoized(s[i+1:], wordDict, memoizedDict)
                    memoizedDict[s[i+1:]] = ret_flag
                flag = flag or ret_flag
                if flag:
                    return flag
        return flag
            
        
    
    
        
