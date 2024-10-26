from typing import List


# https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/?envType=daily-question&envId=2024-10-26
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # 初始化状态变量 f，初始值为 1，表示总奖励为 0 的状态
        f = 1

        # 遍历排序并去重后的奖励值
        for v in sorted(set(rewardValues)):
            # 位运算部分：
            # (1 << v) - 1 生成一个从第 0 位到第 v-1 位全为 1 的二进制数
            # f & ((1 << v) - 1) 取出 f 中从第 0 位到第 v-1 位的值
            # (f & ((1 << v) - 1)) << v 将上述结果左移 v 位
            # f |= ... 将上述结果与 f 进行按位或运算，更新 f
            f |= (f & ((1 << v) - 1)) << v

        # 返回 f 的二进制表示的位数减 1，即为最大总奖励
        return f.bit_length() - 1


if __name__ == '__main__':
    print(Solution().maxTotalReward([1, 1, 3, 3]))
    print(Solution().maxTotalReward([1, 6, 4, 3, 2]))
