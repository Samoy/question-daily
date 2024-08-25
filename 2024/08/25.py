from functools import cache
from typing import List


# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/?envType=daily-question&envId=2024-08-25
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all_ = sum(nums)
        if all_ % k:
            return False
        per = all_ // k
        nums.sort()  # 方便下面剪枝
        if nums[-1] > per:
            return False
        n = len(nums)

        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):  # p + nums[i] 等于 per 时置为 0
                    return True
            return False

        return dfs((1 << n) - 1, 0)


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3))
