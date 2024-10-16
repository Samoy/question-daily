from typing import List


# https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/?envType=daily-question&envId=2024-10-16
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while len(nums):
            min_num = min(nums)
            max_num = max(nums)
            nums.remove(min_num)
            nums.remove(max_num)
            averages.append((min_num + max_num) / 2)
        return min(averages)


if __name__ == '__main__':
    print(Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
    print(Solution().minimumAverage([1, 9, 8, 3, 10, 5]))
    print(Solution().minimumAverage([1, 2, 3, 7, 8, 9]))
