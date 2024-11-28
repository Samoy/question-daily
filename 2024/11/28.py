from itertools import pairwise
from math import comb
from typing import List


# https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-i/?envType=daily-question&envId=2024-11-28
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        m = nums[-1]
        for x, y in pairwise(nums):
            m -= max(y - x, 0)
        return comb(m + len(nums), m) % MOD if m >= 0 else 0


if __name__ == '__main__':
    print(Solution().countOfPairs([2, 3, 2]))
    print(Solution().countOfPairs([5, 5, 5, 5]))
