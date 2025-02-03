from typing import List


# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/?envType=daily-question&envId=2025-02-01
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[right]:
                return target > nums[right] and x >= target
            return target > nums[right] or x >= target

        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif check(mid):
                right = mid
            else:
                left = mid
        return nums[right] == target


if __name__ == '__main__':
    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3))
