from heapq import heapify, heappop, heappush
from typing import List


# https://leetcode.cn/problems/maximum-spending-after-buying-items/?envType=daily-question&envId=2024-12-12
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        h = [(a[-1], i) for i, a in enumerate(values)]
        heapify(h)
        ans = 0
        for d in range(1, len(values) * len(values[0]) + 1):
            v, i = heappop(h)
            ans += v * d
            values[i].pop()
            if values[i]:
                heappush(h, (values[i][-1], i))
        return ans


if __name__ == '__main__':
    print(Solution().maxSpending(values=[[8, 5, 2], [6, 4, 1], [9, 7, 3]]))
    print(Solution().maxSpending(values=[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]))
