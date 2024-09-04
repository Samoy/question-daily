from itertools import pairwise
from typing import List


# https://leetcode.cn/problems/happy-students/?envType=daily-question&envId=2024-09-04
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0] > 0  # 一个学生都不选
        for i, (x, y) in enumerate(pairwise(nums), 1):
            if x < i < y:
                ans += 1
        return ans + 1  # 一定可以都选


if __name__ == '__main__':
    print(Solution().countWays([1, 1]))
    print(Solution().countWays([6, 0, 3, 3, 6, 7, 2, 7]))
