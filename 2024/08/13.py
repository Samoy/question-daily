from typing import List


# https://leetcode.cn/problems/special-array-i/description/?envType=daily-question&envId=2024-08-13
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def same_parity(nums1: int, nums2: int):
            return (nums1 & 1) ^ (nums2 & 1) == 0

        n = len(nums)
        if n == 1:
            return True
        for i in range(1, n, 2):
            before = nums[i - 1]
            if same_parity(before, nums[i]):
                return False
            if i < n - 1:
                after = nums[i + 1]
                if same_parity(nums[i], after):
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isArraySpecial([1]))
    print(Solution().isArraySpecial([2, 1, 4]))
    print(Solution().isArraySpecial([4, 3, 1, 6]))
