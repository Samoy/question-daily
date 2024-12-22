# https://leetcode.cn/problems/sort-integers-by-the-power-value/?envType=daily-question&envId=2024-12-22
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_power(n):
            count = 0
            while n != 1:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3 * n + 1
                count += 1
            return count

        return sorted(range(lo, hi + 1), key=lambda x: (get_power(x), x))[k - 1]


if __name__ == '__main__':
    print(Solution().getKth(12, 15, 2))
    print(Solution().getKth(7, 11, 4))
