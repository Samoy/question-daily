from collections import defaultdict, deque
from typing import List


# https://leetcode.cn/problems/bus-routes/?envType=daily-question&envId=2024-09-17
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1 if source != target else 0

        # BFS
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()
            dis_x = dis[x]
            for i in stop_to_buses[x]:
                if routes[i]:
                    for y in routes[i]:
                        if y not in dis:
                            dis[y] = dis_x + 1
                            q.append(y)
                    routes[i] = None

        return dis.get(target, -1)


if __name__ == '__main__':
    print(Solution().numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
    print(Solution().numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6]], source=15, target=12))
