from typing import List


# https://leetcode.cn/problems/find-the-winner-of-an-array-game/description/?envType=daily-question&envId=2024-05-19
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 检查特殊情况：如果k大于数组长度，那么最大值必定是赢家
        if k > len(arr):
            return max(arr)

        # 否则，进行模拟游戏
        else:
            # 初始化连胜计数（streak）、当前赢家（winner）和上一轮的失败者（defeated）
            streak, winner, defeated = 0, 0, 0

            # 当连胜计数小于k时，继续游戏
            while streak < k:
                # 比较前两个元素，找到最大值和最小值
                tmp = max(arr[0], arr[1])
                defeated = min(arr[0], arr[1])

                # 如果当前赢家大于或等于新最大值，连胜计数加一
                if winner >= tmp:
                    streak += 1
                else:
                    # 否则，更新连胜计数为1，设置新最大值为赢家
                    streak = 1
                    winner = tmp

                # 移除失败者，将其添加到数组末尾（不影响后续比较，因为已经确定是失败者）
                arr.remove(defeated)
                arr.append(defeated)

            # 返回游戏的赢家
            return winner

    def getWinner2(self, arr: List[int], k: int) -> int:
        # 初始化赢家为数组前两个元素中的较大值
        winner = max(arr[0], arr[1])
        # 如果k为1，直接返回当前赢家，因为它只需赢一次
        if k == 1:
            return winner
        # 初始化连胜计数
        streak = 1
        # 记录遍历过程中的最大值，用于处理k大于数组长度的情况
        max_num = winner
        # 遍历数组剩余部分
        length = len(arr)
        for i in range(2, length):
            # 当前待比较的元素
            curr = arr[i]
            # 如果当前赢家仍大于新元素，连胜计数加一
            if winner > curr:
                streak += 1
                # 如果达到k连胜，直接返回赢家
                if streak == k:
                    return winner
            else:
                # 否则，更新赢家为当前元素，并重置连胜计数
                winner = curr
                streak = 1
            # 更新过程中遇到的最大值
            max_num = max(max_num, curr)
        # 如果遍历完数组仍没有达到k连胜，则返回过程中遇到的最大值（因为题目保证有赢家）
        return max_num


if __name__ == '__main__':
    s = Solution()
    print(s.getWinner([2, 1, 3, 5, 4, 6, 7], 2))
    print(s.getWinner([3, 2, 1], 10))
    print(s.getWinner([1, 9, 8, 2, 3, 7, 6, 4, 5], 7))
    print(s.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
    print(s.getWinner([1, 25, 35, 42, 68, 70], 1))
    print(s.getWinner2([2, 1, 3, 5, 4, 6, 7], 2))
    print(s.getWinner2([3, 2, 1], 10))
    print(s.getWinner2([1, 9, 8, 2, 3, 7, 6, 4, 5], 7))
    print(s.getWinner2([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
    print(s.getWinner2([1, 25, 35, 42, 68, 70], 1))
