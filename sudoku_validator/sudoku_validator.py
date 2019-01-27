
def check_row_and_col(board):
	for i in range(0, len(board)):
		row_map = {}
		col_map = {}
		for j in xrange(0, len(board[0])):
			elem_row =  board[i][j]
			elem_col =  board[j][i]
			if board[i][j] != ".":
				if row_map.has_key(elem_row):
					return False
				else:
					row_map[elem_row] =  1
				if col_map.has_key(elem_col):
					return False
				else:
					col_map[elem_col] = 1
	return True


def check_box(board,  row,  col):
	box_map = {}
	for i in xrange(0,3):
		for j in xrange(0, 3):
			elem  = board[row+i][col+j]
			if elem != ".":
				if box_map.has_key(elem):
					return False
				else:
					box_map[elem] = 1
	return True


def is_valid(board):
	if not check_row_and_col(board):
		return False
	for row in xrange(0, len(board), 3):
		for col in xrange(0, len(board[0]), 3):
			if not check_box(board, row, col):
				return False
	return True


board = [["1","2","3",".",".",".",".",".","."],["4","5","6",".",".",".",".",".","."],["7","5","9",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print board
print len(board)
print len(board[0])
print (is_valid(board))