from typing import List


# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/?envType=daily-question&envId=2025-01-14
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(x < k for x in nums)


if __name__ == "__main__":
    print(Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10))
    print(Solution().minOperations(nums=[1, 1, 2, 4, 9], k=1))
    print(Solution().minOperations(nums=[1, 1, 2, 4, 9], k=9))
