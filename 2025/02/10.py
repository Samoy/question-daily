from collections import deque
from typing import List

MOUSE_TURN = 0
CAT_TURN = 1

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2


# https://leetcode.cn/problems/cat-and-mouse/?envType=daily-question&envId=2025-02-10
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        degrees = [[[0, 0] for _ in range(n)] for _ in range(n)]
        results = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degrees[i][j][MOUSE_TURN] = len(graph[i])
                degrees[i][j][CAT_TURN] = len(graph[j])
        for y in graph[0]:
            for i in range(n):
                degrees[i][y][CAT_TURN] -= 1

        q = deque()
        for j in range(1, n):
            results[0][j][MOUSE_TURN] = MOUSE_WIN
            results[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n):
            results[i][i][MOUSE_TURN] = CAT_WIN
            results[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))

        while q:
            mouse, cat, turn = q.popleft()
            result = results[mouse][cat][turn]
            if turn == MOUSE_TURN:
                prev_states = [(mouse, prev, CAT_TURN) for prev in graph[cat]]
            else:
                prev_states = [(prev, cat, MOUSE_TURN) for prev in graph[mouse]]
            for prevMouse, prev_cat, prev_turn in prev_states:
                if prev_cat == 0:
                    continue
                if results[prevMouse][prev_cat][prev_turn] == DRAW:
                    can_win = result == MOUSE_WIN and prev_turn == MOUSE_TURN or result == CAT_WIN and prev_turn == CAT_TURN
                    if can_win:
                        results[prevMouse][prev_cat][prev_turn] = result
                        q.append((prevMouse, prev_cat, prev_turn))
                    else:
                        degrees[prevMouse][prev_cat][prev_turn] -= 1
                        if degrees[prevMouse][prev_cat][prev_turn] == 0:
                            results[prevMouse][prev_cat][prev_turn] = CAT_WIN if prev_turn == MOUSE_TURN else MOUSE_WIN
                            q.append((prevMouse, prev_cat, prev_turn))
        return results[1][2][MOUSE_TURN]


if __name__ == '__main__':
    print(Solution().catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
    print(Solution().catMouseGame([[1, 3], [0], [3], [0, 2]]))
