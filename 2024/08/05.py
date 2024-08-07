# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/?envType=daily-question&envId=2024-08-05
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = 0
        res = 0

        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res


if __name__ == '__main__':
    print(Solution().findIntegers(5))
    print(Solution().findIntegers(1))
    print(Solution().findIntegers(2))
