# https://leetcode.cn/problems/n-queens-ii/?envType=daily-question&envId=2024-12-02
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)


if __name__ == '__main__':
    print(Solution().totalNQueens(n=4))
    print(Solution().totalNQueens(n=1))
