# https://leetcode.cn/problems/find-the-maximum-achievable-number/?envType=daily-question&envId=2024-05-21
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


if __name__ == '__main__':
    s = Solution()
    print(s.theMaximumAchievableX(4, 1))
    print(s.theMaximumAchievableX(3, 2))
