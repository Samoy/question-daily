from typing import List


# https://leetcode.cn/problems/jump-game-ii/?envType=daily-question&envId=2025-01-27
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, cur_right, next_right = 0, 0, 0
        for i in range(len(nums) - 1):
            next_right = max(next_right, i + nums[i])
            if i == cur_right:
                cur_right = next_right
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([2, 3, 0, 1, 4]))
