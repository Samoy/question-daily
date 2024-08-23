# https://leetcode.cn/problems/minimum-array-end/?envType=daily-question&envId=2024-08-22
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bit_count = n.bit_length() + x.bit_count()
        res, j = x, 0
        m = n - 1
        for i in range(bit_count):
            if ((res >> i) & 1) == 0:
                if ((m >> j) & 1) != 0:
                    res |= (1 << i)
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minEnd(n=3, x=4))
    print(s.minEnd(n=2, x=7))
