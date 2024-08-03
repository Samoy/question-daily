from typing import List


# https://leetcode.cn/problems/right-triangles/?envType=daily-question&envId=2024-08-02
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        col_sum = [sum(col) - 1 for col in zip(*grid)]
        ans = 0
        for row in grid:
            row_sum = sum(row) - 1
            ans += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)
        return ans


if __name__ == '__main__':
    print(Solution().numberOfRightTriangles([[0, 1, 0], [0, 1, 1], [0, 1, 0]]))
    print(Solution().numberOfRightTriangles([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
    print(Solution().numberOfRightTriangles([[1, 0, 1], [1, 0, 0], [1, 0, 0]]))
