# https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/?envType=daily-question&envId=2025-02-21
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        d = [float('inf')] * (n + 1)
        f = [float('inf')] * (n + 1)
        d[0] = 0

        for i in range(1, n + 1):
            d[i] = d[i - 1] + (1 if floor[i - 1] == '1' else 0)

        for _ in range(numCarpets):
            f[0] = 0
            for i in range(1, n + 1):
                f[i] = f[i - 1] + (1 if floor[i - 1] == '1' else 0)
                f[i] = min(f[i], d[max(0, i - carpetLen)])
            d, f = f, d

        return int(d[n])


if __name__ == '__main__':
    print(Solution().minimumWhiteTiles("10110101", 2, 2))
    print(Solution().minimumWhiteTiles("11111", 2, 3))
