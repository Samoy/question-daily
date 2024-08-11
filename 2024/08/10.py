from typing import List

# https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/description/?envType=daily-question&envId=2024-08-10
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        zd = [0] * (n * 4)

        def build(l, r, rt, heights):
            if l == r:
                zd[rt] = heights[l - 1]
                return

            mid = (l + r) // 2
            build(l, mid, rt << 1, heights)
            build(mid + 1, r, rt << 1 | 1, heights)
            zd[rt] = max(zd[rt << 1], zd[rt << 1 | 1])

        def query(pos, val, l, r, rt):
            if val >= zd[rt]:
                return 0
            if l == r:
                return l
            mid = (l + r) // 2
            if pos <= mid:
                res = query(pos, val, l, mid, rt << 1)
                if res != 0:
                    return res
            return query(pos, val, mid + 1, r, rt << 1 | 1)

        build(1, n, 1, heights)
        m = len(queries)
        ans = [0] * m
        for i in range(m):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
                continue
            ans[i] = query(b + 1, heights[a], 1, n, 1) - 1
        return ans

if __name__ == '__main__':
    print(Solution().leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))
    print(Solution().leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))
    