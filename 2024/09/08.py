from typing import List


# https://leetcode.cn/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-09-08
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for p in range(n - 1, -1, -1):
            x = nums[i] * nums[i]
            y = nums[j] * nums[j]
            if x > y:  # 更大的数放右边
                ans[p] = x
                i += 1
            else:
                ans[p] = y
                j -= 1
        return ans


if __name__ == '__main__':
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
