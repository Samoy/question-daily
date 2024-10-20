from typing import List


# https://leetcode.cn/problems/smallest-range-i/?envType=daily-question&envId=2024-10-20
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)


if __name__ == '__main__':
    print(Solution().smallestRangeI(nums=[1], k=0))
    print(Solution().smallestRangeI(nums=[0, 10], k=2))
    print(Solution().smallestRangeI(nums=[1, 3, 6], k=3))
