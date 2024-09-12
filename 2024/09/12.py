from typing import List


# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/?envType=daily-question&envId=2024-09-12
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2 + 1
        while left + 1 < right:
            k = (left + right) // 2
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k
        return left * 2


if __name__ == '__main__':
    print(Solution().maxNumOfMarkedIndices([3, 5, 2, 4]))
    print(Solution().maxNumOfMarkedIndices([9, 2, 5, 4]))
    print(Solution().maxNumOfMarkedIndices([7, 6, 8]))
