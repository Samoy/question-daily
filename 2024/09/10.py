from typing import List


# https://leetcode.cn/problems/count-increasing-quadruplets/?envType=daily-question&envId=2024-09-10
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt4 = 0
        cnt3 = [0] * len(nums)
        for l in range(2, len(nums)):
            cnt2 = 0
            for j in range(l):
                if nums[j] < nums[l]:  # 3 < 4
                    cnt4 += cnt3[j]
                    # 把 j 当作 i，把 l 当作 k，现在 nums[i] < nums[k]，即 1 < 2
                    cnt2 += 1
                else:  # 把 l 当作 k，现在 nums[j] > nums[k]，即 3 > 2
                    cnt3[j] += cnt2
        return cnt4


if __name__ == '__main__':
    print(Solution().countQuadruplets([1, 3, 2, 4, 5]))
    print(Solution().countQuadruplets([1, 2, 3, 4]))
