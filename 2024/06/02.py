from typing import List


# https://leetcode.cn/problems/distribute-candies/description/?envType=daily-question&envId=2024-06-02
class Solution:
    """
    解题思路如下：
    1. 计算不同种类的糖：首先利用 set(candyType) 去除重复项，得到所有不同种类的糖的数量。
       这是因为集合（set）数据结构中不会保存重复元素，所以转换后集合的长度就是糖的种类数。
    2. 确定最多能吃糖的种类数：由于题目要求 Alice 只能吃 n/2 枚糖，那么理论上她能尝试的糖的种类数最多也是 n/2 种
       （假设每种糖恰好吃一枚且种类足够多）。因此，我们用 len(candyType) // 2 计算出这个理论上的最大种类数。
    3. 取最小值：最后，通过 min 函数比较不同种类的糖的数量和理论上的最大可尝试种类数，取两者的较小值作为答案。
       这是因为实际的不同种类糖的数量可能小于 n/2（比如很多糖是重复的类型），或者即使种类数量多于 n/2，Alice 也只能吃掉 n/2 枚，
       所以取最小值确保了结果既满足医生的建议，又能最大化尝试的种类数。
    """

    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1, 1, 2, 2, 3, 3]))
    print(s.distributeCandies([1, 1, 2, 3]))
    print(s.distributeCandies([6, 6, 6, 6]))
