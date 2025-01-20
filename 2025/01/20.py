from typing import List


# https://leetcode.cn/problems/find-closest-number-to-zero/?envType=daily-question&envId=2025-01-20
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return -min((abs(x), -x) for x in nums)[1]


if __name__ == "__main__":
    print(Solution().findClosestNumber([-4, -2, 1, 4, 8]))
    print(Solution().findClosestNumber([2, -1, 1]))
