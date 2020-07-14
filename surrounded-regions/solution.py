#https://leetcode.com/problems/surrounded-regions/submissions/

class Solution:
    def expand(self, i,j,visited, board):
        print(i,j)
        if (i,j) in visited:
            return
        if i>=0 and i < len(board) and j>=0 and j< len(board[0]) and board[i][j] == "O":
            visited.add((i,j))
            self.expand(i-1,j,visited,board)
            self.expand(i,j-1,visited,board)
            self.expand(i+1,j,visited,board)
            self.expand(i,j+1,visited,board)
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        if len(board) == 1 or len(board[0]) == 1:
            return board
        visited = set([])
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == "O":
                    if (i-1 == 0) and (board[i-1][j] == "O"):
                        self.expand(i,j,visited, board)
                        continue
                    if j-1 == 0 and board[i][j-1] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if i+1 == len(board)-1 and board[i+1][j] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if j+1 == len(board[0])-1 and board[i][j+1] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if (i,j) in visited:
                        continue
        for i in range(1,len(board)-1):
            for j in range(1,2):
                if board[i][j] == "O":
                    if (i-1 == 0) and (board[i-1][j] == "O"):
                        self.expand(i,j,visited, board)
                        continue
                    if j-1 == 0 and board[i][j-1] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if i+1 == len(board)-1 and board[i+1][j] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if j+1 == len(board[0])-1 and board[i][j+1] == "O":
                        self.expand(i,j,visited,board)
                        continue
                    if (i,j) in visited:
                        continue
        
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        return board
                    
                    
