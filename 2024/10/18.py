from typing import List


# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2024-10-18
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans if nums[-2] and nums[-1] else -1


if __name__ == '__main__':
    print(Solution().minOperations([0, 1, 1, 1, 0, 0]))
    print(Solution().minOperations([0, 1, 1, 1]))
