from typing import List


# https://leetcode.cn/problems/combination-sum-ii/?envType=daily-question&envId=2025-01-26
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            # 所选元素之和恰好等于 target
            if left == 0:
                ans.append(path.copy())  # 也可以写 path[:]
                return

            # 没有可以选的数字
            if i == n:
                return

            # 所选元素之和无法恰好等于 target
            x = candidates[i]
            if left < x:
                return

            # 选 x
            path.append(x)
            dfs(i + 1, left - x)
            path.pop()  # 恢复现场

            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中，这就重复了
            i += 1
            while i < n and candidates[i] == x:
                i += 1
            dfs(i, left)

        dfs(0, target)
        return ans


if __name__ == "__main__":
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
