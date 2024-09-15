from itertools import accumulate
from typing import List


# https://leetcode.cn/problems/points-that-intersect-with-cars/?envType=daily-question&envId=2024-09-15
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for s, e in nums:
            diff[s] += 1
            diff[e + 1] -= 1
        return sum(s > 0 for s in accumulate(diff))


if __name__ == '__main__':
    print(Solution().numberOfPoints([[3, 6], [1, 5], [4, 7]]))
    print(Solution().numberOfPoints([[1, 3], [5, 8]]))
