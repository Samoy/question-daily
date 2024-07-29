from typing import List


# https://leetcode.cn/problems/falling-squares/?envType=daily-question&envId=2024-07-28
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        heights = [0] * n
        for i, (left1, side1) in enumerate(positions):
            right1 = left1 + side1 - 1
            heights[i] = side1
            for j in range(i):
                left2, right2 = positions[j][0], positions[j][0] + positions[j][1] - 1
                if right1 >= left2 and right2 >= left1:
                    heights[i] = max(heights[i], heights[j] + side1)
        for i in range(1, n):
            heights[i] = max(heights[i], heights[i - 1])
        return heights


if __name__ == '__main__':
    print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
    print(Solution().fallingSquares([[100, 100], [200, 100]]))
