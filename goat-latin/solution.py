#https://leetcode.com/problems/goat-latin/submissions/
class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        words = S.strip().split(' ')
        count = 1
        out = []
        for word in words:
            w = self.process_word(word)
            w += count*"a"
            count += 1
            out.append(w)
        return " ".join(out)
        
    def process_word(self,word):
        s = set(['a','e','i','o','u','A','E','I','O','U'])
        if word[0] in s:
            return word+"ma"
        else:
            return word[1:]+word[0]+"ma"
