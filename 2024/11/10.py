from bisect import bisect_left
from typing import List


# https://leetcode.cn/problems/single-element-in-a-sorted-array/?envType=daily-question&envId=2024-11-10
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        k = bisect_left(range(len(nums) // 2), True, key=lambda key: nums[key * 2] != nums[key * 2 + 1])
        return nums[k * 2]


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
