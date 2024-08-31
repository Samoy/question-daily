from typing import List


# https://leetcode.cn/problems/make-a-square-with-the-same-color/?envType=daily-question&envId=2024-08-31
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def can(i_start, i_util, j_start, j_util):
            white, black = 0, 0
            for i in range(i_start, i_util):
                for j in range(j_start, j_util):
                    if grid[i][j] == "B":
                        black += 1
                    else:
                        white += 1
            if abs(white - black):
                return True

        # 左上角
        if can(0, 2, 0, 2):
            return True
        # 右上角
        if can(0, 2, 1, 3):
            return True
        # 左下角
        if can(1, 3, 0, 2):
            return True
        # 右下角
        if can(1, 3, 1, 3):
            return True
        return False


if __name__ == '__main__':
    print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
    print(Solution().canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
    print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]))
