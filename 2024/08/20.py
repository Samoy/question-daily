from functools import cache


class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(i, op, jump):
            if op == 1 and i > 0:  # 处理第一种操作
                i -= 1  # - 退 1 台阶
                return dfs(i, 2, jump) + (i == k)  # - 接下来尝试第二种操作
            if op == 2 and i <= k:  # 处理第二种操作
                i += 1 << jump  # - 进 1 << jump 台阶
                return (
                        dfs(i, 1, jump + 1) + dfs(i, 2, jump + 1) + (i == k)
                )  # - 接下来尝试第一、二种操作
            return 0

        return dfs(1, 1, 0) + dfs(1, 2, 0) + (k == 1)


if __name__ == '__main__':
    print(Solution().waysToReachStair(0))
    print(Solution().waysToReachStair(1))
