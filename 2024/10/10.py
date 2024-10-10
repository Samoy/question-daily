from typing import List


# https://leetcode.cn/problems/find-the-number-of-good-pairs-i/?envType=daily-question&envId=2024-10-10
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 % (num2 * k) == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
    print(Solution().numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
