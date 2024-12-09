# https://leetcode.cn/problems/determine-color-of-a-chessboard-square/?envType=daily-question&envId=2024-12-09
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) ^ int(coordinates[1])) & 1 == 1


if __name__ == '__main__':
    print(Solution().squareIsWhite(coordinates="a1"))
    print(Solution().squareIsWhite(coordinates="h3"))
    print(Solution().squareIsWhite(coordinates="c7"))
