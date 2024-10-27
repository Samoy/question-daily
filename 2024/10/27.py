from typing import List


# https://leetcode.cn/problems/redundant-connection/?envType=daily-question&envId=2024-10-27
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        # 并查集
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        # 合并
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        # 遍历
        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]

        return []


if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
