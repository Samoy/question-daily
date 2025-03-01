from typing import List


# https://leetcode.cn/problems/palindrome-partitioning/?envType=daily-question&envId=2025-03-01
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:
                ans.append(path.copy())  # 复制 path
                return

            # 不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
            if i < n - 1:
                dfs(i + 1, start)

            # 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                dfs(i + 1, i + 1)  # 下一个子串从 i+1 开始
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    print(Solution().partition(s="aab"))
    print(Solution().partition(s="a"))
