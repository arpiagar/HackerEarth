#https://leetcode.com/problems/unique-paths-ii/submissions/

from copy import copy, deepcopy

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        out_grid = deepcopy(obstacleGrid)
        all_rows_false = False
        if len(obstacleGrid):
            first_row =  obstacleGrid[0]
            i = 0
            block_further = False
            for j in range(0, len(first_row)):
                if first_row[j] == 1 or  block_further:
                    block_further = True
                    out_grid[0][j] = 0
                else:
                    out_grid[0][j] =  1
            block_further = False
            for i in range(0, len(obstacleGrid)):
                row = obstacleGrid[i]
                if len(row):
                    if row[0] == 1 or block_further:
                        out_grid[i][0] = 0
                        block_further = True
                    else:
                        out_grid[i][0] = 1
                else:
                    return 0

            for i  in range(1, len(obstacleGrid)):
                row = obstacleGrid[i]
                for j in range(1, len(row)) :
                    if obstacleGrid[i][j] == 1:
                        out_grid[i][j] = 0
                    else:
                        out_grid[i][j] = out_grid[i-1][j] + out_grid[i][j-1]
        else:
            return 0
        return out_grid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


