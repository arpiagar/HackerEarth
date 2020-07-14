#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,3,8,6,4]
        # 0 0 2 5

        start = 0
        profit = 0
        end = 1
        if not prices or len(prices)==1:
            return profit
        while(end < len(prices)):
            if prices[start] >= prices[end]:
                start += 1
                end += 1
            else:
                while(end < len(prices)-1 and prices[end] < prices[end+1]):
                    end += 1
                profit += prices[end]-prices[start]
                start = end
                end = start+1
        return profit
