from functools import cache
from typing import List


# https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/description/?envType=daily-question&envId=2024-06-10
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, target: int) -> int:
            nonlocal done
            if done:
                return 0
            if i >= j:
                done = True
                return 0
            res = 0
            if nums[i] + nums[i + 1] == target:  # 删除前两个数
                res = max(res, dfs(i + 2, j, target) + 1)
            if nums[j - 1] + nums[j] == target:  # 删除后两个数
                res = max(res, dfs(i, j - 2, target) + 1)
            if nums[i] + nums[j] == target:  # 删除第一个和最后一个数
                res = max(res, dfs(i + 1, j - 1, target) + 1)
            return res

        done = False
        n = len(nums)
        res1 = dfs(2, n - 1, nums[0] + nums[1])  # 删除前两个数
        res2 = dfs(0, n - 3, nums[-2] + nums[-1])  # 删除后两个数
        res3 = dfs(1, n - 2, nums[0] + nums[-1])  # 删除第一个和最后一个数
        return max(res1, res2, res3) + 1  # 加上第一次操作


if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations([3, 2, 1, 2, 3, 4]))
    print(s.maxOperations([3, 2, 6, 1, 4]))
