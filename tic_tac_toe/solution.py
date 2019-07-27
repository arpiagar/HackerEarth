# In a N*N matric,  a win is qualified as a pattern or X or O (P times) where P<=N
# Return the winning combination given a state matrix
# direction = "R","U","D","UD", "DD"
def return_winning_combo(matrix , symbol, p_count, curr_count, idx, idy, direction):
    N = len(matrix[0])
    out = []
    element =  matrix[idx][idy]
    if curr_count > p_count:
        return []
    if element == symbol:
        if curr_count +1  == p_count:
            return return_matrix_indices(matrix, idx, idy, direction)
        else:
            if idx-1 >=0 :
                if direction == "L":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx-1, idy, "L"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx-1, idy, "L"))
            if idx+1 < N:
                if direction == "R":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx+1, idy, "R"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx+1, idy, "R"))
            if idy-1 >=0 :
                if direction == "U":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx, idy-1, "U"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx, idy-1, "U"))
            if idy+1 < N:
                if direction == "D":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx+1, idy, "D"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx, idy+1, "D"))
            if idx-1 >=0 and idy-1 >=0 :
                if direction == "UL":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx-1, idy-1, "UL"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx-1, idy-1, "UL"))
            if idx+1 < N and idy+1 < N:
                if direction == "RD":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx+1, idy+1, "RD"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx+1, idy+1, "RD"))
            if idx-1 >=0 and idy+1 < N :
                if direction == "LD":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx-1, idy+1, "LD"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx-1, idy+1, "LD"))
            if idx+1 <N and idy-1 >= 0:
                if direction == "RU":
                    out.append(return_winning_combo(matrix, symbol, p_count, curr_count+1, idx+1, idy-1, "RU"))
                else:
                    out.append(return_winning_combo(matrix, symbol, p_count, 1, idx+1, idy-1, "RU"))
    else:
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx-1, idy, "L"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx+1, idy-1, "RU"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx-1, idy+1, "LD"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx+1, idy+1, "RD"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx-1, idy-1, "UL"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx, idy+1, "D"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx+1, idy, "R"))
        out.append(return_winning_combo(matrix, symbol, p_count, 0, idx, idy-1, "U"))
    return []

def return_matrix_indices(matrix, idx, idy, direction, p_count):
    out = []
    if direction == "L":
        for i in xrange(0, p_count):
            out.append((idx+i, idy))
    if direction == "R":
        for i in xrange(0, p_count):
             out.append((idx-i, idy))
    if direction == "U":
         for i in xrange(0, p_count):
              out.append((idx, idy+i))
    if direction == "D":
         for i in xrange(0, p_count):
              out.append((idx, idy-i))
    if direction == "UL":
         for i in xrange(0, p_count):
              out.append((idx+i, idy+i))
    if direction == "DR":
         for i in xrange(0, p_count):
              out.append((idx-i, idy-i))
    if direction == "UR":
         for i in xrange(0, p_count):
              out.append((idx-i, idy+1))
    if direction == "DL":
         for i in xrange(0, p_count):
              out.append((idx+i, idy-1))
    return out
if __name__ == "__main__":



