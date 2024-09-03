from typing import List


# https://leetcode.cn/problems/maximum-strength-of-a-group/?envType=daily-question&envId=2024-09-03
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mn = mx = nums[0]
        for x in nums[1:]:
            mn, mx = min(mn, x, mn * x, mx * x), max(mx, x, mn * x, mx * x)
        return mx


if __name__ == '__main__':
    print(Solution().maxStrength([3, -1, -5, 2, 5, -9]))
    print(Solution().maxStrength([-4, -5, -4]))
