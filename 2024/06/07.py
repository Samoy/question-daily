from typing import List


# https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i/?envType=daily-question&envId=2024-06-07
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        cnt, s, length, i = 1, nums[0] + nums[1], len(nums), 2
        while i < length:
            if i == length - 1 or nums[i] + nums[i + 1] != s:
                break
            else:
                cnt += 1
                s = nums[i] + nums[i + 1]
            i += 2
        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxOperations([3, 2, 1, 4, 5]))
    print(solution.maxOperations([3, 2, 6, 1, 4]))
    print(solution.maxOperations([5, 6]))
    print(solution.maxOperations([1, 1, 1, 1, 1, 1, 2, 1, 1, 2]))
