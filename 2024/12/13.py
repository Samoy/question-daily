from typing import List


# https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/?envType=daily-question&envId=2024-12-13
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            nums[nums.index(min(nums))] *= multiplier
        return nums


if __name__ == '__main__':
    print(Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
    print(Solution().getFinalState(nums=[1, 2], k=3, multiplier=4))
