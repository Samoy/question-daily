from typing import List


# https://leetcode.cn/problems/distance-between-bus-stops/?envType=daily-question&envId=2024-09-16
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))


if __name__ == '__main__':
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1))
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2))
    print(Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3))
