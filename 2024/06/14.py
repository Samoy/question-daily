from math import inf
from typing import List


# https://leetcode.cn/problems/visit-array-positions-to-maximize-score/description/?envType=daily-question&envId=2024-06-14
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # 初始化结果为数组的第一个元素，因为从位置0开始
        res = nums[0]

        # 初始化动态规划数组dp，大小为2，分别对应当前位置数字为偶数和奇数的最大得分
        # 初始化值为负无穷大，保证初次赋值后可以正常更新
        dp = [-inf, -inf]

        # 根据nums[0]的奇偶性设置dp的初始值
        # dp[nums[0] & 1] 表示当前数字结尾且奇偶性与nums[0]相同的最大得分
        dp[nums[0] & 1] = nums[0]

        # 遍历数组剩余部分
        for i in range(1, len(nums)):
            # 计算当前数字的奇偶性
            parity = nums[i] & 1

            # 计算两种情况下的最大得分：
            # 1. 当前数字与dp中相同奇偶性的位置相连（无需扣除x）
            # 2. 当前数字与dp中不同奇偶性的位置相连（需扣除x）
            # 取这两种情况的最大值作为当前位置的最优解
            cur = max(dp[parity] + nums[i], dp[1 - parity] - x + nums[i])

            # 更新全局最大得分res
            res = max(res, cur)
            # 更新dp数组，保持dp[parity]为以当前数字nums[i]结尾且奇偶性匹配的最大得分
            dp[parity] = max(dp[parity], cur)

        # 返回最终的最大得分
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([2, 3, 6, 1, 9, 2], 5))
    print(s.maxScore([2, 4, 6, 8], 3))
