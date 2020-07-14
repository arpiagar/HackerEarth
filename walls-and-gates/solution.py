#https://leetcode.com/problems/walls-and-gates/solution/



class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return rooms

        counter = 0
        m_set = set([])
        n_rows= len(rooms)-1
        n_col = len(rooms[0])-1
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == counter:
                    m_set.add((i,j, counter))

        stack = [x for x in m_set]
        while stack:
            x,y, counter = stack.pop(0)
            if x-1 >=0 and (x-1,y) not in m_set and rooms[x-1][y]==2147483647:
                m_set.add((x-1,y))
                stack.append((x-1,y, counter+1))
                rooms[x-1][y] = counter+1
            if x+1 <= n_rows and (x+1,y) not in m_set and rooms[x+1][y]==2147483647:
                m_set.add((x+1,y))
                stack.append((x+1,y, counter+1))
                rooms[x+1][y] = counter+1
            if  y-1 >=0 and (x,y-1) not in m_set and rooms[x][y-1]==2147483647:
                m_set.add((x,y-1))
                stack.append((x,y-1, counter+1))
                rooms[x][y-1] = counter+1
            if  y+1 <= n_col and (x,y+1) not in m_set and rooms[x][y+1]==2147483647:
                m_set.add((x,y+1))
                stack.append((x,y+1, counter+1))
                rooms[x][y+1] = counter+1
        return rooms
