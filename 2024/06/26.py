from typing import List


# https://leetcode.cn/problems/special-permutations/?envType=daily-question&envId=2024-06-26
class Solution:
    """
    给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：
    对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
    请你返回特别排列的总数目，由于答案可能很大，请将它对 109 + 7 取余 后返回。
    """

    def specialPerm(self, a: List[int]) -> int:
        # 定义模数
        mod = 10 ** 9 + 7
        # 数组长度
        n = len(a)
        # 构建状态转移掩码，1 << n 代表所有元素都被选中的状态
        m = 1 << n
        # 初始化动态规划表，f[state][last_index] 表示当前状态state且以a[last_index]结尾的满足条件的排列数目
        f = [[0] * n for _ in range(m)]

        # 遍历单个元素构成的“排列”
        for i in range(n):
            f[1 << i][i] = 1  # 每个元素单独作为一个序列，计数为1

        # 遍历所有可能的状态（从只有一个元素被选中到所有元素都被选中）
        for s in range(m - 1):  # 不包括所有元素都被选中的状态
            # 获取当前状态下的排列计数
            dr = f[s]
            for i in range(n):  # 遍历所有元素
                # 如果当前元素不在状态s中或者dr[i]为0，跳过
                if s >> i & 1 == 0 or dr[i] == 0:
                    continue
                # 记录前一个选取的元素
                pre = a[i]
                for j in range(n):  # 再次遍历，尝试添加新元素
                    # 如果当前j位置的元素已经在状态s中，跳过
                    if s >> j & 1:
                        continue
                    # 当前考虑的元素
                    cur = a[j]
                    # 判断是否满足整除条件
                    if pre % cur == 0 or cur % pre == 0:
                        # 更新状态转移：选择j作为下一个元素的排列数累加
                        f[s | 1 << j][j] += dr[i]

        # 最终结果为所有可能的结束状态的排列数之和，再对mod取余
        return sum(f[-1]) % mod


if __name__ == '__main__':
    print(Solution().specialPerm([2, 3, 6]))
    print(Solution().specialPerm([1, 4, 3]))
