from typing import List


# https://leetcode.cn/problems/target-sum/?envType=daily-question&envId=2024-06-30
class Solution:
    """
    给你一个非负整数数组 nums 和一个整数 target 。
    向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
    例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
    返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 计算目标差值，若差值为负或为奇数，则无法通过加减操作达到目标，提前返回0
        diff = sum(nums) - target
        if diff < 0 or diff % 2 != 0:
            return 0

        # 初始化变量
        n, neg = len(nums), diff // 2  # n为数组长度，neg为目标差值除以2后的非负整数部分

        # 初始化动态规划表，dp[i][j]表示前i个数构成j为目标差值一半的方案数
        dp = [[0] * (neg + 1) for _ in range(n + 1)]  # 初始化二维列表，避免引用复制问题
        dp[0][0] = 1  # base case，没有数字时，差值为0的方案有1种（即不选任何数）

        # 动态规划填表
        for i in range(1, n + 1):  # 遍历每个数字
            num = nums[i - 1]  # 当前考虑的数字
            for j in range(0, neg + 1):  # 遍历所有可能的目标差值一半的范围
                # 不选择当前数字或选择当前数字并减去它的值两种情况之和
                dp[i][j] = dp[i - 1][j]  # 不选当前数字
                if j >= num:  # 如果当前差值允许选当前数字
                    dp[i][j] += dp[i - 1][j - num]  # 选择当前数字，更新方案数

        # 最终答案为dp[n][neg]，即所有数字都考虑过，且达到原问题中target差值一半时的方案数
        return dp[n][neg]


if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().findTargetSumWays([1], 1))
    print(Solution().findTargetSumWays([1, 2, 1], 2))
    print(Solution().findTargetSumWays([22, 19, 36, 28, 48, 24, 20, 23, 10, 18, 28, 1, 41, 49, 12, 21, 48, 2, 40, 44],
                                       14))
