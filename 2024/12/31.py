from typing import List


# https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/?envType=daily-question&envId=2024-12-31
class Solution:
    def minimumCost(
            self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        ans = i = j = 0
        for _ in range(m + n - 2):
            if j == n - 1 or i < m - 1 and horizontalCut[i] < verticalCut[j]:
                ans += horizontalCut[i] * (n - j)  # 上下连边
                i += 1
            else:
                ans += verticalCut[j] * (m - i)  # 左右连边
                j += 1
        return ans


if __name__ == '__main__':
    print(Solution().minimumCost(m=3, n=2, horizontalCut=[1, 3], verticalCut=[5]))
    print(Solution().minimumCost(m=2, n=2, horizontalCut=[7], verticalCut=[4]))
