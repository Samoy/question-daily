from typing import List


# https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/?envType=daily-question&envId=2024-07-17
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        opened = [0] * n
        for mask in range(1 << n):
            for i in range(n):
                opened[i] = mask & (1 << i)
            d = [[1000000] * n for _ in range(n)]
            for i, j, r in roads:
                if opened[i] > 0 and opened[j] > 0:
                    d[i][j] = d[j][i] = min(d[i][j], r)
            for k in range(n):
                if opened[k] > 0:
                    for i in range(n):
                        if opened[i] > 0:
                            for j in range(i + 1, n):
                                if opened[j] > 0:
                                    d[i][j] = d[j][i] = min(d[i][j], d[i][k] + d[k][j])
            good = 1
            for i in range(n):
                if opened[i] > 0:
                    for j in range(i + 1, n):
                        if opened[j] > 0:
                            if d[i][j] > maxDistance:
                                good = 0
                                break
                if good == 0:
                    break
            res += good
        return res


if __name__ == '__main__':
    print(Solution().numberOfSets(3, 5, [[0, 1, 2], [1, 2, 10], [0, 2, 10]]))
    print(Solution().numberOfSets(3, 5, [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]))
    print(Solution().numberOfSets(1, 10, []))
