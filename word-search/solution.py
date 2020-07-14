#https://leetcode.com/problems/word-search/solution/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        n_rows= len(board)
        n_cols = len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == word[0]:
                    visited = set([(i,j)])
                    print(i,j)
                    if self.checkForCompleteWord(board, i, j, n_rows,n_cols,word[1:], visited):
                        return True
        return False

    def checkForCompleteWord(self, board, x, y, n_rows, n_cols, rem_word, visited):
        if not rem_word:
            return True
        flag = False
        if x-1 >=0 and (x-1,y) not in visited and board[x-1][y]==rem_word[0]:
            visited.add((x-1,y))
            if self.checkForCompleteWord(board, x-1, y, n_rows,n_cols,rem_word[1:], visited):
                return True
            else:
                visited.remove((x-1,y))
        if y-1 >=0 and (x,y-1) not in visited and board[x][y-1]==rem_word[0]:
            visited.add((x,y-1))
            if self.checkForCompleteWord(board, x, y-1, n_rows,n_cols,rem_word[1:], visited):
                return True
            else:
                visited.remove((x,y-1))
        if x+1 < n_rows and (x+1,y) not in visited and board[x+1][y]==rem_word[0]:
            visited.add((x+1,y))
            if self.checkForCompleteWord(board, x+1, y, n_rows,n_cols,rem_word[1:], visited):
                return True
            else:
                visited.remove((x+1,y))
        if y+1 < n_cols and (x,y+1) not in visited and board[x][y+1]==rem_word[0]:
            visited.add((x,y+1))
            if self.checkForCompleteWord(board, x, y+1, n_rows,n_cols,rem_word[1:], visited):
                return True
            else:
                visited.remove((x,y+1))
        return False





