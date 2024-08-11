from typing import List

# https://leetcode.cn/problems/uncrossed-lines/?envType=daily-question&envId=2024-08-11
class Solution:
    def maxUncrossedLines(self, s: List[int], t: List[int]) -> int:
        f = [0] * (len(t) + 1)
        for x in s:
            pre = 0  # f[0]
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j])
                pre = tmp
        return f[-1]