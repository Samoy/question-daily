from typing import List


# https://leetcode.cn/problems/available-captures-for-rook/?envType=daily-question&envId=2024-12-06
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt, st, ed = 0, 0, 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    st, ed = i, j
        for i in range(4):
            step = 0
            while True:
                tx = st + step * dx[i]
                ty = ed + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    cnt += 1
                    break
                step += 1
        return cnt


if __name__ == '__main__':
    print(Solution().numRookCaptures(
        [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
    print(Solution().numRookCaptures(
        [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
    print(Solution().numRookCaptures(
        [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
