from typing import List


# https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/description/?envType=daily-question&envId=2024-05-16
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # 耗时最长工作所需周数
        max_milestone = max(milestones)
        # 其余工作所需周数
        other_milestones = sum(milestones) - max_milestone
        if max_milestone > other_milestones + 1:
            # 此时无法完成所耗时最长的工作
            return other_milestones * 2 + 1
        else:
            # 此时可以完成所有工作
            return max_milestone + other_milestones


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfWeeks(milestones=[1, 2, 3]))  # 7
    print(s.numberOfWeeks(milestones=[5, 2, 1]))  # 6
