#https://leetcode.com/problems/decode-ways/submissions/

# 2,7 - 1
# 23 -- 2
#1 23 -- 2
#12 3 --  1
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1

        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            two_digit = int(s[i-2:i])
            if two_digit >= 10  and two_digit <=26:
                dp[i] += dp[i-2]
        return dp[len(s)]
