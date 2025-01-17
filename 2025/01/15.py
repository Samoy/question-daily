from heapq import heapify, heappop, heapreplace
from typing import List


# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/?envType=daily-question&envId=2025-01-15
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums[0] < k:
            x = heappop(nums)
            heapreplace(nums, nums[0] + x * 2)
            ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10))
    print(Solution().minOperations(nums=[1, 1, 2, 4, 9], k=20))
