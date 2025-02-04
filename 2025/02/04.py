from typing import List


# https://leetcode.cn/problems/sort-array-by-parity-ii/?envType=daily-question&envId=2025-02-04
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(nums):
            if nums[even] % 2 == 0:  # 寻找偶数下标中最左边的奇数
                even += 2
            elif nums[odd] % 2 == 1:  # 寻找奇数下标中最左边的偶数
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        return nums


if __name__ == '__main__':
    print(Solution().sortArrayByParityII([4, 2, 5, 7]))
    print(Solution().sortArrayByParityII([2, 3]))
