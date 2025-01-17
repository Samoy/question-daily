from cmath import inf
from typing import List


# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/?envType=daily-question&envId=2025-01-17
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        left = bottom = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and nums[left] | right_or >= k:
                ans = min(ans, right - left + 1)
                left += 1
                if bottom < left:
                    # 重新构建一个栈
                    for i in range(right - 1, left - 1, -1):
                        nums[i] |= nums[i + 1]
                    bottom = right
                    right_or = 0
        return ans if ans < inf else -1


if __name__ == "__main__":
    print(Solution().minimumSubarrayLength(nums=[1, 2, 3], k=2))
    print(Solution().minimumSubarrayLength(nums=[2, 1, 8], k=10))
    print(Solution().minimumSubarrayLength(nums=[1, 2], k=0))
