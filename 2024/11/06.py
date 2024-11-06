from typing import List


# https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/?envType=daily-question&envId=2024-11-06
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            cnt = cnt + 1 if i == 0 or x == nums[i - 1] + 1 else 1
            if cnt >= k:
                ans[i - k + 1] = x
        return ans


if __name__ == '__main__':
    print(Solution().resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3))
    print(Solution().resultsArray(nums=[2, 2, 2, 2, 2], k=4))
    print(Solution().resultsArray(nums=[3, 2, 3, 2, 3, 2], k=2))
