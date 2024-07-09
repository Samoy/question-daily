from typing import List


# https://leetcode.cn/problems/find-pivot-index/description/?envType=daily-question&envId=2024-07-09
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
    print(Solution().pivotIndex([1, 2, 3]))
    print(Solution().pivotIndex([2, 1, -1]))
