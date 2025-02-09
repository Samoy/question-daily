from typing import List


# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?envType=daily-question&envId=2025-02-09
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[cnt - 2]:
                nums[cnt] = nums[i]
                cnt += 1
        return min(cnt, len(nums))


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
