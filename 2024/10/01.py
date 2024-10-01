from functools import lru_cache
from typing import List


# https://leetcode.cn/problems/minimum-cost-for-tickets/?envType=daily-question&envId=2024-10-01
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in day_set:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)


if __name__ == '__main__':
    print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
