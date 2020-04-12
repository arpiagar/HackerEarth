#https://leetcode.com/problems/number-of-islands/submissions/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        if not grid : # []
            return 0
        if not grid[0]: # [[]]
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1":
                    if (i,j) not in visited :
                        self.mapIsland(grid, i,j,visited)
                        count += 1
        return count

    def mapIsland(self, grid, i, j, visited):
        if i<0 or i>= len(grid) or j<0 or j>= len(grid[0]):
            return
        if (i,j) in visited:
            return
        if grid[i][j] == "0":
            return
        if grid[i][j]:
            visited[(i,j)] = 1
            self.mapIsland(grid, i-1,j, visited)
            self.mapIsland(grid, i+1,j, visited)
            self.mapIsland(grid, i,j-1, visited)
            self.mapIsland(grid, i,j+1, visited)

