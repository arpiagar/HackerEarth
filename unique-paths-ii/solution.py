#https://leetcode.com/problems/unique-paths-ii/submissions/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        tempGrid = []
        for elem in obstacleGrid:
            tempGrid.append([0]*len(elem))
            
        for i in range(0,len(obstacleGrid)):
            if obstacleGrid[i][0]:
                tempGrid[i][0] = 0
                while(i < len(obstacleGrid)):
                    tempGrid[i][0] = 0
                    i+=1
                break
            else:
                tempGrid[i][0] = 1
                
        for i in range(0,len(obstacleGrid[0])):
            if obstacleGrid[0][i]:
                tempGrid[0][i] = 0
                while(i < len(obstacleGrid[0])):
                    tempGrid[0][i] = 0
                    i += 1
                break
            else:
                tempGrid[0][i] = 1
        for i in range(1,len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    tempGrid[i][j] = 0
                else:
                    tempGrid[i][j] = tempGrid[i-1][j]+tempGrid[i][j-1]
        return tempGrid[-1][-1]
        
