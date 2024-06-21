from typing import List


# https://leetcode.cn/problems/6CE719/description/?envType=daily-question&envId=2024-06-21
class Solution:
    """
    力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 i ~ (i+1) 天的气温变化趋势，
    将根据以下规则判断：
        若第 i+1 天的气温 高于 第 i 天，为 上升 趋势
        若第 i+1 天的气温 等于 第 i 天，为 平稳 趋势
        若第 i+1 天的气温 低于 第 i 天，为 下降 趋势
    已知 temperatureA[i] 和 temperatureB[i] 分别表示第 i 天两地区的气温。 组委会希望找到一段天数尽可能多，
    且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势相同的最大连续天数。
    """

    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        trend, ans, length = 0, 0, len(temperatureA) - 1
        for i, x in enumerate(temperatureA):
            if i < length:
                temp_diff_a = temperatureA[i + 1] - x
                temp_diff_b = temperatureB[i + 1] - temperatureB[i]
                if ((temp_diff_a > 0 and temp_diff_b > 0)
                        or (temp_diff_a == 0 and temp_diff_b == 0)
                        or (temp_diff_a < 0 and temp_diff_b < 0)):
                    trend += 1
                    ans = max(ans, trend)
                else:
                    trend = 0
        return ans


if __name__ == '__main__':
    print(Solution().temperatureTrend([21, 18, 18, 18, 31], [34, 32, 16, 16, 17]))
    print(Solution().temperatureTrend([5, 10, 16, -6, 15, 11, 3], [16, 22, 23, 23, 25, 3, -16]))
