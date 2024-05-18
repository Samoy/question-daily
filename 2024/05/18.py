from typing import List

# https://leetcode.cn/problems/find-the-maximum-divisibility-score/description/?envType=daily-question&envId=2024-05-18
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = 0
        num = divisors[0]
        for _, it in enumerate(divisors):
            score = 0
            for _, n in enumerate(nums):
                if n % it == 0:
                    score += 1
            if score > max_score:
                num = it
            elif score == max_score:
                num = min(num, it)
            max_score = max(max_score, score)
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.maxDivScore([4, 7, 9, 3, 9], [5, 2, 3]))
    print(s.maxDivScore([20, 14, 21, 10], [5, 7, 5]))
    print(s.maxDivScore([12], [10, 16]))
    print(s.maxDivScore([90, 84], [56, 6, 97, 72, 62, 39, 6, 73, 53, 71, 4]))
