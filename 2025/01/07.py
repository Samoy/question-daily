# https://leetcode.cn/problems/number-of-changing-keys?envType=daily-question&envId=2025-01-07
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(1 for i in range(len(s) - 1) if s[i].upper() != s[i + 1].upper())


if __name__ == '__main__':
    print(Solution().countKeyChanges("aAbBcC"))
    print(Solution().countKeyChanges("AaAaAaaA"))
