from cmath import inf
from typing import List


# https://leetcode.cn/problems/maximum-distance-in-arrays/?envType=daily-question&envId=2025-02-19
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mn, mx = inf, -inf
        for a in arrays:
            ans = max(ans, a[-1] - mn, mx - a[0])
            mn = min(mn, a[0])
            mx = max(mx, a[-1])
        return ans


if __name__ == '__main__':
    print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print(Solution().maxDistance([[1], [1]]))
