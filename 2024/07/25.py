# https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/?envType=daily-question&envId=2024-07-25
class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        found0 = found5 = False
        for i in range(n - 1, -1, -1):
            c = num[i]
            if found0 and c in "05" or found5 and c in "27":
                return n - i - 2
            if c == '0':
                found0 = True
            elif c == '5':
                found5 = True
        return n - found0


if __name__ == '__main__':
    print(Solution().minimumOperations("2245047"))
    print(Solution().minimumOperations("2908305"))
    print(Solution().minimumOperations("10"))
