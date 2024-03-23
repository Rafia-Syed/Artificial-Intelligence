class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if there is a queen in the same row to the left
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_queens(self, col):
        if col >= self.n:
            # Base case: All queens are placed successfully
            self.solutions.append([row[:] for row in self.board])
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                # Place the queen
                self.board[i][col] = 1

                # Recur to place rest of the queens
                self.solve_queens(col + 1)

                # If placing queen in board[i][col] doesn't lead to a solution, backtrack
                self.board[i][col] = 0

        return False

    def find_solutions(self):
        self.solve_queens(0)
        return self.solutions


def print_solution(solution):
    for row in solution:
        print(" ".join(map(str, row)))
    print()


# Example usage
if __name__ == "__main__":
    n = 8  # Change this value to solve for different board sizes
    solver = NQueens(n)
    solutions = solver.find_solutions()

    print(f"Total solutions for {n}-Queens problem: {len(solutions)}\n")
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        print_solution(solution)
