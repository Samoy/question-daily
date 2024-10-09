from cmath import inf
from typing import List


# https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/?envType=daily-question&envId=2024-10-09
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        left = bottom = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and nums[left] | right_or > k:
                ans = min(ans, (nums[left] | right_or) - k)
                if bottom <= left:
                    for i in range(right - 1, left, -1):
                        nums[i] |= nums[i + 1]
                    bottom = right
                    right_or = 0
                left += 1
            if left <= right:
                ans = min(ans, k - (nums[left] | right_or))
        return ans


if __name__ == '__main__':
    print(Solution().minimumDifference([1, 2, 4, 5], 3))
    print(Solution().minimumDifference([1, 3, 1, 3], 2))
    print(Solution().minimumDifference([1], 10))
