from typing import List
import heapq


# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/?envType=daily-question&envId=2024-07-18
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        n = len(disappear)  # 获取节点总数
        graph = [[] for _ in range(n)]  # 初始化邻接列表表示的图

        # 构建图的邻接表
        for u, v, length in edges:
            graph[u].append((v, length))  # 添加边 (u -> v, length)
            graph[v].append((u, length))  # 因为是无向图，所以也添加 (v -> u, length)

        # 使用最小堆存储 (到达时间, 节点)
        queue = [(0, 0)]  # 初始状态是从节点0出发，到达时间为0
        visited = set()  # 已访问过的节点集合
        answer = [-1] * n  # 初始化结果数组，所有节点默认不可达

        # Dijkstra算法变种的主循环
        while queue:
            time, node = heapq.heappop(queue)  # 弹出当前可达的最短时间的节点
            # 只有当节点未被访问过且当前到达时间小于等于节点消失时间时，才进行处理
            if node not in visited and time <= disappear[node]:
                visited.add(node)  # 标记节点为已访问
                answer[node] = time  # 更新答案数组中的到达时间

                # 遍历当前节点的所有邻居
                for neighbor, length in graph[node]:
                    # 如果邻居节点未被访问过且新到达时间小于邻居的消失时间，则加入队列
                    if neighbor not in visited and time + length < disappear[neighbor]:
                        heapq.heappush(queue, (time + length, neighbor))

        return answer


if __name__ == '__main__':
    print(Solution().minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 1, 5]))
    print(Solution().minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 3, 5]))
    print(Solution().minimumTime(2, [[0, 1, 1]], [1, 1]))
