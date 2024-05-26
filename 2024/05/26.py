from typing import List


# https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/?envType=daily-question&envId=2024-05-26
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # 获取矩阵的行数m和列数n
        m, n = len(matrix), len(matrix[0])

        # 初始化一个前缀和二维数组pre，大小为(m+1) x (n+1)，用于存储所有子矩形的异或和
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        # 结果列表，用于存储所有坐标对应异或和
        results = list()

        # 遍历矩阵的所有元素，计算子矩形的异或和并添加到结果列表
        for i in range(1, m + 1):  # 行
            for j in range(1, n + 1):  # 列
                # 计算当前元素所在子矩形的异或和
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                # 将子矩形的异或和添加到结果列表
                results.append(pre[i][j])

        # 对结果列表进行降序排序
        results.sort(reverse=True)

        # 返回第k大的异或和（列表下标从0开始，所以返回第k-1个元素）
        return results[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.kthLargestValue([[5, 2], [1, 6]], 1))
    print(s.kthLargestValue([[5, 2], [1, 6]], 2))
    print(s.kthLargestValue([[5, 2], [1, 6]], 3))
    print(s.kthLargestValue([[5, 2], [1, 6]], 4))
