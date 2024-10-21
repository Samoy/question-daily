from typing import List


# https://leetcode.cn/problems/smallest-range-ii/?envType=daily-question&envId=2024-10-21
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            # a和b分别为当前元素和下一个元素
            a, b = nums[i], nums[i + 1]
            # 更新最小可能差，考虑增加或减少k后的最大值和最小值
            ans = min(ans, max(nums[-1] - k, a + k) - min(nums[0] + k, b - k))
        return ans


if __name__ == '__main__':
    print(Solution().smallestRangeII(nums=[1], k=0))
    print(Solution().smallestRangeII(nums=[0, 10], k=2))
    print(Solution().smallestRangeII(nums=[1, 3, 6], k=3))
