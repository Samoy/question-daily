from collections import defaultdict
from math import inf
from typing import List


# https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/?envType=daily-question&envId=2024-07-23
class Solution:
    mod = int(1e9 + 7)  # 定义模数

    def sumOfPowers(self, nums: List[int], k: int) -> int:
        n = len(nums)  # 获取数组长度
        res = 0  # 初始化结果变量
        d = [[defaultdict(int) for _ in range(k + 1)] for _ in range(n)]  # 初始化动态规划表
        nums.sort()  # 对输入数组进行排序

        # 遍历数组中的每一个元素
        for i in range(n):
            # 初始化单元素子序列的能量值为无穷大
            d[i][1][inf] = 1
            # 遍历当前元素之前的所有元素
            for j in range(i):
                diff = abs(nums[i] - nums[j])  # 计算当前元素与之前元素的差值绝对值
                # 遍历从2到k的所有子序列长度
                for p in range(2, k + 1):
                    # 遍历长度为p-1的子序列的能量值
                    for v, cnt in d[j][p - 1].items():
                        # 更新长度为p的子序列的能量值
                        d[i][p][min(diff, v)] = (d[i][p][min(diff, v)] + cnt) % self.mod

            # 计算长度为k的子序列的能量和
            for v, cnt in d[i][k].items():
                res = (res + v * cnt % self.mod) % self.mod
        return res  # 返回最终结果


if __name__ == '__main__':
    print(Solution().sumOfPowers([1, 2, 3, 4], 3))
    print(Solution().sumOfPowers([2, 2], 2))
    print(Solution().sumOfPowers([4, 3, -1], 2))
