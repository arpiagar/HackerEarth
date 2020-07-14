#https://leetcode.com/problems/check-if-it-is-a-straight-line/



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) == 1:
            return True
        start_x, start_y = coordinates[0]
        end_x, end_y = coordinates[1]
        isInfiniteSlope = IsUndefined = False
        if end_x-start_x==0:
            if end_y-start_y ==0:
                IsUndefined = True
            else:
                isInfiniteSlope = True
        if not(IsUndefined or isInfiniteSlope):
            slope = (end_y-start_y)/(end_x-start_x)
        for i in range(2, len(coordinates)):
            end_x,end_y = coordinates[i]
            if IsUndefined:
                if (end_y-start_y) !=0 or (end_x-start_x)!=0:
                    return False
            if isInfiniteSlope:
                if (end_x-start_x)!=0:
                    return False
                else:
                    if (end_y-start_y) ==0:
                        return False
            if not(IsUndefined or isInfiniteSlope):
                if slope != (end_y-start_y)/(end_x-start_x):
                    return False
        return True
