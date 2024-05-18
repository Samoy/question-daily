from typing import List


# https://leetcode.cn/problems/find-the-maximum-divisibility-score/description/?envType=daily-question&envId=2024-05-18
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # 初始化最大分数为0，以及当前得分最高的除数为divisors的第一个元素
        max_score = 0
        num = divisors[0]

        # 遍历每个除数
        for i, it in enumerate(divisors):
            # 初始化当前除数的得分
            score = 0

            # 遍历每个数字
            for j, n in enumerate(nums):
                # 如果数字能被当前除数整除，增加得分
                if n % it == 0:
                    score += 1

            # 更新最大分数和对应的除数
            # 如果当前得分大于最大分数，更新最大分数和除数
            if score > max_score:
                num = it
            # 如果当前得分等于最大分数，用较小的除数替换
            elif score == max_score:
                num = min(num, it)

            # 更新最大分数
            max_score = max(max_score, score)

        # 返回得分最高且数值最小的除数
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.maxDivScore([4, 7, 9, 3, 9], [5, 2, 3]))
    print(s.maxDivScore([20, 14, 21, 10], [5, 7, 5]))
    print(s.maxDivScore([12], [10, 16]))
    print(s.maxDivScore([90, 84], [56, 6, 97, 72, 62, 39, 6, 73, 53, 71, 4]))
