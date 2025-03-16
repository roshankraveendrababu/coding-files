def helper(matrix,row,col):
    for i in range(9):
        if i!=col:
            if matrix[row][i]==matrix[row][col]:
                return False
    for i in range(9):
        if i!=row:
            if matrix[i][col]==matrix[row][col]:
                return False
    start_row=3*(row//3)
    start_col=3*(col//3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if i==row and j==col:
                continue
            if matrix[i][j]==matrix[row][col]:
                return False
    return True


def valid_sudoku(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j]!=".":
                if helper(matrix,i,j)==0:
                    return False
    return True

if __name__=="__main__":
    sudoku3 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    ["9", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(valid_sudoku(sudoku3))  # Output should be False (duplicate '9' in the last row)

