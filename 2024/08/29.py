from typing import List


# https://leetcode.cn/problems/check-if-grid-satisfies-conditions/description/?envType=daily-question&envId=2024-08-29
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i < m - 1:
                    if grid[i][j] != grid[i + 1][j]:
                        return False
                if j < n - 1:
                    if grid[i][j] == grid[i][j + 1]:
                        return False
        return True


if __name__ == '__main__':
    print(Solution().satisfiesConditions([[1, 0, 2], [1, 0, 2]]))
    print(Solution().satisfiesConditions([[1, 1, 1], [0, 0, 0]]))
    print(Solution().satisfiesConditions([[1], [2], [3]]))
