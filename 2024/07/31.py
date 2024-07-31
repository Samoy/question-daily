from typing import List


# https://leetcode.cn/problems/minimum-rectangles-to-cover-points/?envType=daily-question&envId=2024-07-31
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key=lambda p: p[0])
        ans = 0
        x2 = -1
        for x, _ in points:
            if x > x2:
                ans += 1
                x2 = x + w
        return ans


if __name__ == '__main__':
    print(Solution().minRectanglesToCoverPoints(points=[[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], w=1))
    print(Solution().minRectanglesToCoverPoints(points=[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], w=2))
    print(Solution().minRectanglesToCoverPoints(points=[[2, 3], [1, 2]], w=0))
