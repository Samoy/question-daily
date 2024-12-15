from itertools import accumulate
from typing import List


# https://leetcode.cn/problems/reduce-array-size-to-the-half/?envType=daily-question&envId=2024-12-15
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = [0] * (max(arr) + 1)
        for x in arr:
            cnt[x] += 1
        cnt.sort(reverse=True)

        m = len(arr) // 2
        for i, s in enumerate(accumulate(cnt)):
            if s >= m:
                return i + 1


if __name__ == '__main__':
    print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
    print(Solution().minSetSize([7, 7, 7, 7, 7, 7]))
