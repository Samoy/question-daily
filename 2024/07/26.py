from typing import List


# https://leetcode.cn/problems/find-the-value-of-the-partition/?envType=daily-question&envId=2024-07-26
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))


if __name__ == '__main__':
    print(Solution().findValueOfPartition([1, 3, 2, 4]))
    print(Solution().findValueOfPartition([100, 1, 10]))
