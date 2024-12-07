from functools import lru_cache


# https://leetcode.cn/problems/knight-probability-in-chessboard/?envType=daily-question&envId=2024-12-07
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return (dfs := lru_cache(None)(lambda x, y, s:
                                       sum(dfs(x + i, y + j, s + 1) for i, j in
                                           [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1],
                                            [2, -1], [-2,
                                                      -1]]) / 8 if 0 <= x < n and 0 <= y < n and s <= k else s > k))(
            row, column, 0)


if __name__ == '__main__':
    print(Solution().knightProbability(n=3, k=2, row=0, column=0))
    print(Solution().knightProbability(n=1, k=0, row=0, column=0))
