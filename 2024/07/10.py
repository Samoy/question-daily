from typing import List


# https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/?envType=daily-question&envId=2024-07-10
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = 1
        while left < n and nums[left - 1] < nums[left]:
            left += 1
        res += left + (left < n)
        for r in range(n - 2, -1, -1):
            while left > 0 and nums[left - 1] >= nums[r + 1]:
                left -= 1
            res += left + (left <= r)
            if nums[r] >= nums[r + 1]:
                break
        return res


if __name__ == '__main__':
    print(Solution().incremovableSubarrayCount([1, 2, 3, 4]))
    print(Solution().incremovableSubarrayCount([6, 5, 7, 8]))
    print(Solution().incremovableSubarrayCount([8, 7, 6, 6]))
