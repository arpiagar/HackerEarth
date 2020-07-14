i#https://leetcode.com/problems/count-number-of-teams/



class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        if len(rating) < 3:
            return count
        n = len(rating)
        first = second = third = 0
        while(first < n-2):
            first_elem = rating[first]
            second = first+1
            while(second < n-1):
                second_elem = rating[second]
                third = second +1
                if second_elem > first_elem:
                    count += len([x for x in rating[third:] if x>second_elem])
                else:
                    count += len([x for x in rating[third:] if x < second_elem])
                second += 1
            first += 1
        return count
