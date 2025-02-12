from typing import List


# https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/?envType=daily-question&envId=2025-02-12
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mid):
            res = 0
            for num in nums:
                if num > mid:
                    res += (num - 1) // mid
            return res <= maxOperations

        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    print(Solution().minimumSize([9], 2))
    print(Solution().minimumSize([2, 4, 8, 2], 4))
    print(Solution().minimumSize([7, 17], 2))
