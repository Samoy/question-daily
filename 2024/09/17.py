from collections import defaultdict, deque
from typing import List

# https://leetcode.cn/problems/bus-routes/?envType=daily-question&envId=2024-09-17
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 记录经过车站 x 的公交车编号
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)

        # 小优化：如果没有公交车经过起点或终点，直接返回
        if source not in stop_to_buses or target not in stop_to_buses:
            # 注意原地 TP 的情况
            return -1 if source != target else 0

        # BFS
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()  # 当前在车站 x
            dis_x = dis[x]
            for i in stop_to_buses[x]:  # 遍历所有经过车站 x 的公交车 i
                if routes[i]:
                    for y in routes[i]:  # 遍历公交车 i 的路线
                        if y not in dis:  # 没有访问过车站 y
                            dis[y] = dis_x + 1  # 从 x 站上车然后在 y 站下车
                            q.append(y)
                    routes[i] = None  # 标记 routes[i] 遍历过

        return dis.get(target, -1)

if __name__ == '__main__':
    print(Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
    print(Solution().numBusesToDestination(routes = [[7,12],[4,5,15],[6]], source = 15, target = 12))
