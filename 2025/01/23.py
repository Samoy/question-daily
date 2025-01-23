from typing import List


# https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/?envType=daily-question&envId=2025-01-23
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        g = [[] for _ in coins]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> List[int]:
            s = [0] * 14
            for y in g[x]:
                if y != fa:
                    fy = dfs(y, x)
                    for j, v in enumerate(fy):
                        s[j] += v
            for j in range(13):
                s[j] = max((coins[x] >> j) - k + s[j], (coins[x] >> (j + 1)) + s[j + 1])
            s[13] += (coins[x] >> 13) - k
            return s

        return dfs(0, -1)[0]


if __name__ == "__main__":
    print(
        Solution().maximumPoints(
            edges=[[0, 1], [1, 2], [2, 3]], coins=[10, 10, 3, 3], k=5
        )
    )
    print(Solution().maximumPoints(edges=[[0, 1], [0, 2]], coins=[8, 4, 4], k=0))
