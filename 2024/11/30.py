from typing import List


# https://leetcode.cn/problems/find-if-digit-game-can-be-won/?envType=daily-question&envId=2024-11-30
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(x if x < 10 else -x for x in nums) != 0


if __name__ == '__main__':
    print(Solution().canAliceWin([1, 2, 3, 4, 10]))
    print(Solution().canAliceWin([1, 2, 3, 4, 5, 14]))
    print(Solution().canAliceWin([5, 5, 5, 25]))
