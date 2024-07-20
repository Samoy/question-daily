from itertools import permutations
from typing import List


# https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/?envType=daily-question&envId=2024-07-20
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 初始化 'more_than_one_stones' 和 'no_stones' 列表
        # 'more_than_one_stones' 存储有多余石头的格子坐标
        # 'no_stones' 存储缺少石头的格子坐标
        more_than_one_stones = []
        no_stones = []

        # 遍历网格中的每个格子
        for i, row in enumerate(grid):
            for j, cnt in enumerate(row):
                # 如果格子中有超过一个石头，将多余的石头加入 'more_than_one_stones' 列表
                if cnt > 1:
                    more_than_one_stones.extend([(i, j)] * (cnt - 1))
                # 如果格子中没有石头，将其加入 'no_stones' 列表
                elif cnt == 0:
                    no_stones.append((i, j))

        # 初始化答案为无穷大，确保任何实际解都比它小
        ans = float('inf')

        # 对 'more_than_one_stones' 列表的所有可能排列进行遍历
        for from2 in permutations(more_than_one_stones):
            # 初始化总移动距离为0
            total = 0

            # 遍历 'from2' 和 'no_stones' 列表中的元素对，计算并累加移动距离
            for (x1, y1), (x2, y2) in zip(from2, no_stones):
                # 计算曼哈顿距离
                total += abs(x1 - x2) + abs(y1 - y2)

            # 更新最小移动次数
            ans = min(ans, total)

        # 返回最小移动次数
        return ans


if __name__ == '__main__':
    print(Solution().minimumMoves([[1, 1, 0], [1, 1, 1], [1, 2, 1]]))
    print(Solution().minimumMoves([[1, 3, 0], [1, 0, 0], [1, 0, 3]]))
