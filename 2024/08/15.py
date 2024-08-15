from cmath import inf
from typing import List


# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/?envType=daily-question&envId=2024-08-15
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre_min = [[inf] * n for _ in range(2)]
        ans = -inf

        for i in range(m):
            pre_min[i & 1] = [inf] * n
            for j in range(n):
                pre = inf
                if i > 0:
                    pre = min(pre, pre_min[(i - 1) & 1][j])
                if j > 0:
                    pre = min(pre, pre_min[i & 1][j - 1])
                # i = j = 0 时没有转移
                if i + j > 0:
                    ans = max(ans, grid[i][j] - pre)
                pre_min[i & 1][j] = min(pre, grid[i][j])
        return ans


if __name__ == '__main__':
    print(Solution().maxScore(grid=[[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]))
    print(Solution().maxScore(grid=[[4, 3, 2], [3, 2, 1]]))
