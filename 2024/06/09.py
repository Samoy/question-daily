from typing import List


# https://leetcode.cn/problems/burst-balloons/description/?envType=daily-question&envId=2024-06-10
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 获取气球数量并初始化一个大小为 n+2 的新数组，用于动态规划记录最大硬币数
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]

        # 在气球序列首尾各加一个值为1的虚拟气球，以简化边界处理
        val = [1] + nums + [1]

        # 反向遍历气球，避免重复计算
        for i in range(n - 1, -1, -1):
            # 遍历当前气球到末尾的所有可能的最后一个被戳破的气球
            for j in range(i + 2, n + 2):
                # 遍历此区间内所有可能戳破的气球
                for k in range(i + 1, j):
                    # 计算当前戳破方案可获得的硬币总数
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]

                    # 更新从i到j区间内能获得的最大硬币数
                    rec[i][j] = max(rec[i][j], total)

        # 返回从第一个到最后一个气球（即整个序列）能得到的最大硬币数
        return rec[0][n + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))
    print(s.maxCoins([1, 5]))
