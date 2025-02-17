from collections import Counter
from typing import List


# https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/?envType=daily-question&envId=2025-02-17
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        total = sum(cnt.values())
        for k, v in cnt.items():
            if v > total / 4:
                return k
        return -1


if __name__ == '__main__':
    print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
    print(Solution().findSpecialInteger([1, 1]))
