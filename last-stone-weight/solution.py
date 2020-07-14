#https://leetcode.com/problems/last-stone-weight/solution/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        sorted_stones = sorted(stones, reverse=True)
        count = 1
        stone1 = sorted_stones[0]
        while(count < len(sorted_stones)):
            stone2 = sorted_stones[count]
            if stone1 == stone2:
                if count+1 == len(sorted_stones):
                    return 0
                stone1 = sorted_stones[count+1]
                count += 2
            else:
                stone1 = abs(stone1-stone2)
                if count+1 == len(sorted_stones):
                    return stone1
                sorted_stones = sorted([stone1]+sorted_stones[count+1:], reverse=True)
                stone1 = sorted_stones[0]
                count = 1
        return stone1
        
        
    

