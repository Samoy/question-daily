from typing import List


# https://leetcode.cn/problems/count-the-number-of-good-nodes/?envType=daily-question&envId=2024-11-14
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0

        def dfs(x: int, fa: int) -> int:
            size, sz0, ok = 1, 0, True
            for y in g[x]:
                if y == fa:
                    continue  # 不能递归到父节点
                sz = dfs(y, x)
                if sz0 == 0:
                    sz0 = sz  # 记录第一个儿子子树的大小
                elif sz != sz0:  # 存在大小不一样的儿子子树
                    ok = False  # 注意不能 break，其他子树 y 仍然要递归
                size += sz
            nonlocal ans
            ans += ok
            return size

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    print(Solution().countGoodNodes(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
    print(Solution().countGoodNodes(edges=[[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]))
    print(Solution().countGoodNodes(
        edges=[[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]]))
