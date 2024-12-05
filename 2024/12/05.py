# https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/?envType=daily-question&envId=2024-12-05
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 车与皇后处在同一行，且中间没有象
        if a == e and (c != a or d <= min(b, f) or d >= max(b, f)):
            return 1
        # 车与皇后处在同一列，且中间没有象
        if b == f and (d != b or c <= min(a, e) or c >= max(a, e)):
            return 1
        # 象、皇后处在同一条对角线，且中间没有车
        if abs(c - e) == abs(d - f) and ((c - e) * (b - f) != (a - e) * (d - f) or a < min(c, e) or a > max(c, e)):
            return 1
        return 2


if __name__ == '__main__':
    print(Solution().minMovesToCaptureTheQueen(a=1, b=1, c=8, d=8, e=2, f=3))
    print(Solution().minMovesToCaptureTheQueen(a=5, b=3, c=3, d=4, e=5, f=2))
