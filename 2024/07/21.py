from math import inf
from typing import List


# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/description/?envType=daily-question&envId=2024-07-21
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = f0 = f1 = -inf
        for x in arr:
            # 删除一个元素
            f1 = max(f1 + x, f0)
            # 不删除任何元素
            f0 = max(f0, 0) + x
            ans = max(ans, f0, f1)
        return ans


if __name__ == '__main__':
    print(Solution().maximumSum([1, -2, 0, 3]))
    print(Solution().maximumSum([1, -2, -2, 3]))
    print(Solution().maximumSum([-1, -1, -1, -1]))
