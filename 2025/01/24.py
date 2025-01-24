from collections import deque
from typing import List


# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/description/?envType=daily-question&envId=2025-01-24
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque([(n + 1, 0)])  # 哨兵
        for i in range(n, 0, -1):
            while q[-1][0] > i * 2 + 1:  # 右边离开窗口
                q.pop()
            f = prices[i - 1] + q[-1][1]
            while f <= q[0][1]:
                q.popleft()
            q.appendleft((i, f))  # 左边进入窗口
        return q[0][1]


if __name__ == "__main__":
    print(Solution().minimumCoins([3, 1, 2]))
    print(Solution().minimumCoins([1, 10, 1, 1]))
    print(Solution().minimumCoins([26, 18, 6, 12, 49, 7, 45, 45]))
