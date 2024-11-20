from typing import List


# https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/?envType=daily-question&envId=2024-11-20
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        fa = list(range(n - 1))

        # 非递归并查集
        def find(x: int) -> int:
            rt = x
            while fa[rt] != rt:
                rt = fa[rt]
            while fa[x] != rt:
                fa[x], x = rt, fa[x]
            return rt

        ans = []
        cnt = n - 1  # 并查集连通块个数
        for left, right in queries:
            fr = find(right - 1)
            i = find(left)
            while i < right - 1:
                cnt -= 1
                fa[i] = fr
                i = find(i + 1)
            ans.append(cnt)
        return ans


if __name__ == '__main__':
    print(Solution().shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
    print(Solution().shortestDistanceAfterQueries(n=4, queries=[[0, 3], [0, 2]]))
