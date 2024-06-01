# https://leetcode.cn/problems/distribute-candies-among-children-i/description/?envType=daily-question&envId=2024-06-01
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 初始化答案计数器
        ans = 0

        # 遍历第一个小朋友可能得到的糖果数（最多limit颗）
        for i in range(min(limit, n) + 1):
            # 计算在给第一个小朋友i颗糖果后剩余的糖果数
            remaining_candies = n - i

            # 如果剩余的糖果数超过了其他两位小朋友各拿limit颗的总和，则跳过本次循环
            # 因为我们要求没有任何一位小朋友得到超过limit颗糖果
            if remaining_candies > 2 * limit:
                continue

            # 计算在不违反限制的情况下，第二个小朋友可以得到的糖果范围
            # 使用min和max确保范围始终有效
            # 第二个小朋友最少可以得到0颗（都给第三位），最多limit颗
            second_possible = min(remaining_candies, limit)
            second_min = max(0, remaining_candies - limit)

            # 根据第二位小朋友的可能范围累加方案数
            # 这里利用了等差数列求和公式简化计算，实际上计算的是second_min到second_possible的整数个数
            ans += second_possible - second_min + 1

        # 返回总方案数
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(5, 2))
    print(s.distributeCandies(3, 3))
