#https://leetcode.com/problems/count-servers-that-communicate/submissions/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows_set = set([])
        cols_set = set([])
        for i in range(0, len(grid)):
            temp = [ x for x in grid[i] if x]
            if len(temp) >= 2:
                rows_set.add(i)
        for j in range(0, len(grid[0])):
            count = 0
            for i in range(0, len(grid)):
                if grid[i][j] == 1:
                    count += 1
            if count >= 2:
                cols_set.add(j)
        
        count = 0
        print(rows_set, cols_set)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i in rows_set and grid[i][j]:
                    count += 1
                elif j in cols_set and grid[i][j]:
                    count += 1
                    
        return count
                
