from heapq import heappop, heappush
from typing import List


# https://leetcode.cn/problems/minimum-number-of-refueling-stops/description/?envType=daily-question&envId=2024-10-07
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        ans = pre_position = 0
        cur_fuel = startFuel
        fuel_heap = []  # 下面把堆中元素取反，当作最大堆用
        for position, fuel in stations:
            cur_fuel -= position - pre_position  # 每行驶 1 英里用掉 1 升汽油
            while fuel_heap and cur_fuel < 0:  # 没油了
                cur_fuel -= heappop(fuel_heap)  # 选油量最多的油桶
                ans += 1
            if cur_fuel < 0:  # 无法到达
                return -1
            heappush(fuel_heap, -fuel)  # 留着后面加油
            pre_position = position
        return ans


if __name__ == '__main__':
    print(Solution().minRefuelStops(target=1, startFuel=1, stations=[]))
    print(Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]))
    print(Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
