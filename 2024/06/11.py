from typing import List


# https://leetcode.cn/problems/battleships-in-a-board/description/?envType=daily-question&envId=2024-06-11
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 遍历矩阵的每一个元素
        return sum(
            # 当前元素为 'X'，表示可能是一个战舰的开始
            ch == "X"
            # 并且它不是另一个战舰的一部分（即上方或左方没有紧挨着另一个 'X'）
            and not (
                    # 检查上方是否有战舰（i > 0 确保不越界）
                    i > 0 and board[i - 1][j] == "X"
                    or
                    # 检查左方是否有战舰（j > 0 确保不越界）
                    j > 0 and board[i][j - 1] == "X"
            )
            # 使用enumerate遍历行和列，i为行索引，row为当前行，j为列索引，ch为当前单元格的字符
            for i, row in enumerate(board)
            for j, ch in enumerate(row)
        )


if __name__ == '__main__':
    s = Solution()
    print(s.countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
    print(s.countBattleships([["."]]))
