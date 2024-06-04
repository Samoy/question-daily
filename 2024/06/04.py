from typing import List


# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/description/?envType=daily-question&envId=2024-06-04
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # 初始化节点数量和邻接表
        n = len(edges) + 1
        g = [[] for _ in range(n)]

        # 构造无向图
        for x, y, wt in edges:
            g[x].append([y, wt])  # 添加从x到y的边
            g[y].append([x, wt])  # 添加从y到x的边

        # 定义深度优先搜索（DFS）函数
        def dfs(x: int, fa: int, s: int) -> int:
            # 如果s模signalSpeed为0，说明从根节点到x的路径可以作为起点或终点
            cnt = 0 if s % signalSpeed else 1
            for y, wt in g[x]:
                # 避免回溯，检查y是否是父节点
                if y != fa:
                    # 递归计算以y为起点的满足条件的子树节点数，并累加到cnt
                    cnt += dfs(y, x, s + wt)
            return cnt

        # 初始化答案数组
        ans = [0] * n

        # 遍历每个节点并执行DFS，计算通过该节点可连接的服务器对数
        for i, gi in enumerate(g):
            s = 0
            for y, wt in gi:
                # 对每个邻居执行DFS，累加计数到答案数组中
                cnt = dfs(y, i, wt)
                ans[i] += cnt * s
                s += cnt
        # 返回答案数组
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1))
    print(s.countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], 3))
