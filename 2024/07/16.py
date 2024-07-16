from typing import List


# https://leetcode.cn/problems/find-common-elements-between-two-arrays/?envType=daily-question&envId=2024-07-16
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [sum(x in set2 for x in nums1), sum(x in set1 for x in nums2)]


if __name__ == '__main__':
    print(Solution().findIntersectionValues([2, 3, 2], [1, 2]))
    print(Solution().findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))
    print(Solution().findIntersectionValues([3, 4, 2, 3], [1, 5]))
