from heapq import heappush, heappop
from math import inf
from typing import List


# https://leetcode.cn/problems/network-delay-time/?envType=daily-question&envId=2024-11-25
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, d in times:
            g[x - 1].append((y - 1, d))

        dis = [inf] * n
        dis[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heappush(h, (new_dis, y))
        mx = max(dis)
        return mx if mx < inf else -1


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
    print(Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
