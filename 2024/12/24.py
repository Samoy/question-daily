from heapq import heappop, heappush
from typing import List


# https://leetcode.cn/problems/maximum-number-of-eaten-apples/?envType=daily-question&envId=2024-12-24
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = i = 0
        h = []
        while i < len(apples) or h:
            while h and h[0][0] == i:  # 已腐烂
                heappop(h)
            if i < len(apples) and apples[i]:
                heappush(h, [i + days[i], apples[i]])
            if h:
                ans += 1
                h[0][1] -= 1  # 吃一个最早腐烂的苹果
                if h[0][1] == 0:
                    heappop(h)
            i += 1
        return ans


if __name__ == '__main__':
    print(Solution().eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
    print(Solution().eatenApples(apples=[3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))
