from typing import List


# https://leetcode.cn/problems/find-the-integer-added-to-array-ii/?envType=daily-question&envId=2024-08-09
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            j = 0
            for v in nums1[i:]:
                if nums2[j] == v + x:
                    j += 1
                    if j == len(nums2):
                        return x
        return nums2[0] - nums1[0]


if __name__ == '__main__':
    print(Solution().minimumAddedInteger(nums1=[4, 20, 16, 12, 8], nums2=[14, 18, 10]))
    print(Solution().minimumAddedInteger(nums1=[3, 5, 5, 3], nums2=[7, 7]))
