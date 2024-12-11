from typing import List


# https://leetcode.cn/problems/semi-ordered-permutation/?envType=daily-question&envId=2024-12-11
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1 and nums[-1] == n:
            return 0
        one_index, n_index = nums.index(1), nums.index(n)
        return one_index + n - n_index - 1 if one_index < n_index else one_index + n - n_index - 2


if __name__ == '__main__':
    print(Solution().semiOrderedPermutation([2, 1, 4, 3]))
    print(Solution().semiOrderedPermutation([2, 4, 1, 3]))
    print(Solution().semiOrderedPermutation([1, 3, 4, 2, 5]))
