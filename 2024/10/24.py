from typing import List


# https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/?envType=daily-question&envId=2024-10-24
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        max_i = win = 0
        for i in range(1, len(skills)):
            if skills[i] > skills[max_i]:  # 打擂台，发现新的最大值
                max_i = i
                win = 0
            win += 1  # 获胜回合 +1
            if win == k:  # 连续赢下 k 场比赛
                break
        # 如果 k 很大，那么 max_i 就是 skills 最大值的下标，毕竟最大值会一直赢下去
        return max_i


if __name__ == '__main__':
    print(Solution().findWinningPlayer(skills=[4, 2, 6, 3, 9], k=2))
    print(Solution().findWinningPlayer(skills=[2, 5, 4], k=3))
