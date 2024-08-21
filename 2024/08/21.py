from bisect import bisect_left
from functools import cache


# https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description/?envType=daily-question&envId=2024-08-21
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count(num: int) -> int:
            @cache
            def dfs(i: int, cnt1: int, is_limit: bool) -> int:
                if i == 0:
                    return cnt1
                res = 0
                up = num >> (i - 1) & 1 if is_limit else 1
                for d in range(up + 1):  # 枚举要填入的数字 d
                    res += dfs(i - 1, cnt1 + (d == 1 and i % x == 0), is_limit and d == up)
                return res

            return dfs(num.bit_length(), 0, True)

        return bisect_left(range((k + 1) << x), k + 1, key=count) - 1
