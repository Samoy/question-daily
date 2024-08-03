from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/maximum-points-inside-the-square/?envType=daily-question&envId=2024-08-03
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_distance = defaultdict(lambda: float('inf'))
        min2 = float('inf')
        for (x, y), c in zip(points, s):
            d = max(abs(x), abs(y))
            if d < min_distance[c]:
                min2 = min(min2, min_distance[c])
                min_distance[c] = d
            else:
                min2 = min(min2, d)
        return sum(d < min2 for d in min_distance.values())


if __name__ == '__main__':
    print(Solution().maxPointsInsideSquare([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], "abdca"))
    print(Solution().maxPointsInsideSquare([[1, 1], [-2, -2], [-2, 2]], "abb"))
    print(Solution().maxPointsInsideSquare([[1, 1], [-1, -1], [2, -2]], "ccd"))
