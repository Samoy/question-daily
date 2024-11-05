# https://leetcode.cn/problems/find-the-winning-player-in-coin-game/?envType=daily-question&envId=2024-11-05
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) % 2 != 0 else "Bob"


if __name__ == "__main__":
    print(Solution().losingPlayer(2, 7))
    print(Solution().losingPlayer(4, 11))
