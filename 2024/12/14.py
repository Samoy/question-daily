from heapq import heapify, heapreplace
from typing import List


# https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/?envType=daily-question&envId=2024-12-14
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:  # 数组不变
            return nums

        MOD = 1_000_000_007
        n = len(nums)
        mx = max(nums)
        h = [(x, i) for i, x in enumerate(nums)]
        heapify(h)

        # 模拟，直到堆顶是 mx
        while k and h[0][0] < mx:
            x, i = h[0]
            heapreplace(h, (x * multiplier, i))
            k -= 1

        # 剩余的操作可以直接用公式计算
        h.sort()
        for i, (x, j) in enumerate(h):
            nums[j] = x * pow(multiplier, k // n + (i < k % n), MOD) % MOD
        return nums


if __name__ == '__main__':
    print(Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
    print(Solution().getFinalState(nums=[100000, 2000], k=2, multiplier=1000000))
