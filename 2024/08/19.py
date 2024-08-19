MOD = 1_000_000_007
MX = 100_001

f = [[[0] * 3, [0] * 3] for _ in range(MX)]
f[0] = [[1] * 3, [1] * 3]
for i in range(1, MX):
    for j in range(2):
        for k in range(3):
            res = f[i - 1][j][0]
            if j == 0:
                res += f[i - 1][1][0]
            if k < 2:
                res += f[i - 1][j][k + 1]
            f[i][j][k] = res % MOD


# https://leetcode.cn/problems/student-attendance-record-ii/?envType=daily-question&envId=2024-08-19
class Solution:
    def checkRecord(self, n: int) -> int:
        return f[n][0][0]


if __name__ == '__main__':
    print(Solution().checkRecord(2))
    print(Solution().checkRecord(1))
    print(Solution().checkRecord(10101))
