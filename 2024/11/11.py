from typing import List


# https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/?envType=daily-question&envId=2024-11-11
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 对 cuts 进行排序，并在两端添加 0 和 n
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)

        # 初始化动态规划表
        dp = [[0] * m for _ in range(m)]

        # 填充动态规划表
        for i in range(m - 3, -1, -1):  # 从后往前遍历，确保子问题已经解决
            for j in range(i + 2, m):  # 从前往后遍历，确保区间长度至少为 2
                # 计算在区间 [i, j] 内进行切割的最小成本
                # 选择一个中间点 k，使得 i < k < j
                # dp[i][j] = min(dp[i][k] + dp[k][j]) + 当前区间的长度 (cuts[j] - cuts[i])
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]

        # 返回最终结果，即在整个木棍 [0, n] 上进行切割的最小成本
        return dp[0][-1]


if __name__ == '__main__':
    print(Solution().minCost(n=7, cuts=[1, 3, 4, 5]))
    print(Solution().minCost(n=9, cuts=[5, 6, 1, 4, 2]))
