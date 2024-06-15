from typing import List


# https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/description/?envType=daily-question&envId=2024-06-15
class Solution:
    """
    给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。
    在一步操作中，你可以执行下述指令：
      1. 在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
      2.将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
    数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。
    对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。
    注意：你 只 能对每个下标执行 一次 此操作。
    数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。
    """

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # 找到nums中的最大值，用于确定差分数组的大小，确保覆盖所有可能的变换范围
        m = max(nums)
        # 初始化差分数组，大小为m+2，用于记录每个数值段的“密度”变化
        diff = [0] * (m + 2)
        # 遍历nums中的每个元素，根据其变换范围更新差分数组
        for x in nums:
            # 更新差分数组，使x-k到x+k范围内（含边界）的值增加1，表示这个范围的“密度”增加
            diff[max(x - k, 0)] += 1
            # 在x+k+1位置减1，完成范围的闭合，保证只在有效的变换范围内计数
            diff[min(x + k + 1, m + 1)] -= 1
        # 初始化结果变量和计数器
        res, count = 0, 0
        # 遍历差分数组，累加差分值以得到连续相等子序列的当前长度
        for x in diff:
            count += x  # 累加当前差分值到计数器
            res = max(res, count)  # 更新最大美丽值（最长连续相等子序列长度）
        # 返回最大美丽值
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maximumBeauty([4, 6, 1, 2], 2))
    print(s.maximumBeauty([1, 1, 1, 1], 10))
    print(s.maximumBeauty([12, 71], 10))
