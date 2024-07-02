from typing import List


# https://leetcode.cn/problems/maximum-prime-difference/description/?envType=daily-question&envId=2024-07-02
class Solution:
    """
    给你一个整数数组 nums。
    返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。
    """

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num in [2, 3, 5, 7]:
                return True
            return (num % 2 != 0
                    and num % 3 != 0
                    and num % 5 != 0
                    and num % 7 != 0
                    and num % 10 in [1, 3, 7, 9])

        i, j = 0, len(nums) - 1
        while not is_prime(nums[i]):
            i += 1
        while not is_prime(nums[j]):
            j -= 1
        return j - i


if __name__ == '__main__':
    print(Solution().maximumPrimeDifference([4, 2, 9, 5, 3]))
    print(Solution().maximumPrimeDifference([4, 8, 2, 8]))
