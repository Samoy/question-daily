from collections import Counter
from typing import List


# https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/?envType=daily-question&envId=2024-10-12
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for num, c in cnt.items():
            if c == 2:
                ans ^= num
        return ans


if __name__ == '__main__':
    print(Solution().duplicateNumbersXOR([1, 2, 1, 3]))
    print(Solution().duplicateNumbersXOR([1, 2, 3]))
    print(Solution().duplicateNumbersXOR([1, 2, 2, 1]))
