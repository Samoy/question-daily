from typing import List


# https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/?envType=daily-question&envId=2025-01-12
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        m = max(candidates).bit_length()
        return max(sum(x >> i & 1 for x in candidates) for i in range(m))


if __name__ == '__main__':
    print(Solution().largestCombination([16, 17, 71, 62, 12, 24, 14]))
    print(Solution().largestCombination([8, 8]))
