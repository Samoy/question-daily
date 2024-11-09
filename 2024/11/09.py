from typing import List


# https://leetcode.cn/problems/design-neighbor-sum-service/?envType=daily-question&envId=2024-11-09
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.value_map = {}
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                self.value_map[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        # 求出该值对应的位置
        row, col = self.value_map[value]
        top, bottom, left, right = 0, 0, 0, 0
        if row > 0:  # 说明上方有元素
            top = self.grid[row - 1][col]
        if row < self.row - 1:  # 说明下方有元素
            bottom = self.grid[row + 1][col]
        if col > 0:  # 说明左方有元素
            left = self.grid[row][col - 1]
        if col < self.col - 1:  # 说明右方有元素
            right = self.grid[row][col + 1]
        return top + bottom + left + right

    def diagonalSum(self, value: int) -> int:
        row, col = self.value_map[value]
        top_left, bottom_left, top_right, bottom_right = 0, 0, 0, 0
        if row > 0 and col > 0:  # 说明左上角有元素
            top_left = self.grid[row - 1][col - 1]
        if row < self.row - 1 and col > 0:  # 说明坐下方有元素
            bottom_left = self.grid[row + 1][col - 1]
        if row > 0 and col < self.col - 1:  # 说明右上方有元素
            top_right = self.grid[row - 1][col + 1]
        if row < self.row - 1 and col < self.col - 1:  # 说明右下方有元素
            bottom_right = self.grid[row + 1][col + 1]
        return top_left + bottom_left + top_right + bottom_right


if __name__ == '__main__':
    sum1 = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(sum1.adjacentSum(1))
    print(sum1.adjacentSum(4))
    print(sum1.diagonalSum(4))
    print(sum1.diagonalSum(8))

    sum2 = NeighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
    print(sum2.adjacentSum(15))
    print(sum2.diagonalSum(9))
