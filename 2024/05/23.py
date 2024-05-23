from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/find-the-longest-equal-subarray/?envType=daily-question&envId=2024-05-23
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans = 0  # 初始化最长等值子数组的长度为0
        cnt = defaultdict(int)  # 创建一个defaultdict，用于记录每个元素在子数组中出现的次数，默认值为0

        # 双指针 i 和 j 分别表示滑动窗口的左右边界
        i = 0
        for j, x in enumerate(nums):  # 遍历数组nums的每个元素，下标用j表示
            cnt[x] += 1  # 更新元素x的计数，表示x在子数组中出现了一次

            # 当前窗口内不等值元素数量超过k时，移除左边界元素并更新窗口大小
            while j - i + 1 - cnt[nums[i]] > k:
                cnt[nums[i]] -= 1  # 减少左边界元素的计数
                i += 1  # 移动左边界

            # 更新最长等值子数组的长度，cnt[nums[j]]表示以x结尾的子数组的长度
            ans = max(ans, cnt[nums[j]])

        return ans  # 返回最长等值子数组的长度


if __name__ == '__main__':
    s = Solution()
    print(s.longestEqualSubarray([1, 3, 2, 3, 1, 3], 3))
    print(s.longestEqualSubarray([1, 1, 2, 2, 1, 1], 2))
