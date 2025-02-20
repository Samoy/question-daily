from typing import List


# https://leetcode.cn/problems/number-of-even-and-odd-bits/?envType=daily-question&envId=2025-02-20
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        for i in range(32):
            if n & (1 << i) != 0:
                res[i % 2] += 1
        return res


if __name__ == '__main__':
    print(Solution().evenOddBit(17))
    print(Solution().evenOddBit(2))
