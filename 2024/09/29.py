from typing import List


# https://leetcode.cn/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-09-29
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tk = tickets[k]
        return sum(min(t, tk - (i > k)) for i, t in enumerate(tickets))


if __name__ == '__main__':
    print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
    print(Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
