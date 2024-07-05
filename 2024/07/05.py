from typing import List


# https://leetcode.cn/problems/modify-the-matrix/description/?envType=daily-question&envId=2024-07-05
class Solution:
    """
    给你一个下标从 0 开始、大小为 m x n 的整数矩阵 matrix ，新建一个下标从 0 开始、名为 answer 的矩阵。
    使 answer 与 matrix 相等，接着将其中每个值为 -1 的元素替换为所在列的 最大 元素。
    返回矩阵 answer 。
    """

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            max_num = max([matrix[j][i] for j in range(m)])
            for j in range(m):
                if matrix[j][i] == -1:
                    matrix[j][i] = max_num
        return matrix


if __name__ == '__main__':
    print(Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]))
    print(Solution().modifiedMatrix([[3, -1], [5, 2]]))
