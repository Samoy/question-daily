from typing import List


# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/?envType=daily-question&envId=2024-10-19
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if x == k % 2:  # 必须操作
                k += 1
        return k


if __name__ == '__main__':
    print(Solution().minOperations([0, 1, 1, 0, 1]))
    print(Solution().minOperations([1, 0, 0, 0]))
