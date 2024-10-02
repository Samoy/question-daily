from bisect import bisect_left
from typing import List


# https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/?envType=daily-question&envId=2024-10-02
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        h100 = round(hour * 100)  # 下面不会用到任何浮点数
        delta = h100 - (n - 1) * 100
        if delta <= 0:  # 无法到达终点
            return -1

        max_dist = max(dist)
        if h100 <= n * 100:  # 特判
            # 见题解中的公式
            return max(max_dist, (dist[-1] * 100 - 1) // delta + 1)

        def check(v: int) -> bool:
            t = n - 1  # n-1 个上取整中的 +1 先提出来
            for d in dist[:-1]:
                t += (d - 1) // v
            return (t * v + dist[-1]) * 100 <= h100 * v

        h = h100 // (n * 100)
        return bisect_left(range((max_dist - 1) // h + 1), True, 1, key=check)


if __name__ == '__main__':
    print(Solution().minSpeedOnTime([1, 3, 2], 6))
    print(Solution().minSpeedOnTime([1, 3, 2], 2.7))
    print(Solution().minSpeedOnTime([1, 3, 2], 1.9))
