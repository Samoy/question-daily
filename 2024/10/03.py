from typing import List


# https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/?envType=daily-question&envId=2024-10-03
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        f = [[float("inf")] * n for _ in range(maxTime + 1)]
        f[0][0] = passingFees[0]
        for t in range(1, maxTime + 1):
            for i, j, cost in edges:
                if cost <= t:
                    f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i])
                    f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j])

        ans = min(f[t][n - 1] for t in range(1, maxTime + 1))
        return -1 if ans == float("inf") else ans


if __name__ == '__main__':
    print(Solution().minCost(maxTime=30, edges=[[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
                             passingFees=[5, 1, 2, 20, 20, 3]))
    print(Solution().minCost(maxTime=29, edges=[[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
                             passingFees=[5, 1, 2, 20, 20, 3]))
    print(Solution().minCost(maxTime=25, edges=[[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
                             passingFees=[5, 1, 2, 20, 20, 3]))
