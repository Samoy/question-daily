from typing import List

# https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/?envType=daily-question&envId=2025-01-22
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        return sum(piles[n // 3 :: 2])

if __name__ == '__main__':
    s = Solution()
    assert s.maxCoins([2,4,1,2,7,8]) == 9
    assert s.maxCoins([2,4,5]) == 4