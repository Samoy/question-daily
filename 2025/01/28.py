from typing import List


# https://leetcode.cn/problems/pascals-triangle-ii/?envType=daily-question&envId=2025-01-28
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        return row


if __name__ == '__main__':
    print(Solution().getRow(3))
    print(Solution().getRow(0))
    print(Solution().getRow(1))
