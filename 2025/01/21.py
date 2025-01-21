from functools import cache
from itertools import accumulate
from typing import List


# https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/?envType=daily-question&envId=2025-01-21
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            # 不选这一组中的任何物品
            res = dfs(i - 1, j)
            # 枚举选哪个
            for w, v in enumerate(accumulate(piles[i][:j]), 1):
                res = max(res, dfs(i - 1, j - w) + v)
            return res
        return dfs(len(piles) - 1, k)


if __name__ == "__main__":
    print(Solution().maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))
    print(
        Solution().maxValueOfCoins(
            piles=[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],
            k=7,
        )
    )
