from math import inf
from typing import List


# https://leetcode.cn/problems/minimize-manhattan-distances/description/?envType=daily-question&envId=2024-07-09
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        max_x1 = max_x2 = max_y1 = max_y2 = -inf
        min_x1 = min_x2 = min_y1 = min_y2 = inf
        max_xi = min_xi = max_yi = min_yi = 0

        for i, (x, y) in enumerate(points):
            x, y = x + y, y - x

            # x 最大次大
            if x > max_x1:
                max_x2 = max_x1
                max_x1 = x
                max_xi = i
            elif x > max_x2:
                max_x2 = x

            # x 最小次小
            if x < min_x1:
                min_x2 = min_x1
                min_x1 = x
                min_xi = i
            elif x < min_x2:
                min_x2 = x

            # y 最大次大
            if y > max_y1:
                max_y2 = max_y1
                max_y1 = y
                max_yi = i
            elif y > max_y2:
                max_y2 = y

            # y 最小次小
            if y < min_y1:
                min_y2 = min_y1
                min_y1 = y
                min_yi = i
            elif y < min_y2:
                min_y2 = y

        ans = inf
        for i in max_xi, min_xi, max_yi, min_yi:
            dx = (max_x2 if i == max_xi else max_x1) - (min_x2 if i == min_xi else min_x1)
            dy = (max_y2 if i == max_yi else max_y1) - (min_y2 if i == min_yi else min_y1)
            ans = min(ans, max(dx, dy))
        return ans


if __name__ == '__main__':
    print(Solution().minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))
    print(Solution().minimumDistance([[1, 1], [1, 1], [1, 1]]))
