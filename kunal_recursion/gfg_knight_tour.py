class Grid:
    def create_mat(self, n):
        mat = [[-1 for _ in range(n)] for _ in range(n)]
        mat[0][0] = 0
        return mat  # Ensure it returns the matrix

    def solve_mat(self, mat):
        move_x = [2, 2, -2, -2, -1, -1, 1, 1]
        move_y = [-1, 1, -1, 1, 2, -2, 2, -2]

        if not self.solve_recursive(mat, 0, 0, move_x, move_y, 1):
            print("Solution does not exist")  # Handle the case where no solution exists

    def issafe(self, mat, cur_x, cur_y):
        return 0 <= cur_x < len(mat) and 0 <= cur_y < len(mat) and mat[cur_x][cur_y] == -1

    def solve_recursive(self, mat, cur_x, cur_y, mov_x, mov_y, pos):
        if pos == len(mat) ** 2:
            return True  # Base case: If all squares are visited
        
        for i in range(8):
            new_x = cur_x + mov_x[i]
            new_y = cur_y + mov_y[i]
            if self.issafe(mat, new_x, new_y):
                mat[new_x][new_y] = pos
                if self.solve_recursive(mat, new_x, new_y, mov_x, mov_y, pos + 1):
                    return True  # If a solution is found, stop recursion
                mat[new_x][new_y] = -1  # Backtrack

        return False  # No valid move found

    def print_mat(self, mat):
        for row in mat:
            print(" ".join(str(cell).rjust(2) for cell in row))

if __name__ == "__main__":
    grid = Grid()
    mat = grid.create_mat(8)
    grid.solve_mat(mat)
    grid.print_mat(mat)
