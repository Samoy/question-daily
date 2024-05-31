from typing import List


# https://leetcode.cn/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2024-05-31
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 使用列表中的数字作为下标来解决
        # 下标为2的就是出现两次的
        # 下标为0的就是出现0次的
        n = len(grid)
        count = [0] * (n * n + 1)
        count[0] = -1
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        return [count.index(2), count.index(0)]


if __name__ == '__main__':
    s = Solution()
    print(s.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
    print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
