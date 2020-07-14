#https://leetcode.com/problems/island-perimeter/

class Solution:
    def checkSurroundingZero(self,grid, x,y):
        count = 0
        if x-1 <0:
            count +=1
        else:
            if grid[x-1][y] == 0:
                count +=1
        if y-1<0:
            count += 1
        else:
            if grid[x][y-1] ==0:
                count += 1
        if x+1 == len(grid):
            count += 1
        else:
            if grid[x+1][y] == 0:
                count +=1
        if y+1 == len(grid[0]):
            count += 1
        else:
            if grid[x][y+1] == 0:
                count += 1
        return count

    def getMap(self,grid, i, j, visited_map):
        if grid[i][j] and (i,j) not in visited_map:
            visited_map.add((i,j))
            if i+1 < len(grid):
                self.getMap(grid,i+1,j,visited_map)
            if i-1 >= 0:
                self.getMap(grid,i-1,j,visited_map)
            if j+1 < len(grid[0]):
                self.getMap(grid, i,j+1,visited_map)
            if j-1 >=0:
                self.getMap(grid, i,j-1,visited_map)

    def retVal(self, boundary_map, visited_map):
        count = 0
        for elem in visited_map:
            count += boundary_map[elem]
        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        boundary_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    boundary_map[(i,j)] = self.checkSurroundingZero(grid,i,j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    visited_map = set([])
                    self.getMap(grid, i, j, visited_map)
                    return self.retVal(boundary_map, visited_map)


