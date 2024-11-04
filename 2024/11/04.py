from math import isqrt


# https://leetcode.cn/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-11-04
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a * 2 <= c:
            b = isqrt(c - a * a)
            if a * a + b * b == c:
                return True
            a += 1
        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(3))
