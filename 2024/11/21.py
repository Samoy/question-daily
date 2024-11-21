from typing import List


# https://leetcode.cn/problems/snake-in-matrix/?envType=daily-question&envId=2024-11-21
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for cmd in commands:
            if cmd == "RIGHT":
                ans += 1
            elif cmd == "DOWN":
                ans += n
            elif cmd == "LEFT":
                ans -= 1
            else:
                ans -= n
        return ans


if __name__ == '__main__':
    print(Solution().finalPositionOfSnake(n=2, commands=["RIGHT", "DOWN"]))
    print(Solution().finalPositionOfSnake(n=3, commands=["DOWN", "RIGHT", "UP"]))
