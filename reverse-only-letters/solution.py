#https://leetcode.com/problems/reverse-only-letters/submissions/


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return S
        S = [x for x in S]
        left, right = 0, len(S)-1
        s = set()
        for i in range(ord('a'), ord('z')+1):
            s.add(chr(i))
        for i in range(ord('A'), ord('Z')+1):
            s.add(chr(i))
        while left <len(S)-1 and S[left] not in s :
            left += 1
        while  right >=0  and S[right] not in s:
            right -= 1
        print(left,right)
        while left < right:
            while left <len(S)-1 and S[left] not in s:
                left += 1
            while  right >=0 and S[right] not in s:
                right -= 1
            if left<right:
                S[left],S[right] = S[right], S[left]
                left +=1
                right -=1        
        return "".join(S)
