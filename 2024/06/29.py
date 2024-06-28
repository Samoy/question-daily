# https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/?envType=daily-question&envId=2024-06-29
class Solution:
    """
    给你一个用字符串表示的正整数 num ，请你以字符串形式返回不含尾随零的整数 num 。
    """

    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


if __name__ == '__main__':
    print(Solution().removeTrailingZeros("51230100"))
    print(Solution().removeTrailingZeros("123"))
