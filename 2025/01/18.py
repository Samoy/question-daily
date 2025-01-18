from typing import List


# https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/?envType=daily-question&envId=2025-01-18
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        def findORs(nums: List[int], k: int) -> List[set[int]]:
            dp = []
            prev = [set() for _ in range(k + 1)]
            prev[0].add(0)
            for i, num in enumerate(nums):
                for j in range(min(k - 1, i + 1), -1, -1):
                    for x in prev[j]:
                        prev[j + 1].add(x | num)
                dp.append(prev[k].copy())
            return dp

        A = findORs(nums, k)
        B = findORs(nums[::-1], k)

        mx = 0
        for i in range(k - 1, len(nums) - k):
            mx = max(mx, *(a ^ b for a in A[i] for b in B[-i - 2]))
        return mx


if __name__ == '__main__':
    print(Solution().maxValue(nums=[2, 6, 7], k=1))
    print(Solution().maxValue(nums=[4, 2, 5, 6, 7], k=2))
