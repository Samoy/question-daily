from typing import List


# https://leetcode.cn/problems/intersection-of-two-arrays-ii/?envType=daily-question&envId=2025-01-30
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 如果保证 nums1 和 nums2 是有序的，排序可以去掉
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            x, y = nums1[i], nums2[j]
            if x < y:
                i += 1
            elif x > y:
                j += 1
            else:
                ans.append(x)
                i += 1
                j += 1
        return ans


if __name__ == '__main__':
    print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
