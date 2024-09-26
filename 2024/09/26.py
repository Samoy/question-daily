from typing import List
from itertools import chain


# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/?envType=daily-question&envId=2024-09-26
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(chain(*[[int(i) for i in list(str(n))] for n in nums])))


if __name__ == '__main__':
    print(Solution().differenceOfSum([1, 15, 6, 3]))
    print(Solution().differenceOfSum([1, 2, 3, 4]))
