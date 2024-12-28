from collections import Counter
from typing import List


# https://leetcode.cn/problems/split-the-array/?envType=daily-question&envId=2024-12-27
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) <= 2


if __name__ == '__main__':
    print(Solution().isPossibleToSplit([1, 1, 2, 2, 3, 4]))
    print(Solution().isPossibleToSplit([1, 1, 1, 1]))
