from bisect import bisect_left
from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/?envType=daily-question&envId=2024-08-27
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def check(upper: int) -> bool:
            cnt = l = 0
            freq = defaultdict(int)
            for r, in_ in enumerate(nums):
                freq[in_] += 1  # 移入右端点
                while len(freq) > upper:  # 窗口内元素过多
                    out = nums[l]
                    freq[out] -= 1  # 移出左端点
                    if freq[out] == 0:
                        del freq[out]
                    l += 1
                cnt += r - l + 1  # 右端点固定为 r 时，有 r-l+1 个合法左端点
                if cnt >= k:
                    return True
            return False

        return bisect_left(range(len(set(nums))), True, 1, key=check)


if __name__ == '__main__':
    print(Solution().medianOfUniquenessArray([1, 2, 3]))
    print(Solution().medianOfUniquenessArray([3, 4, 3, 4, 5]))
    print(Solution().medianOfUniquenessArray([4, 3, 5, 4]))
