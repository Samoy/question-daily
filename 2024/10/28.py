from typing import List


class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))

    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)

    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]


# https://leetcode.cn/problems/redundant-connection-ii/?envType=daily-question&envId=2024-10-28
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        parent = list(range(n + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflict_edge = edges[conflict]
            if cycle >= 0:
                return [parent[conflict_edge[1]], conflict_edge[1]]
            else:
                return [conflict_edge[0], conflict_edge[1]]
