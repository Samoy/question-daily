from typing import List


# https://leetcode.cn/problems/subsets-ii/?envType=daily-question&envId=2025-02-05
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            ans.append(path.copy())  # 也可以写 path[:]

            # 在 [i,n-1] 中选一个 nums[j]
            # 注意选 nums[j] 意味着 [i,j-1] 中的数都没有选
            for j in range(i, n):
                # 如果 j>i，说明 nums[j-1] 没有选
                # 同方法一，所有等于 nums[j-1] 的数都不选
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()  # 恢复现场

        dfs(0)
        return ans


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 2]))
    print(Solution().subsetsWithDup([0]))
