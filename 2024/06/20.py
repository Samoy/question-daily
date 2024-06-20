from typing import List
from math import gcd


# https://leetcode.cn/problems/number-of-beautiful-pairs/?envType=daily-question&envId=2024-06-20
class Solution:
    """
    给你一个下标从 0 开始的整数数组 nums 。如果下标对 i、j 满足 0 ≤ i < j < nums.length ，
    如果 nums[i] 的 第一个数字 和 nums[j] 的 最后一个数字 互质 ，则认为 nums[i] 和 nums[j] 是一组 美丽下标对 。
    返回 nums 中 美丽下标对 的总数目。
    对于两个整数 x 和 y ，如果不存在大于 1 的整数可以整除它们，则认为 x 和 y 互质 。
    换而言之，如果 gcd(x, y) == 1 ，则认为 x 和 y 互质，其中 gcd(x, y) 是 x 和 y 的 最大公因数 。
    """

    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums) - 1):
            num_i = self.get_first_digit(nums[i])
            for j in range(i + 1, len(nums)):
                num_j = nums[j] % 10
                if gcd(num_i, num_j) == 1:
                    ans += 1
        return ans

    def get_first_digit(self, num):
        return num if num < 10 else self.get_first_digit(num // 10)


if __name__ == '__main__':
    print(Solution().countBeautifulPairs(nums=[2, 5, 1, 4]))
    print(Solution().countBeautifulPairs(nums=[11, 21, 12]))
