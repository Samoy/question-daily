from typing import List


# https://leetcode.cn/problems/permutations-ii/?envType=daily-question&envId=2025-02-06
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            dic = set()
            for i in range(x, len(nums)):
                if nums[i] not in dic:
                    dic.add(nums[i])
                    nums[x], nums[i] = nums[i], nums[x]
                    dfs(x + 1)
                    nums[x], nums[i] = nums[i], nums[x]
        dfs(0)
        return res


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
    print(Solution().permuteUnique([1, 2, 3]))
