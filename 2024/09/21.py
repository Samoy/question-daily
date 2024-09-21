from typing import List


# https://leetcode.cn/problems/node-with-highest-edge-score/?envType=daily-question&envId=2024-09-21
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = 0
        score = [0] * len(edges)
        for i, to in enumerate(edges):
            score[to] += i
            if score[to] > score[ans] or score[to] == score[ans] and to < ans:
                ans = to
        return ans


if __name__ == '__main__':
    print(Solution().edgeScore([1, 0, 0, 0, 0, 7, 7, 5]))
    print(Solution().edgeScore([2, 0, 0, 2]))
