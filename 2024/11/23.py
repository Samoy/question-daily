from typing import List


# https://leetcode.cn/problems/find-the-number-of-winning-players/?envType=daily-question&envId=2024-11-23
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnts = [[0] * 11 for _ in range(n)]
        for x, y in pick:
            cnts[x][y] += 1

        ans = 0
        for i, cnt in enumerate(cnts):
            if any(c > i for c in cnt):
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]))
    print(Solution().winningPlayerCount(n=5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]]))
    print(Solution().winningPlayerCount(n=5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]]))
