from typing import List


# https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/description/?envType=daily-question&envId=2024-06-25
class Solution:
    """
    给你一个下标从 0 开始大小为 m x n 的二进制矩阵 grid 。
    从原矩阵中选出若干行构成一个行的 非空 子集，如果子集中任何一列的和至多为子集大小的一半，那么我们称这个子集是 好子集。
    更正式的，如果选出来的行子集大小（即行的数量）为 k，那么每一列的和至多为 floor(k / 2) 。
    请你返回一个整数数组，它包含好子集的行下标，请你将子集中的元素 升序 返回。
    如果有多个好子集，你可以返回任意一个。如果没有好子集，请你返回一个空数组。
    一个矩阵 grid 的行 子集 ，是删除 grid 中某些（也可能不删除）行后，剩余行构成的元素集合。
    """

    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        mask_to_idx = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0:
                return [i]
            mask_to_idx[mask] = i

        for x, i in mask_to_idx.items():
            for y, j in mask_to_idx.items():
                if (x & y) == 0:
                    return sorted((i, j))
        return []


if __name__ == '__main__':
    print(Solution().goodSubsetofBinaryMatrix([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]))  # [0,1]
    print(Solution().goodSubsetofBinaryMatrix([[0]]))  # [0]
    print(Solution().goodSubsetofBinaryMatrix([[1, 1, 1], [1, 1, 1]]))  # []
