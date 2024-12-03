# https://leetcode.cn/problems/check-if-two-chessboard-squares-have-the-same-color/?envType=daily-question&envId=2024-12-03
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = ord(coordinate1[0]) - ord("a"), int(coordinate1[1]) - 1
        x2, y2 = ord(coordinate2[0]) - ord("a"), int(coordinate2[1]) - 1
        return (x1 + y1) % 2 == (x2 + y2) % 2


if __name__ == '__main__':
    print(Solution().checkTwoChessboards(coordinate1="a1", coordinate2="c3"))
    print(Solution().checkTwoChessboards(coordinate1="a1", coordinate2="h3"))
