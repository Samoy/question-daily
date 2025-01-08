# https://leetcode.cn/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2025-01-08
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i] * 3)
        return ans


if __name__ == '__main__':
    print(Solution().largestGoodInteger('6777133339'))
    print(Solution().largestGoodInteger('2300019'))
    print(Solution().largestGoodInteger('42352338'))
