from functools import lru_cache
from typing import List


# https://leetcode.cn/problems/shopping-offers/?envType=daily-question&envId=2024-11-03
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # 过滤不需要计算的大礼包，只保留需要计算的大礼包
        filter_special = []
        for sp in special:
            if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                filter_special.append(sp)

        # 记忆化搜索计算满足购物清单所需花费的最低价格
        @lru_cache(None)
        def dfs(cur_needs):
            # 不购买任何大礼包，原价购买购物清单中的所有物品
            min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                nxt_needs = []
                for i in range(n):
                    if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
                        break
                    nxt_needs.append(cur_needs[i] - cur_special[i])
                if len(nxt_needs) == n:  # 大礼包可以购买
                    min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
            return min_price

        return dfs(tuple(needs))


if __name__ == '__main__':
    print(Solution().shoppingOffers(price=[2, 5], special=[[3, 0, 5], [1, 2, 10]], needs=[3, 2]))
    print(Solution().shoppingOffers(price=[2, 3, 4], special=[[1, 1, 0, 4], [2, 2, 1, 9]], needs=[1, 2, 1]))
