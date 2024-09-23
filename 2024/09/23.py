from math import inf
from typing import List


# https://leetcode.cn/problems/best-sightseeing-pair/?envType=daily-question&envId=2024-09-23
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 初始化答案为负无穷，确保任何有效的值都会比它大
        ans = -inf
        # 初始化最大值为第一个观光点的值加上其索引（0）
        max_value = values[0]
        # 遍历从第二个观光点开始的所有观光点
        for i in range(1, len(values)):
            # 更新答案为当前最大值与当前观光点组成的一对观光点得分的最大值
            ans = max(ans, max_value + values[i] - i)
            # 更新最大值为当前观光点的值加上其索引与之前最大值的最大值
            max_value = max(max_value, values[i] + i)
        # 返回最大得分
        return ans


if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(Solution().maxScoreSightseeingPair([1, 2]))
