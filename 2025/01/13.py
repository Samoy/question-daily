from itertools import accumulate
from typing import List

# https://leetcode.cn/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-13
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        t = (sum(nums) + 1) // 2
        return sum(s >= t for s in accumulate(nums[:-1]))


if __name__ == "__main__":
    print(Solution().waysToSplitArray([10, 4, -8, 7]))
    print(Solution().waysToSplitArray([2, 3, 1, 0]))