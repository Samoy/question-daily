from itertools import accumulate, pairwise
from typing import List


# https://leetcode.cn/problems/special-array-ii/?envType=daily-question&envId=2024-08-14
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), initial=0))
        return [s[from_] == s[to] for from_, to in queries]


if __name__ == '__main__':
    print(Solution().isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
    print(Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
