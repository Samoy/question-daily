from typing import List


# https://leetcode.cn/problems/minimum-money-required-before-transactions/?envType=daily-question&envId=2025-01-25
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = mx = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            mx = max(mx, min(cost, cashback))
        return total_lose + mx


if __name__ == '__main__':
    print(Solution().minimumMoney([[2, 1], [5, 0], [4, 2]]))
    print(Solution().minimumMoney([[3, 0], [0, 3]]))
