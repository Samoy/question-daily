from typing import List


# https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/?envType=daily-question&envId=2024-08-30
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        # 初始化答案变量为0
        ans = 0
        # `cnt` 是一个二维列表，用于统计每个位置上的数字出现次数
        # 初始化 `cnt` 为一个二维列表，大小为 [数位长度][10]，所有元素初始化为0
        cnt = [[0] * 10 for _ in str(nums[0])]

        # 遍历输入列表中的每个数字及其索引
        for k, x in enumerate(nums):
            # 初始化一个变量用于追踪当前数字的位数位置
            i = 0

            # 使用除法和取余来逐位处理数字
            while x:
                # 计算当前位的数字
                x, d = divmod(x, 10)

                # 更新答案：当前数字的位数在之前所有数字中不等于它的计数加到答案中
                # 这实际上是计算了之前所有数字与当前数字在相同位上的差异
                ans += k - cnt[i][d]

                # 更新计数：增加当前位数上该数字的出现次数
                cnt[i][d] += 1

                # 移动到下一个位数
                i += 1

        # 返回最终的答案
        return ans


if __name__ == '__main__':
    print(Solution().sumDigitDifferences([13, 23, 12]))
    print(Solution().sumDigitDifferences([10, 10, 10, 10]))
