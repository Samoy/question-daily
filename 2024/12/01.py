from typing import List


# https://leetcode.cn/problems/n-queens/?envType=daily-question&envId=2024-12-01
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return solutions


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
    print(Solution().solveNQueens(1))
