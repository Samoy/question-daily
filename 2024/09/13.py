from collections import deque
from typing import List


# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/?envType=daily-question&envId=2024-09-13
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = s = left = 0
        q = deque()
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            # 1. 入
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += c  # 维护 sum(runningCosts)

            # 2. 出
            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]  # 维护 sum(runningCosts)
                left += 1

            # 3. 更新答案
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    print(Solution().maximumRobots(chargeTimes=[3, 6, 1, 3, 4], runningCosts=[2, 1, 3, 4, 5], budget=25))
    print(Solution().maximumRobots(chargeTimes=[11, 12, 19], runningCosts=[10, 8, 7], budget=19))
