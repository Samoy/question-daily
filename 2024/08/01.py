from typing import List


# https://leetcode.cn/problems/uOAnQW/?envType=daily-question&envId=2024-08-01
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])  # 最大的 cnt 个数之和
        if s % 2 == 0:  # s 是偶数
            return s

        def replace_sum(x: int) -> int:
            for v in cards[cnt:]:
                if v % 2 != x % 2:  # 找到一个最大的奇偶性和 x 不同的数
                    return s - x + v  # 用 v 替换 s
            return 0

        x = cards[cnt - 1]
        ans = replace_sum(x)  # 替换 x
        for v in cards[cnt - 1:: -1]:
            if v % 2 != x % 2:  # 找到一个最小的奇偶性和 x 不同的数
                ans = max(ans, replace_sum(v))  # 替换
                break
        return ans


if __name__ == '__main__':
    print(Solution().maxmiumScore(cards=[1, 2, 8, 9], cnt=3))
    print(Solution().maxmiumScore(cards=[3, 3, 1], cnt=1))
    print(Solution().maxmiumScore(cards=[1, 3, 4, 5], cnt=4))
