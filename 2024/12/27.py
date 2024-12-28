from typing import List


# https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/?envType=daily-question&envId=2024-12-27
class Solution:
    def occurrencesOfElement(
            self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        pos = [i for i, num in enumerate(nums) if num == x]
        return [-1 if q > len(pos) else pos[q - 1] for q in queries]


if __name__ == '__main__':
    print(Solution().occurrencesOfElement(nums=[1, 3, 1, 7], queries=[1, 3, 2, 4], x=1))
    print(Solution().occurrencesOfElement(nums=[1, 2, 3], queries=[10], x=5))
