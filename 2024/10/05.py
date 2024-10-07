from bisect import bisect_left
from typing import List

# https://leetcode.cn/problems/minimum-time-to-complete-trips/description/?envType=daily-question&envId=2024-10-05
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        f = lambda x: sum(x // t for t in time)
        min_t = min(time)
        avg = (totalTrips - 1) // len(time) + 1
        # bisect_left 需要用左闭右开区间
        left = min_t * avg
        right = min(max(time) * avg, min_t * totalTrips)
        return bisect_left(range(right), totalTrips, left, key=f)


if __name__ == '__main__':
    print(Solution().minimumTime(time=[1, 2, 3], totalTrips=5))
    print(Solution().minimumTime(time=[2], totalTrips=1))
