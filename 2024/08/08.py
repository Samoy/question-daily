from typing import List


# https://leetcode.cn/problems/find-the-integer-added-to-array-i/?envType=daily-question&envId=2024-08-08
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) - sum(nums1)) // len(nums1)


if __name__ == '__main__':
    print(Solution().addedInteger([2, 6, 4], [9, 7, 5]))
    print(Solution().addedInteger([10], [5]))
    print(Solution().addedInteger([1, 1, 1, 1], [1, 1, 1, 1]))
