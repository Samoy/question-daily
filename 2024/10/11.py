from collections import Counter
from typing import List


# https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/?envType=daily-question&envId=2024-10-11
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 统计 nums1 中每个元素除以 k 后的结果，并且只保留能够整除的结果
        cnt = Counter(num1 // k for num1 in nums1 if num1 % k == 0)

        # 如果没有符合条件的元素，则返回 0
        if not cnt:
            return 0

        # 初始化答案变量
        ans = 0

        # 找到最大的除以 k 后的结果
        u = max(cnt)

        # 统计 nums2 中每个元素出现的次数
        nums2_cnt = Counter(nums2)

        # 遍历 nums2 中的每个元素及其出现次数
        for x, c in nums2_cnt.items():
            # 计算 nums1 中能够被 nums2[j] * k 整除的元素个数
            s = sum(cnt[i] for i in range(x, u + 1, x))

            # 更新答案
            ans += s * c

        # 返回优质数对的总数
        return ans


if __name__ == '__main__':
    print(Solution().numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
    print(Solution().numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
