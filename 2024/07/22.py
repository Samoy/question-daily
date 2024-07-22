from typing import List


# https://leetcode.cn/problems/detonate-the-maximum-bombs/?envType=daily-question&envId=2024-07-22
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 获取炸弹总数
        n = len(bombs)
        # 初始化图结构，用于存储炸弹间的引爆关系
        g = [[] for _ in range(n)]
        # 遍历每一对炸弹，判断是否可以互相引爆
        for i in range(n):
            for j in range(i + 1, n):
                # 解包炸弹坐标和半径
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                # 判断炸弹j是否在炸弹i的引爆范围内
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    g[i].append(j)
                # 判断炸弹i是否在炸弹j的引爆范围内
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r2 ** 2:
                    g[j].append(i)
        # 初始化最大引爆数量为0
        ans = 0
        # 遍历每个炸弹作为起始点
        for i in range(n):
            # 初始化访问标记数组
            vis = [False] * n
            # 使用队列进行广度优先搜索
            q = [i]
            # 当队列不为空时，继续搜索
            while q:
                # 弹出队列头部的炸弹索引
                t = q.pop(0)
                # 标记当前炸弹已访问
                vis[t] = True
                # 遍历当前炸弹可以引爆的所有炸弹
                for v in g[t]:
                    # 如果未访问过，则加入队列，准备下一轮搜索
                    if not vis[v]:
                        q.append(v)
            # 更新最大引爆数量
            ans = max(ans, sum(vis))
        # 返回最大引爆数量
        return ans


if __name__ == '__main__':
    print(Solution().maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]]))
    print(Solution().maximumDetonation(bombs=[[1, 1, 5], [10, 10, 5]]))
    print(Solution().maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
