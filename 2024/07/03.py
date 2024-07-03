# https://leetcode.cn/problems/harshad-number/?envType=daily-question&envId=2024-07-03
class Solution:
    """
    如果一个整数能够被其各个数位上的数字之和整除，则称之为 哈沙德数（Harshad number）。
    给你一个整数 x 。如果 x 是 哈沙德数 ，则返回 x 各个数位上的数字之和，否则，返回 -1 。
    """

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s, num = 0, x
        while num > 0:
            s += num % 10
            num = num // 10
        return s if x % s == 0 else -1


if __name__ == '__main__':
    print(Solution().sumOfTheDigitsOfHarshadNumber(18))
    print(Solution().sumOfTheDigitsOfHarshadNumber(23))
