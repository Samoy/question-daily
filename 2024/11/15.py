from typing import List


# https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/?envType=daily-question&envId=2024-11-15
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        diff_row = 0
        for row in grid:
            for j in range(len(row) // 2):
                if row[j] != row[-1 - j]:
                    diff_row += 1

        diff_col = 0
        for col in zip(*grid):
            for i in range(len(grid) // 2):
                if col[i] != col[-1 - i]:
                    diff_col += 1

        return min(diff_row, diff_col)


if __name__ == '__main__':
    print(Solution().minFlips([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
    print(Solution().minFlips([[0, 1], [0, 1], [0, 0]]))
    print(Solution().minFlips([[1], [0]]))
