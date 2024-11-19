from math import inf
from typing import List


# https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/?envType=daily-question&envId=2024-11-19
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        frm = [[] for _ in range(n)]
        dp = list(range(n))
        ans = []
        for left, right in queries:
            frm[right].append(left)
            if dp[left] + 1 < dp[right]:
                dp[right] = dp[left] + 1
                for i in range(right + 1, n):
                    dp[i] = min(dp[i], dp[i - 1] + 1, min((dp[j] for j in frm[i]), default=inf) + 1)
            ans.append(dp[-1])
        return ans


if __name__ == '__main__':
    print(Solution().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))
    print(Solution().shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]))
