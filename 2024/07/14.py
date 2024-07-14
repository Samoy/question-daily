from typing import List


# https://leetcode.cn/problems/max-increase-to-keep-city-skyline/?envType=daily-question&envId=2024-07-14
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = [max(row) for row in grid]
        n = len(grid)
        grid_transpose = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid_transpose[i][j] = grid[j][i]
        max_col = [max(col) for col in grid_transpose]
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(max_row[i], max_col[j]) - grid[i][j]
        return ans


if __name__ == '__main__':
    print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
    print(Solution().maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
