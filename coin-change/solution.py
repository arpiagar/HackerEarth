https://leetcode.com/problems/coin-change/solution/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sorted_coins = sorted(coins, reverse=True)
        coin_map = {}
        return self.min_combination(coins, amount, coin_map)
    
    
    
    def min_combination(self, coins, amount, coin_map):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in coin_map:
            return coin_map[amount]
        if amount in coins:
            coin_map[amount] = 1
            return 1
        min_coins = amount+1
        for coin in coins:
            ret_val = self.min_combination(coins, amount-coin, coin_map) 
            if ret_val != -1:
                min_coins = min(min_coins, ret_val)
        if min_coins == amount+1:
            coin_map[amount] = -1
        else:
            coin_map[amount] = 1+min_coins
        return coin_map[amount] 
