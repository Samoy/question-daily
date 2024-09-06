from typing import List


# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/?envType=daily-question&envId=2024-09-06
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        fs = {}
        mx = [0] * (k + 2)
        for x in nums:
            if x not in fs:
                fs[x] = [0] * (k + 1)
            f = fs[x]
            for j in range(k, -1, -1):
                f[j] = max(f[j], mx[j]) + 1
                mx[j + 1] = max(mx[j + 1], f[j])
        return mx[-1]


if __name__ == '__main__':
    print(Solution().maximumLength([1, 2, 1, 1, 3], 2))
    print(Solution().maximumLength([1, 2, 3, 4, 5, 1], 0))
