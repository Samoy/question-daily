from typing import List

DENOMINATIONS = [20, 50, 100, 200, 500]
KINDS = len(DENOMINATIONS)


# https://leetcode.cn/problems/design-an-atm-machine/?envType=daily-question&envId=2025-01-05
class ATM:
    def __init__(self):
        self.banknotes = [0] * KINDS

    def deposit(self, banknotesCount: List[int]) -> None:
        # 存钱
        for i, count in enumerate(banknotesCount):
            self.banknotes[i] += count

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * KINDS

        # 计算每种钞票所需数量
        for i in range(KINDS - 1, -1, -1):
            ans[i] = min(amount // DENOMINATIONS[i], self.banknotes[i])
            amount -= ans[i] * DENOMINATIONS[i]

        # 无法取恰好 amount
        if amount > 0:
            return [-1]

        # 取钱
        for i, count in enumerate(ans):
            self.banknotes[i] -= count

        return ans


if __name__ == '__main__':
    atm = ATM()
    atm.deposit([0, 0, 1, 2, 1])
    print(atm.withdraw(600))
    atm.deposit([0, 1, 0, 1, 1])
    print(atm.withdraw(600))
    print(atm.withdraw(550))
