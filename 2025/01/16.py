from cmath import inf
from typing import List


# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/?envType=daily-question&envId=2025-01-16
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            if x >= k:
                return 1
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                if nums[j] >= k:
                    ans = min(ans, i - j + 1)
                j -= 1
        return ans if ans < inf else -1


if __name__ == "__main__":
    print(Solution().minimumSubarrayLength(nums=[1, 2, 3], k=2))
    print(Solution().minimumSubarrayLength(nums=[2, 1, 8], k=10))
    print(Solution().minimumSubarrayLength(nums=[1, 2], k=0))
