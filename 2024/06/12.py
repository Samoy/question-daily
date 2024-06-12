# https://leetcode.cn/problems/account-balance-after-rounded-purchase/?envType=daily-question&envId=2024-06-12
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        mod, multi = purchaseAmount % 10, purchaseAmount // 10
        if mod >= 5:
            multi += 1
        return 100 - multi * 10


if __name__ == '__main__':
    s = Solution()
    print(s.accountBalanceAfterPurchase(9))
    print(s.accountBalanceAfterPurchase(15))
    print(s.accountBalanceAfterPurchase(11))
    print(s.accountBalanceAfterPurchase(5))
    print(s.accountBalanceAfterPurchase(1))
