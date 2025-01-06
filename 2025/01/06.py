from typing import List


# https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors/?envType=daily-question&envId=2025-01-06
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = special[0] - bottom
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)
        return max(ans, top - special[-1])


if __name__ == '__main__':
    print(Solution().maxConsecutive(2, 9, [4, 6]))
    print(Solution().maxConsecutive(6, 8, [7, 6, 8]))
