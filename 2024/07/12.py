from typing import List


# https://leetcode.cn/problems/minimum-number-game/?envType=daily-question&envId=2024-07-12
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == '__main__':
    print(Solution().numberGame([5, 4, 2, 3]))
    print(Solution().numberGame([2, 5]))
    print(Solution().numberGame([2, 5, 3, 1, 8, 10]))
