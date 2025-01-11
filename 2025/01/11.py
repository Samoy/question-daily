# https://leetcode.cn/problems/find-the-key-of-the-numbers/?envType=daily-question&envId=2025-01-11
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = 0
        pow10 = 1
        while num1 and num2 and num3:
            ans += min(num1 % 10, num2 % 10, num3 % 10) * pow10
            num1 //= 10
            num2 //= 10
            num3 //= 10
            pow10 *= 10
        return ans


if __name__ == '__main__':
    print(Solution().generateKey(num1=1, num2=10, num3=1000))
    print(Solution().generateKey(num1=987, num2=879, num3=798))
    print(Solution().generateKey(num1=1, num2=2, num3=3))
